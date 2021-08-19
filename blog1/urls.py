from django.urls import path,include
from blog1 import views

app_name='blog1'
urlpatterns=[
    path('',views.blog1Home,name='blog1Home'),
    path('<int:pk>',views.blog1Post,name="blog1Post"),


]