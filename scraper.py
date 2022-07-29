import pandas as pd
from urllib.parse import urlparse
from sites.scrape import get_html
from sites.scrape import get_yahoo_data,get_fox_data,get_huffpost_data,get_latintimes_data,get_aljazeera_data,get_bbc_data,get_dailymail_data,get_thesun_data,get_cnbc_data,get_cnn_data
from sites.scrape import get_struct_data

def scrape_data(url):
    
    websites = ['news.yahoo.com', 'www.foxnews.com','www.huffpost.com','www.latimes.com','www.aljazeera.com','www.bbc.com','www.dailymail.co.uk','www.thesun.co.uk','www.cnbc.com','edition.cnn.com']
    url_base =  urlparse(url)
    soup = get_html(url)

    #news.yahoo.com
    if url_base.netloc == websites[0]:
        title, author , main_text  = get_yahoo_data(soup)     
        
    #www.foxnews.com
    elif url_base.netloc == websites[1]:
        title, author, main_text  = get_fox_data(soup)

    #www.huffpost.com    
    elif url_base.netloc == websites[2]:
        title, author, main_text  = get_huffpost_data(soup)
        
    #www.latimes.com
    elif url_base.netloc == websites[3]:
        title, author, main_text  = get_latintimes_data(soup)
        
    #www.aljazeera.com
    elif url_base.netloc == websites[4]:
        title, author, main_text  = get_aljazeera_data(soup)

    #www.bbc.com
    elif url_base.netloc == websites[5]:
        title, author, main_text  = get_bbc_data(soup)

    #www.dailymail.co.uk
    elif url_base.netloc == websites[6]:
        title, author, main_text  = get_dailymail_data(soup)
        

    # www.thesun.co.uk
    elif url_base.netloc == websites[7]:
        title, author, main_text  = get_thesun_data(soup)
        
    #www.cnbc.com
    elif url_base.netloc == websites[8]:
        title, author, main_text  = get_cnbc_data(soup)

    #edition.cnn.com
    elif url_base.netloc == websites[9]:
        title, author, main_text  = get_cnn_data(soup)


    data = get_struct_data(title,author, main_text)

    return data


