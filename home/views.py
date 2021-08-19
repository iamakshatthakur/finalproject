from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib import messages
from blog1.models import Post

# Create your views here.
def home(request):
    return render(request,'home/home.html')

def about(request):
    return render(request,'home/about.html')

# class AboutView(TemplateView):
#     template_name='home/about.html'

def login(request):
    return render(request,'home/login.html')

def contact(request):
    return render(request,'home/contact.html')

def help(request):
    return render(request,'home/help.html')

def search(request):
    query = request.GET['query']
    if len(query)>78:
        allPosts = Post.object.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)
    if allPosts.count()==0:
        messages.warning(request,"No search result found. please refine your query")
    params = {'allPosts':allPosts,'query':query}
    return render (request,'home/search.html',params)
