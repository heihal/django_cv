from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.order_by('title')
    return render(request, 'cv/skills.html',  {'posts': posts})
