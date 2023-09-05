from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Category, Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'pages/index.html', context)

def post(request):
    return render(request, 'pages/post.html')

def about(request):
    return render(request, 'pages/about.html')
