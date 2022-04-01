from bs4 import BeautifulSoup
import requests
import sys
import os
from filedownloader import download_file

xml = sys.argv[1] #First argument is link to rss feed
#downloadLocation = sys.argv[2] #'C:\\Users\\Morten\\Desktop\\School\\Bachelor\\filedownloader\\downloaded\\'
downloadLocation = '/media/morten/T7/Podcasts/'
language = sys.argv[2]
podcastName = sys.argv[3]
url = requests.get(xml)
soup = BeautifulSoup(url.content, 'xml')

entries = soup.find_all('item') #may also be named 'content' 'item' 'entry'

numToDownload = 0
for entry in entries:
    if(numToDownload<=50):
        title = entry.title.text
        link = entry.enclosure['url'] #may be named 'link' 'enclosure'
        if ".mp3" in link:
            if not os.path.isfile(downloadLocation + language + '/' + '-' + language + '-' + podcastName + '-' + title + '.mp3'):
                download_file(link, downloadLocation + language + '/' + '-' + language + '-' + podcastName + '-' + title + '.mp3')
                print(f"Title: {title}\n\nLink:{link}\n\n_______________________________________\n\n")
            else:
                print(f"Title:{title} Already Exist")
        numToDownload+=1

print("Finish")