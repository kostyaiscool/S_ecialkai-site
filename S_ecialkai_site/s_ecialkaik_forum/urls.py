from django.urls import path
from .views import *

urlpatterns = [
    path('create/', CreatePostView.as_view()),
    path('posts/', ListPostView.as_view())
    
]