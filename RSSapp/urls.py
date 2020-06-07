from django.urls import path
from . import views

# SET THE NAMESPACE!
app_name = 'RSSapp'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    path('', views.Index, name='index'),
]
