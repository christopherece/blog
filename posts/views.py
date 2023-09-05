from django.shortcuts import get_object_or_404, render
from .models import Post
# Create your views here.


def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post
    }
    return render(request, 'posts/post.html', context)

def search(request):
    return render(request, 'posts/search.html')