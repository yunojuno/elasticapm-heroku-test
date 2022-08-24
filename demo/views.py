from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html")


def error(request: HttpRequest) -> HttpResponse:
    raise Exception("This is an untrapped error")
