import sys
from webget import download

for url in sys.argv[1:]:
    download(url)
