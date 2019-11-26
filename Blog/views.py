from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request,blog_id):
    return HttpResponse("Hello Detail, This is the Id : " + str(blog_id))