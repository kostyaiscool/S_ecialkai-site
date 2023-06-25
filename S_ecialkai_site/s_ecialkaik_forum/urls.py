from django.urls import path
from .views import *

urlpatterns = [
    path('create/', CreatePostView.as_view(), name='create_post'),
    path('posts/', ListPostView.as_view(), name='list_posts'),
    
]