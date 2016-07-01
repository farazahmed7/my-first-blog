from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import Post,Userdetail
from django.core import serializers
from django.http import HttpResponse
from .forms import PostForm
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view







# Create your views here.

def post_list(request):
	posts = Post.objects.all()
	return render(request, 'blog/post_list.html', {'posts': posts})
	
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})	

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
	
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})	

@csrf_exempt
def android(request):
	if request.method=='POST':
		_name=str(request.POST['name'])
		_email=str(request.POST['email'])
		Userdetail.objects.create(name=_name,email_id=_email)
		return HttpResponse("saved")
	
	return HttpResponse("not saved")	
	
@csrf_exempt	
def newPostFromAndroid(request):
	if request.method=='POST':
		_title=str(request.POST['title'])
		_text=str(request.POST['text'])
		Post.objects.create(title=_title,text=_text)
		return HttpResponse("saved")
	
	return HttpResponse("not saved")
	
@csrf_exempt
@api_view(['GET', 'POST', ])	
def displayAndroid(request):
	if request.method=='GET':
		posts=Post.objects.filter(id=1)
		ser=UserSerializer(posts,many=True)
		return Response(ser.data)
	return HttpResponse("not saved")	
		
	

    