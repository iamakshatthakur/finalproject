from django.urls import path
from home import views
from django.views.generic import TemplateView

app_name='home'

urlpatterns=[
    path('',views.home, name='home'),
    path("about/",views.about,name='about'),
    path("search/",views.search,name='search'),
]