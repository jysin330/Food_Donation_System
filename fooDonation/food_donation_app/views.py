from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("this is my homepage")


def contact(request):
    return HttpResponse("this is my contact")


def search(request):
    return HttpResponse("this is my search")


def about(request):
    return HttpResponse("this is my about")


def tracker(request):
    return HttpResponse("this is my tracker")


def donate(request):
    return HttpResponse("this is my donate")


def work(request):
    return HttpResponse("this is my work")
