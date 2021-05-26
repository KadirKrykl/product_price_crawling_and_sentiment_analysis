import requests
import lxml.html as parser
import lxml.cssselect
import time



class pcHepsiBurada:
    root = "https://www.hepsiburada.com"
    searchUrl = "https://www.hepsiburada.com/ara?q="
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
    commentAdd = "-yorumlari?sayfa=1"
    def __init__(self):
        ...

    def keyPreProcess(self,key):
        return key.replace(" ","+")

    def getProducts(self,key):
        products = dict()
        key = self.keyPreProcess(key)
        pageUrl = self.searchUrl + key
        response = requests.get(pageUrl, headers=self.header)
        if response.status_code == 200:
            parsed = parser.document_fromstring(response.text)
            items = parsed.find_class("search-item")
            if len(items) > 0:
                idx = 0
                while len(products) < 3 and idx < len(items):
                    rate = items[idx].find_class("ratings active")
                    if len(rate) > 0:
                        a = items[idx].cssselect("a")
                        products["h{0}".format(idx)] = {"url" : self.root + items[idx].cssselect("a")[0].attrib["href"]}
                    idx += 1
                for id, product in products.items():
                    response = requests.get(product["url"], headers=self.header)
                    if response.status_code == 200:
                        parsed = parser.document_fromstring(response.text)
                        n = parsed.cssselect("#product-name")[0]
                        product["name"] = parsed.cssselect("#product-name")[0].text.replace("\r\n","").replace("  "," ")
                        product["price"] = float(parsed.cssselect("#offering-price")[0].attrib["content"])
                        product["comments"] = list()
                        response = requests.get(product["url"]+self.commentAdd, headers=self.header)
                        if response.status_code == 200:
                            parsed = parser.document_fromstring(response.text)
                            comments = parsed.cssselect("span[itemprop='description']")
                            for comment in comments:
                                product["comments"].append(comment.text)
        
        return products