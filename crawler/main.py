import requests
from bs4 import BeautifulSoup
from os import path
from spider import Spider


spider = Spider(limit=10)
print(spider.get_limit())
