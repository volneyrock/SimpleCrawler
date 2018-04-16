# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

PARSER = 'lxml'

def extract_data(html):
    title = extract_title(html)
    description = extract_description(html)
    text = extract_text(html)

    return title, description, text

def extract_title(html):
    soup = BeautifulSoup(html.text, PARSER)
    try:
        title = soup.title.string
    except:
        title = None
    return title

def extract_description(html):
    soup = BeautifulSoup(html.text, PARSER)
    description = soup.find_all('meta', attrs={'name':'description'})

    for i in description:
        return i["content"]

def extract_text(html):
    text = ""
    soup = BeautifulSoup(html.text, PARSER)

    for i in soup.find_all('p'):
        text += i.get_text()

    return text