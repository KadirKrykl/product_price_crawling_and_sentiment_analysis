from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time



class pcGittiGidiyor:
    driver = ""
    def __init__(self,driver):
        self.driver = driver

    def getProducts(self,key):
        products = dict()
        try:
            self.driver.get("https://www.gittigidiyor.com/")
            search = self.driver.find_element_by_name("k")
            search.send_keys(key)
            self.driver.find_element_by_xpath("//*[@id='main-header']/div[3]/div/div/div/div[2]/form/div/div[2]/button/span").click()

            element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "catalog-seem-cell"))
                )
            idx = 0
            productList = self.driver.find_elements_by_class_name("catalog-seem-cell")
            while len(products) < 3 and idx < len(productList):
                try:
                    item = productList[idx].find_element_by_class_name("catalog-review-title")
                    products["g{0}".format(idx)] = {"link":productList[idx].find_element_by_tag_name("a").get_attribute('href')}
                except:
                    ...
                finally:
                    idx += 1
            
            for id, product in products.items():
                self.driver.get(product["link"])
                product["name"] = self.driver.find_element_by_css_selector("#sp-title").text
                product["price"] = int(self.driver.find_element_by_css_selector(".lastPrice").text.split(",")[0].replace(".",""))
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                self.driver.find_element_by_css_selector(".see-all-catalog-review").click()
                element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "user-catalog-review"))
                )
                comments = self.driver.find_elements_by_css_selector(".user-catalog-review-comment-detail > p")
                tempList = list()
                for comment in comments:
                    tempList.append(comment.text)
                    print(comment.text)
                product["comments"] = tempList
                
        except:
            ...
        
        return products