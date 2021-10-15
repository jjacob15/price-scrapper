from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime


class HtmlSearch():
    def __init__(self, url):
        self._driver = webdriver.PhantomJS(executable_path="C:\\phantomjs\\bin\\phantomjs.exe", service_args=[
                                           '--ignore-ssl-errors=true', '--ssl-protocol=any'])
        self._driver.get(url)

    def findbyid(self, tagId):
        try:
            print('tagid - start', tagId)
            result = self._driver.find_element_by_id(id_=tagId)
            print('tagid - end')
            return result.text
        except Exception as ex:
            print('tagid - failed')
            return "No price avaiable"

    def byXPath(self, path):
         self._driver.maximize_window()
         print('className - wait complete')
         try:
            result = self._driver.find_element_by_xpath(path)
            print('className - end', result)

            return result.get_attribute("innerText")
         except Exception as ex:
            print(repr(ex))
            print('className - failed')
            return "No price avaiable"

    def findbyclass(self, className):
        print('className - start and wait', className)
        self._driver.maximize_window()
        # wait = WebDriverWait(self._driver, 30)
        # age = wait.until(EC.visibility_of_element_located(
        #     (By.CSS_SELECTOR, "."+className)))
        # age.click()
        print('className - wait complete', className)
        try:
            result = self._driver.find_element_by_xpath("//span[@itemprop='price']")
            # result = self._driver.find_element_by_css_selector("."+className)
            # result = self._driver.find_element_by_css_selector(
            #     "span."+className+"")
            # result = self._driver.find_element_by_css_selector(
            #     "span[itemprop=""price""]")
            print('className - end', className)
            return result.text
        except Exception as ex:
            print(repr(ex))
            print('className - failed')
            return "No price avaiable"


if __name__ == "__main__":
    path = "C:\\Users\\jaison.jacob\\Desktop\\scrapped-price.txt"

    priceList = {}

    bUrl = "https://www.appliancesonline.com.au/product/weber-family-q3100-lpg-56010124"
    H = HtmlSearch(bUrl)
    bprice = H.byXPath("//aol-product-price-details//span[@itemprop='price']")
    priceList["familyq"] = bprice

    # wUrl = "https://www.amazon.com.au/Philips-Beardtrimmer-Beard-Stubble-Trimmer/dp/B0869J4GDH?ref_=Oct_d_obs_d_5150110051&pd_rd_w=WKkLO&pf_rd_p=8eed5a14-3936-4564-ad12-3afe044c0093&pf_rd_r=0AHC462G7G6W80T296YN&pd_rd_r=593a789b-39ce-4fc9-bb6a-d305e306f0c3&pd_rd_wg=QCes0&pd_rd_i=B0869J4GDH"
    wUrl = "https://www.amazon.com.au/Fashioned-Whiskey-Glasses-4-Heavy-Elegant/dp/B00NCO9MLY/"
    W = HtmlSearch(wUrl)
    wprice = W.byXPath("//div[@id='apex_offerDisplay_desktop']/*/*/*/*")
    priceList["whiskey-glass"] = wprice

    try:
        with open(path, "a") as filehandle:
            for key, value in priceList.items():
                filehandle.write('Price of ' + key + ' on ' + str(datetime.datetime.today().strftime(
                    "%b %d %Y %H:%M:%S")) + ' is ' + value + '\n')
    except Exception as ex:
        raise Exception("Unable to write the result on file. " + str(ex))

    print('Scrapping complete')
