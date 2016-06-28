from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.core import serializers
from django.http import HttpResponse



# Create your views here.

def post_list(request):
	posts = Post.objects.all()
	return render(request, 'blog/post_list.html', {'posts': posts})
	