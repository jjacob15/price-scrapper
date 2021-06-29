import requests
import datetime
from bs4 import BeautifulSoup

class HtmlSearch():
    def __init__(self, url):
        self._URL = url

    def findbyid(self, tagId):
        try:
            page = requests.get(self._URL)
            soup = BeautifulSoup(page.content, 'html.parser')
            return soup.find(id=tagId)
        except Exception as ex:
            raise Exception("Unable to find price from the url. Please check the Url. " +  str(ex))

    def savetofile(self, path,tag):
        try:
            with open(path, "a") as filehandle:
                filehandle.write('Price as of ' + str(datetime.datetime.today().strftime("%b %d %Y %H:%M:%S")) + ' is $' + tag.string +'\n')
        except Exception as ex:
            raise Exception("Unable to write the result on file. " + str(ex))


if __name__== "__main__":
    URL = "https://www.royaldoultonoutlet.com.au/vera-wang-wedgwood-chime-nouveau-16-piece-cutlery-set.html"
    path = "C:\\Users\\jaison.jacob\\Desktop\\spoon-price.txt"
    H = HtmlSearch(URL)
    H.savetofile(path,H.findbyid("product_price"))

