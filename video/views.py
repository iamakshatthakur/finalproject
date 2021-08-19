from django.shortcuts import render
from .models import categorylist,Item,VideoComment
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.contrib import messages
from django.http import HttpResponse , HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def category_list(request):
    print("invoked1")
    categories=categorylist.objects.all()
    return render(request,"video/categorylist.html",{ 'categories': categories })


# class categories(ListView):
#    model=categorylist
#    context_object_name='categories'
#    template_name='video/categorylist.html'

def category_view(request,category_slug):
    print("invoked2")
    category = categorylist.objects.filter(slug=category_slug).first()
    article=Item.objects.filter(category=category)
    return render(request,'video/categoryview.html',{'category':category,"article": article})

# class categoryviews(ListView):
#     template_name='video/categoryview.html'
#     context_object_name='article'

#     def get_queryset(self):
#         self.category=get_object_or_404(categorylist,slug=self.kwdargs['category_slug'])
#         return Item.objects.filter(category=self.category)

#     def get_context_data(self,**kwdargs):
#         context = super().get_context_data(**kwargs)
#         context["categoryview"] = self.category
#         return context
        
# class ArticleDetail(DetailView):
#     slug_url_kwarg='article_slug'
#     model=Item
#     template_name='video/articledetail.html'
#     context_object_name='article'

def article_detail(request,article_slug):
    article=Item.objects.filter(slug=article_slug).first()
    comments=VideoComment.objects.filter(article=article,parent=None)
    replies=VideoComment.objects.filter(article=article).exclude(parent=None)
    repDict={}
    for reply in replies:
        if reply.parent.srno not in repDict.keys():
            repDict[reply.parent.srno]=[reply]
        else:
            repDict[reply.parent.srno].append(reply)

    context={'article':article,'comments':comments,'user':request.user,'repDict':repDict}
    print("Now i m called")

    return render(request,'video/article_detail.html', context)


def postComment(request):
    print("hi")
    if request.method=="POST":
        print("hello")
        comment=request.POST.get("comment")
        user=request.user
        articleSno=request.POST.get("articleSno")
        article=Item.objects.get(sno=articleSno)
        parentSno=request.POST.get("parentSno")
        print("response")
        if parentSno=="":
            comment=VideoComment(comment=comment,user=user,article=article)
            print("hello again")
            comment.save()
            messages.success(request,"Your comment has been posted successfully")
        else:
            parent=VideoComment.objects.get(srno=parentSno)
            comment=VideoComment(comment=comment,user=user,article=article,parent=parent)

            comment.save()
            messages.success(request,"Your reply has been posted successfully")
        return HttpResponseRedirect(reverse('video:article_detail',args=(article.slug,)))