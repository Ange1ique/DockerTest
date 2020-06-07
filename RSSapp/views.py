from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
import datetime
from .models import RSS_URLS, Feed
from .forms import InputURLS
import feedparser
from django.forms import formset_factory
from django.forms.models import modelformset_factory


# Create your views here.
def Index(request):
    now = datetime.datetime.now()
    str_now = now.strftime("%d %B, %Y")

    if request.method == 'POST':
        form = InputURLS(request.POST)
        if not form.has_changed():
            context = {"form": form, "date": str_now, "error": "Please enter or select at least one url"}

        elif form.is_valid():
            data = []
            new = form.cleaned_data['urlNew']
            if new != "":
                checkFeed = feedparser.parse(new)
                if checkFeed.bozo:
                    data.append([new, "The given url was unfortunately not well-formed"])
                else:
                    title = checkFeed.get('feed').get('title')
                    if 'youtube' in new:
                        title = "YouTube: " + str(title)
                    data.append([title, checkFeed])
                    newInstance = RSS_URLS(url = new, title = title)
                    try:
                        newInstance.save()
                    except:
                        # url was not unique -> already in database
                        pass

            # if you only want the titles, but there is a possibility that they are not unique:
            # selected = form.cleaned_data['urlsCheckboxes']

            # get list of unique labels that are selected (to_field_name = "url")
            selected = request.POST.getlist("urlsCheckboxes")
            dbTitles = RSS_URLS.objects.all()
            for item in selected:
                instance = dbTitles.get(url=item)
                title = instance.title
                data.append([title, feedparser.parse(item)])

            context = {"data": data, "date": str_now}

            return render(request, 'results.html', context)

        else:
            context = {"form": form, "date": str_now, "error": "Something went wrong, please try again"}

    else:
        form = InputURLS()
        context = {"form": form, "date": str_now}

    return render(request, 'index.html', context)
