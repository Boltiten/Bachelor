import requests

def download_file(url, filename=''):
    try:
        if filename:
            pass
        else:
            filename = req.url[downloadUrl.rfind('/')+1:]
        
        with requests.get(url) as req:
            with open(filename, 'wb') as f:
                for chunk in req.iter_content(chunk_size = 8192):
                    if chunk:
                        f.write(chunk)
            return filename
    except Exception as e:
        print(e)
        return None


downloadLink = 'https://open.spotify.com/episode/3QKDzetcvnP7rM8RozQS1W?si=2bc63abef9f044ec'

download_file(downloadLink, 'C:\\Users\\Morten\\Desktop\\School\\Bachelor\\filedownloader\\downloaded\\joerogie')