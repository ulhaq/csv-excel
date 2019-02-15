import os
import urllib.error
import urllib.request

def download(url, location=None):
    location = os.path.basename(url) if location==None else location

    if os.path.isfile(location):
        return print("File already exists.")

    try:
        print('Downloading', location)

        urllib.request.urlretrieve(url, location)

        print('Download Completed')
    except urllib.error.HTTPError as e:
        print(e.code)
    except urllib.error.URLError as e:
        print(e.args)

    return
