import RequestUrlGetHelper 
import HtmlScraperHelper
import JSONHelper
from bs4 import BeautifulSoup
from WebScrapedObject import WebScrapedObject
import json

rawHtml = RequestUrlGetHelper.getUrlContent("http://toscrape.com/")
html = BeautifulSoup(rawHtml, 'html.parser')

aTags = HtmlScraperHelper.getContentFromHtmlViaAttribute('a', html, 'href')
pTags = HtmlScraperHelper.getContentFromHtmlViaDomNode('p', html)

trials = [WebScrapedObject("aTags", aTags), WebScrapedObject("pTags", pTags)]

jsonData = {}
for trial in trials:
    jsonData = JSONHelper.createJsonProperty(trial.PropertyName, trial.PropertyContent, jsonData)

with open('data.json', 'w') as outfile:
   json.dump(jsonData, outfile, sort_keys=True, indent=4)