from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegiserView.as_view(), name = 'register'),   
    path('login/', JustView.as_view(), name = 'login'),      
]