from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from .models import Post
from .models import PostNew

# Create your views here.

# def home_page_view(request):
#     return HttpResponse('<h1>Hello World</h1>')

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ListPageView(ListView):
    model = Post
    template_name = 'list.html'

class ListNewPageView(ListView):
    model = PostNew
    template_name = 'list_new.html'
    context_object_name = 'post_new_obj'

class PostDetailView(DetailView):
    model = PostNew
    template_name = 'post_detail.html'