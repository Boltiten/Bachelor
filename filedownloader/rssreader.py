from bs4 import BeautifulSoup
import requests
import sys
import os
from filedownloader import download_file

xml = sys.argv[1] #First argument is link to rss feed
downloadLocation = sys.argv[2] #'C:\\Users\\Morten\\Desktop\\School\\Bachelor\\filedownloader\\downloaded\\'
url = requests.get(xml)
soup = BeautifulSoup(url.content, 'xml')

entries = soup.find_all('item') #may also be named 'content' 'item' 'entry' 
i = 0

for entry in entries:
    title = entry.title.text
    #summary = entry.summary.text
    link = entry.enclosure['url'] #may be named 'link' 'enclosure'
    if not os.path.isfile(downloadLocation + title + '.wav'): #str(i)||title
        download_file(link, downloadLocation + title + '.wav') #str(i)||title
        print(f"Title: {title}\n\nLink:{link}\n\n_______________________________________\n\n")
    else:
        print(f"Title:{title} Already Exist")
    i = i +1

