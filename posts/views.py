from django.shortcuts import get_object_or_404, render
from .models import Post
# Create your views here.


def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

# Fetch the next and previous posts based on the creation date
    next_post = Post.objects.filter(created_at__gt=post.created_at).order_by('created_at').first()
    previous_post = Post.objects.filter(created_at__lt=post.created_at).order_by('-created_at').first()

    context = {
        'post': post,
        'next_post':next_post,
        'previous_post':previous_post,
    }
    return render(request, 'posts/post.html', context)

def search(request):
    return render(request, 'posts/search.html')