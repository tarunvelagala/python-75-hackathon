from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

my_url = "http://www.sathyabama.ac.in/index.php"
uClient = ureq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
# variety = page_soup.findAll("html",{"class" : " js no-touch cssanimations csstransitions"})
links = page_soup.findAll('a', href=True)

for link in links:
    print(link["href"])

images = page_soup.findAll('img', src=True)
for image in images:
    print(image["src"])
