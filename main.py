import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import os


def img_crawler(max_page):
    page = 1
    while page <= max_page:
        path = os.path.join(r'C:\Users\Suyog\PycharmProjects\Learning\Kingdom', str(page))
        if not os.path.exists(path):
            os.makedirs(path)
            url = 'http://mangakakalot.com/chapter/kingdom/chapter_' + str(page)
            source_code = requests.get(url)
            plain_text = source_code.text
            soup = BeautifulSoup(plain_text, "html.parser")
            f = open('output.txt', 'w')
            for link in soup.findAll('img'):
                f.write(link.get('src')+' ')
            f.close()
            fr = open('output.txt', 'r')
            b = fr.read()
            text_url = b.split(' ')
            for line in text_url:
                if line is '':
                    break
                else:
                    r = requests.get(line)
                    i = Image.open(BytesIO(r.content))
                    z = line.split('/')[-1]
                    i.save(path + '\\' + z)
            fr.close()
            os.remove('output.txt')

        else:
            pass
        page += 1

img_crawler(11)

