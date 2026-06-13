from .views import home, news_detail, category_news, register

from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('category/<str:category>/', views.category_news, name='category_news'),

    path('register/', views.register, name='register'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('dashboard/create/', views.news_create, name='news_create'),
    path('dashboard/edit/<int:pk>/', views.news_edit, name='news_edit'),
    path('dashboard/delete/<int:pk>/', views.news_delete, name='news_delete'),
]