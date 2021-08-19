from django.urls import path
from video import views
# from video.views import categories,categoryviews,article_detail


app_name='video'
urlpatterns=[
    path('categorylist/',views.category_list,name='category'),
    path('<slug:category_slug>/',views.category_view,name='category_view'),
    path('postComment',views.postComment, name='postComment'),
    path('<slug:article_slug>',views.article_detail, name='article_detail'),
    #path('slug:category_slug>/',ArticleDetail.as_view(),name='article_detail'),
    #path('slug:category_slug>/',categoryviews.as_view(),name='category_view'),
    ]