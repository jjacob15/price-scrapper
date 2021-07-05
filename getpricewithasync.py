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
            raise Exception(
                "Unable to find price from the url. Please check the Url. " + str(ex))

    def findbyclass(self, className):
        try:
            result = self._driver.find_element_by_class_name(className)
            return result.text
        except Exception as ex:
            raise Exception(
                "Unable to find price from the url. Please check the Url. " + str(ex))


if __name__ == "__main__":
    path = "C:\\Users\\jaison.jacob\\Desktop\\scrapped-price.txt"

    bbqUrl = "https://www.appliancesonline.com.au/product/beefeater-bb722aa-bigg-bugg-amber-mobile-bbq"
    B = HtmlSearch(bbqUrl)
    bbqprice = B.findbyclass("aol-product-price")

    spoonUrl = "https://www.royaldoultonoutlet.com.au/vera-wang-wedgwood-chime-nouveau-16-piece-cutlery-set.html"
    H = HtmlSearch(spoonUrl)
    spoonprice = H.findbyid("product_price")

    try:
        with open(path, "a") as filehandle:
            filehandle.write('Price of spoons on ' + str(datetime.datetime.today().strftime(
                "%b %d %Y %H:%M:%S")) + ' is ' + spoonprice + '\n')
            filehandle.write('Price of bbq on ' + str(datetime.datetime.today().strftime(
                "%b %d %Y %H:%M:%S")) + ' is ' + bbqprice + '\n')
    except Exception as ex:
        raise Exception("Unable to write the result on file. " + str(ex))    

