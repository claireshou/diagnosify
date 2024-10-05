from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    return HttpResponse("Welcome to the homepage!")


def my_view(request):
    return HttpResponse("Hello, this is your backend response!")


