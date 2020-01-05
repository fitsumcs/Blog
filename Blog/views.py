from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog
from .forms import CommentForm, AddPost
from django.core.paginator import Paginator
def index(request):
  
    all_post = Blog.objects.order_by('-pubdate')
    paginator = Paginator(all_post, 2)
    page = request.GET.get('page')
    all_post = paginator.get_page(page)
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {"all_post" : all_post,'num_visits': num_visits}
    return render(request,'Blog/index.html',context)
def addpost(request):
    if request.method == 'POST':
        form = AddPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.reporter = request.user
            form.save()
            form = AddPost()

    else:
        form = AddPost()  
    context = {"form":form}
    return render(request,'Blog/addnew.html',context)

def detail(request,blog_id):
    single_post = Blog.objects.get(id=blog_id)
    comments = single_post.comment_set.all()
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = single_post
            form.save()
            form = CommentForm()

    else:
        form = CommentForm()  
    context = {"single_post" : single_post, "comments": comments, "form":form}
    del request.session['num_visits']
    return render(request,'Blog/detail.html',context)