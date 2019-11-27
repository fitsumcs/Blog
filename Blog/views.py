from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog


def index(request):
    all_post = Blog.objects.all()
    context = {"all_post" : all_post}
    return render(request,'Blog/index.html',context)

def detail(request,blog_id):
    return HttpResponse("Hello Detail, This is the Id : " + str(blog_id))