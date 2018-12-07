import json

import RequestUrlGetHelper 
import HtmlScraperHelper
import JSONHelper

from bs4 import BeautifulSoup
from WebScrapedObject import WebScrapedObject

currentUrl = "http://toscrape.com/"
rawHtml = RequestUrlGetHelper.getUrlContent(currentUrl)
html = BeautifulSoup(rawHtml, 'html.parser')

aTags = HtmlScraperHelper.getContentFromHtmlViaAttribute('a', html, 'href')
pTags = HtmlScraperHelper.getContentFromHtmlViaDomNode('p', html)

webScrapedObjects = [WebScrapedObject("aTags", aTags), WebScrapedObject("pTags", pTags)]

jsonData = {}
for webScrapedObject in webScrapedObjects:
    jsonData = JSONHelper.createJsonProperty(webScrapedObject.PropertyName, webScrapedObject.PropertyContent, jsonData)

with open('data.json', 'w') as outfile:
   json.dump(jsonData, outfile, sort_keys=True, indent=4)