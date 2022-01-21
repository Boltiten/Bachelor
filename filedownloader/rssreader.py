from bs4 import BeautifulSoup
import requests
import sys
import os
from filedownloader import download_file

xml = sys.argv[1] #First argument is link to rss feed
downloadLocation = sys.argv[2] #'C:\\Users\\Morten\\Desktop\\School\\Bachelor\\filedownloader\\downloaded\\'
url = requests.get(xml)
soup = BeautifulSoup(url.content, 'xml')

entries = soup.find_all('item')
i = 0

for entry in entries:
    title = entry.title.text
    #summary = entry.summary.text
    link = entry.enclosure['url']
    if not os.path.isfile(downloadLocation + str(i) + '.wav'):
        download_file(link, downloadLocation + str(i) + '.wav')
        print(f"Title: {title}\n\nLink:{link}\n\n_______________________________________\n\n")
    else:
        print(f"Title:{title} Already Exist")
    i = i +1

