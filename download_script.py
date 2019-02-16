import sys
from webget import download

for arg in sys.argv[1:]:
    args = arg.split()
    url = args[0]
    
    if len(args) == 2:
        location = args[1]
    else:
        location = None
    
    download(url, location)
