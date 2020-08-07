import os
from newsapi import NewsApiClient
import datetime

# Init
api_key = os.environ.get('api_key')
newsapi = NewsApiClient(api_key=api_key)

#sources
sources = 'abc-news, al-jazeera-english,ars-technica,bbc-news,bbc-sport,bleacher-report,bloomberg,business-insider,buzzfeed,cnn,crypto-coins-news, entertainment-weekly,espn,football-italia,fox-news,fox-sports,hacker-news,medical-news-today,msnbc,mtv-news,mtv-news-uk,national-geographic,national-review,news24,new-scientist,new-york-magazine,nfl-news,techcrunch,techradar,the-verge,the-wall-street-journal,the-washington-post,wired',
    
# Today's date
date_today = datetime.date.today()

# Date five days ago
timedelta  = datetime.timedelta(days=5)
start_date = (date_today - timedelta)

# get content
def get_all_content(content_about):
    content = newsapi.get_everything(q=content_about,
                                     language="en" , 
                                     from_param=start_date,
                                     to=date_today,
                                     sources=str(sources),
                                     sort_by="relevancy",
                                     page_size=50
                                     )
    content = content.get('articles')                               
    return content

# General headlines
def get_headlines():
    content = newsapi.get_top_headlines(
        sources=str(sources),
        language="en" , 
        page_size=50,
        )
    content = content.get('articles')                               
    return content



