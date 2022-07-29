from requests_html import HTMLSession 
from bs4 import BeautifulSoup
import pandas as pd

def get_html(url):
    session = HTMLSession()
    page = session.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup

def get_yahoo_data(soup):
    list = soup.find('article', class_="caas-container")
    title = list.find('header', class_="caas-title-wrapper").text
    author = list.find('div', class_="caas-attr-item-author").text
    main_text = list.find('div',class_="caas-body").findAll("p", recursive=False)
    return title, author, main_text

def get_fox_data(soup):
    list = soup.find('body', class_="article-single")
    title = list.find('h1', class_="headline").text
    author = list.find('div', class_="author-byline").find("a").text
    main_text = list.find('div',class_="article-body").findAll("p", recursive=False)
    return title, author, main_text


def get_huffpost_data(soup):
    list = soup.find('body', class_="entry")
    title = list.find('h1', class_="headline").text
    if list.find('div', class_="entry__byline__author") is True:        
        author = list.find('div', class_="entry__byline__author").find("a")['data-vars-item-name'] 
    else:    
        author = list.find('span', class_="entry-wirepartner__byline").text
    main_text = list.find_all("div",class_='cli-text')
    return title, author, main_text

def get_latintimes_data(soup):
    list = soup.find('body', class_="page-body")
    title = list.find('h1', class_="headline").text
    author = list.find('div', class_="author-name").find("a").text
    main_text = list.find('div',class_="rich-text-article-body-content").findAll("p", recursive=False)
    return title, author, main_text

def get_aljazeera_data(soup):
    list = soup.find('div', id="article")
    title = list.find('header', class_="article-header").find('h1').text
    author = list.find('span', class_="article-author-name-item").find("a",class_='author-link').text
    main_text = list.find('div',class_="wysiwyg").findAll("p", recursive=False)
    return title, author, main_text

def get_bbc_data(soup):
    list = soup.find('div', class_="ssrcss-rgov1k-MainColumn")
    title = list.find('h1', id="main-heading").text
    author = list.find('p', class_="ssrcss-ugte5s-Contributor").text
    main_text = list.find_all("p",'ssrcss-1q0x1qg-Paragraph')
    return title, author, main_text

def get_dailymail_data(soup):
    list = soup.find('div', id="content")
    title = list.find('h2').text
    author = list.find('a', class_="author").text
    main_text = list.find('div', itemprop="articleBody").findAll("p", recursive=False)
    return title, author, main_text

def get_thesun_data(soup):
    list = soup.find('article', class_="article theme-news")
    title = list.find('h1', class_="article__headline").text
    author = list.find('a', class_="author url fn article__author-link t-p-color").text
    main_text = list.find('div',class_="article__content").findAll("p", recursive=False)
    return title, author, main_text


def get_cnbc_data(soup):
    list = soup.find('div', class_="PageBuilder-pageWrapper")
    title = list.find('h1', class_="ArticleHeader-headline").text
    author = list.find('a', class_="Author-authorName").text
    main_text = list.find('div',class_="ArticleBody-articleBody").findAll("div",class_="group", recursive=False)
    return title, author, main_text


def get_cnn_data(soup):
    list = soup.find('article', class_="pg-rail-tall")
    title = list.find('h1', class_="pg-headline").text
    author = list.find('a').text
    main_text = list.find('section',class_="zn-body-text")
    return title, author, main_text

def get_struct_data(title, author, main_text):
    text = ''.join([str(item.text) for item in main_text ])
    article = {'title': [title], 'author': [author], 'text': [text]}
    data_df = pd.DataFrame(article)
    return data_df