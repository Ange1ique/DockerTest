from django import forms
from .models import RSS_URLS, Feed


class InputURLS(forms.Form):
    urlNew = forms.URLField(required=False, label="Enter a new url")
    urlsCheckboxes = forms.ModelMultipleChoiceField(
                        required = False,
                        widget = forms.CheckboxSelectMultiple,
                        queryset = RSS_URLS.objects.order_by('title').all(),
                        to_field_name = "url"
                        # queryset = RSS_URLS.objects.order_by('title').values_list("url", "title")
               )

    def __init__(self, *args, **kwargs):
        super(InputURLS, self).__init__(*args, **kwargs)
        self.fields['urlNew'].widget.attrs.update({'class': 'form-control'})
