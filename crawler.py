# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from scraper import extract_data

def get_html_page(url):
    '''
    Receives a url and returns its contents,
    If your status is different from 200 (ok)
    or the page does not exist, returns None.
    '''
    try:
        html = requests.get(url)
        if html.status_code != 200:
            print('Error, Can not open page ->{}'.format(str(url)))
            print('Status -> {}'.format(str(html.status_code)))
            return None
        else:
            return html
    except Exception as e:
        print(e)
        return None 


def crawl(pages, depth):
    '''
    Receive a list of pages and the depth of the crawler
    '''
    for i in range(depth):
        print('Depth: {0}'.format(i))
        new_pages = set()
       
        # for page in page list
        for page in pages:            
            page_data = get_html_page(page)
            if page_data:            
                soup = BeautifulSoup(page_data.text, 'lxml')

                # find all links on the page                
                for link in soup.find_all('a', href=True):
                    if not "#" in link['href']:
                        url = urljoin(str(page), str(link.get('href')))
                        if url[0:4] == 'http':
                            new_pages.add(url)
                
                # Add links as new pages
                pages = new_pages                    

                # Extract page data
                url = page
                title, description, text = extract_data(page_data)
                
                # Print results
                print('Url: {0}\nTitle: {1}\nDescription: {2}'.format(url, title, description))
                print('Text: {0}'.format(text))
                print(50*'-')
            

if __name__ == '__main__':
    crawl(['https://www.python.org/'], 2)