from selenium import webdriver
import datetime

class HtmlSearch():
    def __init__(self, url):
        self._driver = webdriver.PhantomJS(executable_path="C:\\phantomjs\\bin\\phantomjs")
        self._driver.get(url)

    def findbyid(self, tagId):
        try:
            result = self._driver.find_element_by_id(id_=tagId)
            return result.text
        except Exception as ex:
            return "No price avaiable"

    def findbyclass(self, className):
        try:
            result = self._driver.find_element_by_class_name(className)
            return result.text
        except Exception as ex:
            return "No price avaiable"


if __name__ == "__main__":
    path = "C:\\Users\\jaison.jacob\\Desktop\\scrapped-price.txt"

    bear = "https://www.amazon.com.au/Very-Cranky-Bear-Book-Boxed/dp/1760971316/ref=sr_1_1?crid=K1Y5CYT162Z1&dchild=1&keywords=the+very+cranky+bear&qid=1626051214&sprefix=the+very+cran%2Caps%2C403&sr=8-1"
    B = HtmlSearch(bear)
    bbqprice = B.findbyid("price")

    spoonUrl = "https://www.royaldoultonoutlet.com.au/vera-wang-wedgwood-chime-nouveau-16-piece-cutlery-set.html"
    H = HtmlSearch(spoonUrl)
    spoonprice = H.findbyid("product_price")

    try:
        with open(path, "a") as filehandle:
            filehandle.write('Price of spoons on ' + str(datetime.datetime.today().strftime(
                "%b %d %Y %H:%M:%S")) + ' is ' + spoonprice + '\n')
            filehandle.write('Price of bear on ' + str(datetime.datetime.today().strftime(
                "%b %d %Y %H:%M:%S")) + ' is ' + bbqprice + '\n')
    except Exception as ex:
        raise Exception("Unable to write the result on file. " + str(ex))    

