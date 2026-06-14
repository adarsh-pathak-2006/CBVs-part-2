from django.shortcuts import render,redirect
from django.views.generic import TemplateView, ListView,DetailView, CreateView
from django.views import View
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

class createBlog(View):
    def get(self, request):
        return render(request, 'create_blog.html')
    
    def post(self, request):
        blogs.objects.create(
            title=request.POST.get('title'),
            content=request.POST.get('content'),
        )
        return redirect('home')

