from dataclasses import field
from email import contentmanager
from multiprocessing import context
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy
# Create your views here.
from blog.models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    # context_object_name = "bla"


class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ['title', 'author', 'body']


class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_update.html"
    fields = ['title', 'body']
    # fields  = "__all__"


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy('home')
