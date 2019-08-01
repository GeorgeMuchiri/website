from django.urls import path, include
from . import views

urlpatterns = [
    path('',  views.index, name='home-page'),
    path('about/', views.about, name='about'),
    path('sermons/', views.sermons, name='sermons'),
    path('contact/', views.contact, name='contact'),
    path('category/', views.categories, name='category'),
    path('marriage/', views.marriage, name='marriage'),
    path('wisdom/', views.wisdom, name='wisdom'),
    path('foundation/', views.foundation, name='foundation'),
]
