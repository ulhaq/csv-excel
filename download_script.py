import sys
from webget import download

for arg in sys.argv[1:]:
    args = arg.split()
    url = args[0]
    location = None
    
    if len(args) > 1:
        location = args[1]
    
    download(url, location)
