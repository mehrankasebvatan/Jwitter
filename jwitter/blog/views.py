from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post


def index(request):
    ret = '<body>'
    all_posts = Post.objects.all()
    for post in all_posts:
        ret = ret + '<p>' + post.text + '</p>' + '<hr>'

    ret = ret + '</body>'
    return HttpResponse(ret)
