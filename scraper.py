from pip import main
from requests_html import HTMLSession 
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urlparse

url_data = "https://news.yahoo.com/a-north-carolina-city-hired-a-black-town-manager-then-its-entire-police-force-resigned-224423896.html"

def scrape_data(url):
    
    websites = ['news.yahoo.com', 'www.foxnews.com','www.huffpost.com','www.latimes.com','www.aljazeera.com','www.bbc.com','www.dailymail.co.uk','www.thesun.co.uk','www.cnbc.com','edition.cnn.com']
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
        main_text = list.find('div',class_="caas-body").findAll("p", recursive=False)
        text = ''.join([str(item.text) for item in main_text ])
        
    #www.foxnews.com
    elif url_base.netloc == websites[1]:
        soup = get_html(url)
        list = soup.find('body', class_="article-single")
        title = list.find('h1', class_="headline").text
        author = list.find('div', class_="author-byline").find("a").text
        main_text = list.find('div',class_="article-body").findAll("p", recursive=False)
        text = ''.join([str(item.text) for item in main_text ])


    #www.huffpost.com    
    elif url_base.netloc == websites[2]:
        soup = get_html(url)
        list = soup.find('body', class_="entry")
        title = list.find('h1', class_="headline").text        
        author = list.find('div', class_="entry__byline__author").find("a")['data-vars-item-name']
        main_text = list.find_all("div",class_='cli-text')
        text = ''.join([str(item.text) for item in main_text ])
        

    
    #www.latimes.com
    elif url_base.netloc == websites[3]:
        soup = get_html(url)
        list = soup.find('body', class_="page-body")
        title = list.find('h1', class_="headline").text
        author = list.find('div', class_="author-name").find("a").text
        main_text = list.find('div',class_="rich-text-article-body-content").findAll("p", recursive=False)
        text = ''.join([str(item.text) for item in main_text ])
        

    #www.aljazeera.com
    elif url_base.netloc == websites[4]:
        soup = get_html(url)
        list = soup.find('div', id="article")
        title = list.find('header', class_="article-header").find('h1').text
        author = list.find('span', class_="article-author-name-item").find("a",class_='author-link').text
        main_text = list.find('div',class_="wysiwyg").findAll("p", recursive=False)
        text = ''.join([str(item.text) for item in main_text ])

    #www.bbc.com
    elif url_base.netloc == websites[5]:
        soup = get_html(url)
        list = soup.find('div', class_="ssrcss-rgov1k-MainColumn")
        title = list.find('h1', id="main-heading").text
        author = list.find('p', class_="ssrcss-ugte5s-Contributor").text
        main_text = list.find_all("p",'ssrcss-1q0x1qg-Paragraph')
        text = ''.join([str(item.text) for item in main_text ])
        print(text)
    
    #www.dailymail.co.uk
    elif url_base.netloc == websites[6]:
        soup = get_html(url)
        list = soup.find('div', id="content")
        title = list.find('h2').text
        author = list.find('a', class_="author").text
        main_text = list.find('div', itemprop="articleBody").findAll("p", recursive=False)
        text = ''.join([str(item.text) for item in main_text ])
        

    # www.thesun.co.uk
    elif url_base.netloc == websites[7]:
        soup = get_html(url)
        list = soup.find('article', class_="article theme-news")
        title = list.find('h1', class_="article__headline").text
        author = list.find('a', class_="author url fn article__author-link t-p-color").text
        main_text = list.find('div',class_="article__content").findAll("p", recursive=False)
        text = ''.join([str(item.text) for item in main_text ])
        
    #www.cnbc.com
    elif url_base.netloc == websites[8]:
        soup = get_html(url)
        list = soup.find('div', class_="PageBuilder-pageWrapper")
        title = list.find('h1', class_="ArticleHeader-headline").text
        author = list.find('a', class_="Author-authorName").text
        main_text = list.find('div',class_="ArticleBody-articleBody").findAll("div",class_="group", recursive=False)
        text = ''.join([str(item.text) for item in main_text ])

    #edition.cnn.com
    elif url_base.netloc == websites[9]:
        soup = get_html(url)
        list = soup.find('article', class_="pg-rail-tall")
        title = list.find('h1', class_="pg-headline").text
        author = list.find('a').text
        main_text = list.find('section',class_="zn-body-text")
        text = ''.join([str(item.text) for item in main_text ])




    article = {'title': [title], 'author': [author], 'text': [text]}
    data_df = pd.DataFrame(article)
    return data_df

url_data = "https://www.foxnews.com/media/idaho-sheriff-sends-dire-warning-idiotic-biden-officials-cusp-complete-collapse"

data = scrape_data(url_data)
print(data)