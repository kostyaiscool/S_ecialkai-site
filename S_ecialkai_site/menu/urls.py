from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name = 'index'), 
    path('Donate/', DonateView.as_view(), name = 'donate'),
    path('Games/', GameView.as_view(), name = 'games'),
    
]