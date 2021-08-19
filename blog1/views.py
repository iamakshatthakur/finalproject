from django.shortcuts import render , redirect, get_object_or_404
from django.http import HttpResponse
from blog1.models import Post
from django.contrib import messages
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from django.template.loader import render_to_string
from django.http import JsonResponse

# Create your views here.  

def blog1Home(request):
    allPosts=Post.objects.all()
    context={'allPosts':allPosts}
    return render(request,'blog1/blog1home.html', context)


def blog1Post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog1/blog1post.html',{'post':post})

