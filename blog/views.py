from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .models import Type

def base(request):
    tags = Type.objects.all()
    return render(request, 'blog/base.html', {'tags': tags})

def body(request):
    return render(request, 'blog/body.html', {})

def post_list(request):
    tags = Type.objects.all()
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts, 'tags': tags})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
