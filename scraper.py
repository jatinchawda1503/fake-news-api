from requests_html import HTMLSession 
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urlparse

url_data = "https://news.yahoo.com/a-north-carolina-city-hired-a-black-town-manager-then-its-entire-police-force-resigned-224423896.html"

def scrape_data(url):
    
    websites = ['news.yahoo.com', 'www.foxnews.com','www.huffpost.com','www.latimes.com','www.aljazeera.com','www.bbc.com','www.dailymail.co.uk',' www.forbes.com']
    url_base =  urlparse(url)
    
    def get_html(url):
        session = HTMLSession()
        page = session.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        return soup


    #news.yahoo.com
    if url_base.netloc == websites[0]:
        soup = get_html(url)
        list = soup.find('article', class_="caas-container")
        title = list.find('header', class_="caas-title-wrapper").text
        author = list.find('div', class_="caas-attr-item-author").text
        text = list.find(class_="caas-body").text
        
    #www.foxnews.com
    elif url_base.netloc == websites[1]:
        soup = get_html(url)
        list = soup.find('body', class_="fn article-single")
        title = list.find('h1', class_="headline").text
        author = list.find('a', class_="author-byline").text
        text = list.find(class_="article-body").text

    #www.huffpost.com    
    elif url_base.netloc == websites[2]:
        pass
    
    #www.latimes.com
    elif url_base.netloc == websites[3]:
        pass

    elif url_base.netloc == websites[4]:
        pass 
    
    elif url_base.netloc == websites[5]:
        pass
    
    #www.dailymail.co.uk
    elif url_base.netloc == websites[6]:
        list = soup.find('div', id="content")
        title = list.find('h2').text
        author = list.find('a', class_="author").text
        text = list.find('div', itemprop="articleBody").text
    
    elif url_base.netloc == websites[7]:
        pass
    article = {'title': [title], 'author': [author], 'text': [text]}
    data_df = pd.DataFrame(article)
    return data_df
