
from .views import index, detail
from django.urls import path

urlpatterns = [
    path('', index, name ='index'),
    path('<int:blog_id>', detail, name ="detail"),
]
