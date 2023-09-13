from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from .forms import BlogForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import os

# Create your views here.
@csrf_exempt
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'message':'Blog saved successfully!'})
        else:
            return JsonResponse({'message':'Blog not created'})
        
@csrf_exempt
def delete_blog(request,pk):
    blog = get_object_or_404(Blog,pk=pk)
    if request.method == 'DELETE':
        if blog.blog_file:
            os.remove(blog.blog_file.path)
        blog.delete()
        return JsonResponse({'message':'Blog deleted successfuly.'})
    return JsonResponse({'message':'Invalid requests56789'})

@csrf_exempt
def update_blog(request,pk):
    blog = get_object_or_404(Blog,pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES,instance=blog)
        if form.is_valid():
            if blog.blog_file and 'filename' in form.changed_data:
                os.remove(blog.blog_file.path)
            form.save()
            return JsonResponse({'message':'Blog updated successfully!'})
        else:
            return JsonResponse({'message':'Invalid data. plz chk ur input.'})
    else:
        form = BlogForm(instance=blog)


def show_blogs(request):
    blogs = Blog.objects.all()

    blogs_list =[{'id':blog.id,'name':blog.name,'blog_file':blog.blog_file.url} for blog in blogs]
    return JsonResponse({'Blogs':blogs_list})