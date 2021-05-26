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
        #Get request for searching
        response = requests.get(pageUrl, headers=self.header) 
        #Response success control
        if response.status_code == 200: 
            #Response html parsed
            parsed = parser.document_fromstring(response.text) 
            #Find all results of searching
            items = parsed.find_class("catalog-seem-cell")
            if len(items) > 0:
                idx = 0
                #Get first 3 search result
                while len(products) < 3 and idx < len(items):
                    #get the product link
                    a = items[idx].cssselect("a")
                    products["g{0}".format(idx)] = {"url" : items[idx].cssselect("a")[0].attrib["href"]}
                    idx += 1
                #Visiting all product and getting other information
                for id, product in products.items():
                    #Get request for product single page
                    response = requests.get(product["url"], headers=self.header) 
                    if response.status_code == 200:
                        parsed = parser.document_fromstring(response.text)
                        #Get name text
                        product["name"] = parsed.cssselect("#sp-title")[0].text 
                        #Get price text and some preprocess
                        price = parsed.cssselect(".lastPrice")[0].text.replace("\n","").replace(" ","").replace("TL","").replace(".","").replace(",",".") 
                        product["price"] = float(price)
                        #Create list for comments
                        product["comments"] = list()
                        #Create comments page url
                        commentLink = product["url"].split("_spp")[0]+self.commentAdd
                        #Get request for product comments
                        response = requests.get(commentLink, headers=self.header)
                        if response.status_code == 200:
                            parsed = parser.document_fromstring(response.text)
                            #Get all comment items and add to list
                            comments = parsed.cssselect(".user-catalog-review-comment-detail>p")
                            for comment in comments:
                                product["comments"].append(comment.text_content())

        return products