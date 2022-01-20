from bs4 import BeautifulSoup
import requests
from filedownloader import download_file

url = requests.get('https://rss.art19.com/apology-line')
soup = BeautifulSoup(url.content, 'xml')

entries = soup.find_all('item')
i = 0

for entry in entries:
    title = entry.title.text
    #summary = entry.summary.text
    link = entry.enclosure['url']   
    download_file(link, 'C:\\Users\\Morten\\Desktop\\School\\Bachelor\\filedownloader\\downloaded\\' + str(i) + '.mp3')
    i = i +1
    print(f"Title: {title}\n\nLink:{link}\n\n_______________________________________\n\n")

