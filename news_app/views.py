from django.shortcuts import render
from .news_api import get_all_content, get_headlines


# Home - Breaking news
def home(request):
    content_about = 'Breaking news'
    context = {
            'title': content_about,
            'all_articles' : get_headlines()
    }
    template_name = 'news_app/index.html'
    return render(request, template_name, context)


# get news by content_about
def get_all_news_by_content(request, content_about ): 
    context = {
            'title': content_about,
            'all_articles' : get_all_content(content_about)
    }
        
    template_name = 'news_app/index.html'
    return render(request, template_name, context)


# get news by content_about
def get_news_by_content(request, category, content_about):
    context = {
            'title': content_about,
            'all_articles' : get_all_content(content_about)
    }
        
    template_name = 'news_app/index.html'
    return render(request, template_name, context)
