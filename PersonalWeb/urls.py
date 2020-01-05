
from .views import home
from django.urls import path
app_name = 'PersonalWeb'
urlpatterns = [
    path('',home, name ='index'),
]
