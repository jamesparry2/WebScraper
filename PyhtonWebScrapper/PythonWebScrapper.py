import RequestUrlGetHelper 
import HtmlScraperHelper
from bs4 import BeautifulSoup

rawHtml = RequestUrlGetHelper.getUrlContent("http://toscrape.com/")
html = BeautifulSoup(rawHtml, 'html.parser')

aTags = HtmlScraperHelper.getContentFromHtmlViaAttribute('a', html, 'href')
print(aTags)