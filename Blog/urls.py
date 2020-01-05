
from .views import index, detail, addpost
from django.urls import path
app_name = 'Blog'
urlpatterns = [
    path('', index, name ='blog'),
    path('addnew', addpost, name ='addnew'),
    path('<int:blog_id>', detail, name ="detail"),
]
