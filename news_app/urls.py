from django.urls import path
from . import views

app_name='news_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('<str:content_about>/', views.get_all_news_by_content, name='all-by-content-news'), 
    path('<str:category>/<str:content_about>/', views.get_news_by_content, name='get-news'), 
    # path('machine-learning-artificial-intelligence', views.ml_ai, name='ml-ai'),
    # path('sotware-engineer', views.sotware_engineer, name='sotware-engineer'),
    # path('dev-ops', views.dev_ops, name='dev-ops'),
    # #science
    # path('science/all', views.dev_ops, name='science'),
    # path('science/health', views.categorized_news, name='s-health'),
    # path('science/education', views.dev_ops, name='s-education'),
    # path('science/finance', views.dev_ops, name='s-finance'),
    # path('science/agriculture', views.dev_ops, name='s-agriculture'),
    # #tech
    # path('technology/all/', views.technology, name='technology'),
    # path('technology/<str:content_about>/<str:category>/', views.categorized_news, name='t-health'),
    # path('technology/<str:content_about>/', views.categorized_news, name='t-education'),
    # path('technology/<str:content_about>/', views.categorized_news, name='t-finance'),
    # path('technology/<str:content_about>/', views.categorized_news, name='t-agriculture'),
    # #sports
    # path('sports/football', views.dev_ops, name='football'),
    # path('sports/nba', views.dev_ops, name='nba'),
    # path('sports/netball', views.dev_ops, name='netball'),
]
