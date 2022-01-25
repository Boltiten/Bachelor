import requests
import sys
from bs4 import BeautifulSoup

def download_file(url, filename=''):
    try:
        if filename:
            pass
        else:
            filename = req.url[downloadUrl.rfind('/')+1:]        
        with requests.get(url) as req:
            with open(filename, 'wb') as f:
                f.write(req.content)
                #for chunk in req.iter_content(chunk_size = 8192):
                #    if chunk:
                #        f.write(chunk)
            return filename
    except Exception as e:
        print(e)
        return None


#downloadLink = sys.argv[1]

#download_file(downloadLink, 'C:\\Users\\Morten\\Desktop\\School\\Bachelor\\filedownloader\\downloaded\\' + sys.argv[2])
