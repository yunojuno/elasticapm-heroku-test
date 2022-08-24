from django.contrib import admin
from django.urls import path

from .views import error, index

admin.autodiscover()

urlpatterns = [
    path("error/", error, name="force_error"),
    path("", index),
]
