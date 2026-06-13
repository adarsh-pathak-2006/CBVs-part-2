from django.shortcuts import render
from django.views.generic import TemplateView, ListView,DetailView, CreateView
from .models import blogs
from django.urls import reverse_lazy

class homeview(TemplateView):
    template_name='home.html'


class AboutView(TemplateView):
    template_name='about.html'

class home_view_data(ListView):
    model=blogs
    template_name='home.html'
    context_object_name='blog'

class blog_detail_view(DetailView):
    model=blogs
    template_name='individual.html'
    context_object_name='blogs'

class createBlog(CreateView):
     model=blogs
     template_name='create_blog.html'
     fields=['title', 'content']
     success_url=reverse_lazy('create')

