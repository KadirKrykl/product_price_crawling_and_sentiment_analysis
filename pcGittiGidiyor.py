import requests
import lxml.html as parser
import lxml.cssselect
import time



class pcGittiGidiyor:
    root = "https://www.gittigidiyor.com"
    searchUrl = "https://www.gittigidiyor.com/arama/?k="
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
    commentAdd = "/yorumlari"
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
            items = parsed.find_class("catalog-seem-cell")
            if len(items) > 0:
                idx = 0
                while len(products) < 3 and idx < len(items):
                    a = items[idx].cssselect("a")
                    products["g{0}".format(idx)] = {"url" : items[idx].cssselect("a")[0].attrib["href"]}
                    idx += 1
                for id, product in products.items():
                    response = requests.get(product["url"], headers=self.header)
                    if response.status_code == 200:
                        parsed = parser.document_fromstring(response.text)
                        product["name"] = parsed.cssselect("#sp-title")[0].text
                        price = parsed.cssselect(".lastPrice")[0].text.replace("\n","").replace(" ","").replace("TL","").replace(".","").replace(",",".")
                        product["price"] = float(price)
                        product["comments"] = list()
                        commentLink = product["url"].split("_spp")[0]+self.commentAdd
                        response = requests.get(commentLink, headers=self.header)
                        if response.status_code == 200:
                            parsed = parser.document_fromstring(response.text)
                            comments = parsed.cssselect(".user-catalog-review-comment-detail>p")
                            for comment in comments:
                                product["comments"].append(comment.text_content())

        return products