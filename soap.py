from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://www.eurogamer.net/"
name = url.split('.')

try:
    with open(f"{name[1]}.txt", "w") as f:
        page = urlopen(url)
        html_bytes = page.read()
        html = html_bytes.decode('utf-8')
        f.write(html)    

except:
    print("something went wrong.")
    
