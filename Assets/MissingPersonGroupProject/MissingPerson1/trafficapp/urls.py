from django.urls import path
from .views import indexPageView
from .views import aboutPageView
from .views import MissingpeoplePageView
from .views import ContactPageView

urlpatterns = [
     path("", indexPageView, name="index"),
     path("about/", aboutPageView, name = "about"),
     path("index/", indexPageView, name="index"),
     path("missingpeople/", MissingpeoplePageView, name="missingpeople"),
     path("contact/", ContactPageView, name="contact")
]
