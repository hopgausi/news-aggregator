from django.urls import path
from . import views

app_name='news_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('<str:content_about>/', views.get_all_news_by_content, name='all-by-content-news'), 
    path('<str:category>/<str:content_about>/', views.get_news_by_content, name='get-news'), 
]
