from .views import register
from django.urls import path
app_name = 'users'
urlpatterns = [
    path('', register, name ='register'),
]