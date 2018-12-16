from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup

# Insert your URL to extract


url_name = "https://www.google.com"
url = urlopen(url_name)

bsObj = BeautifulSoup(url.read(), 'lxml')
print(requests.get(url_name))

# fetching the unique urls
url_dict = {link.text: link.get('href') for link in bsObj.find_all('a') if link.get('href') != '#' if
            link.get('href') is not None}
image_dict = {link.text: link.get('src') for link in bsObj.find_all(
    'img') if 'php' not in link.get('src')}

pdf_dict = {link.text: link.get('href') for link in bsObj.find_all('a') if link.get('href') is not None if
            'pdf' in link.get('href')}

mp3_formats = ['WMA', 'AIFF', 'FLAC', 'ALAC']

mp3_dict = {link.text: link.get('href') for link in bsObj.find_all('a') if link.get('href') is not None for i in
            mp3_formats if i in link.get('href')}

print('-'*50, 'PDF LIST', '-'*50)
print('\n'.join(pdf_dict))
print('-'*50, 'URL LIST', '-'*50)
print('\n'.join(url_dict))
print('-'*50, 'MP3 LIST', '-'*50)
print('\n'.join(mp3_dict))
