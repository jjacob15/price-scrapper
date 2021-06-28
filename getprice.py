import requests
import datetime
from bs4 import BeautifulSoup

URL = "https://www.royaldoultonoutlet.com.au/vera-wang-wedgwood-chime-nouveau-16-piece-cutlery-set.html"

with open("C:\\Users\\jaison.jacob\\Desktop\\spoon-price.txt", "a") as filehandle:
    try:
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        tag = soup.find(id="product_price")
    except Exception as ex:
        filehandle.write(''.join([ex, str(datetime.datetime.today().strftime("%b %d %Y %H:%M:%S"))]))

    filehandle.write('Price as of ' + str(datetime.datetime.today().strftime("%b %d %Y %H:%M:%S")) + ' is $' + tag.string +'\n')

