from typing import Any, Dict
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from .models import Post
from .forms import CreatePostForm

class CreatePostView(CreateView):
    template_name = 'forum/create_post.html'
    form_class = CreatePostForm

    def form_valid(self, form):
        form.save()
        # login(self.request, post)
        return redirect('list_posts')
class ListPostView(ListView):
    template_name = 'forum/list_post.html'
    model = Post
    context_object_name = 'posts'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
      
        return context