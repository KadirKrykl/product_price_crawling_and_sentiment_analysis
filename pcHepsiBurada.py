from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time



class pcHepsiBurada:
    driver = ""
    def __init__(self,driver):
        self.driver = driver

    def getProducts(self,key):
        products = dict()
        try:
            self.driver.get("https://www.hepsiburada.com")
            search = self.driver.find_element_by_xpath("//*[@id='SearchBoxOld']/div/div/div[1]/div[2]/input")
            search.send_keys(key)
            self.driver.find_element_by_xpath("//*[@id='SearchBoxOld']/div/div/div[2]").click()

            element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "search-item"))
                )
            idx = 0
            productList = self.driver.find_elements_by_class_name("search-item")
            while len(products) < 3 and idx < len(productList):
                try:
                    item = productList[idx].find_element_by_class_name("ratings")
                    products["h{0}".format(idx)] = {"link":productList[idx].find_element_by_tag_name("a").get_attribute('href')}
                except:
                    ...
                finally:
                    idx += 1
            
            for id, product in products.items():
                self.driver.get(product["link"])
                product["name"] = self.driver.find_element_by_css_selector("#product-name").text
                product["price"] = int(self.driver.find_element_by_css_selector("#offering-price > span:nth-child(1)").text.replace(".",""))
                target = self.driver.find_element_by_css_selector("#productReviewsTab")
                target.click()
                a = ActionChains(self.driver)
                a.move_to_element(target).perform()
                self.driver.execute_script("window.scrollTo(0, {0});".format(target.location['y']))
                comments = self.driver.find_elements_by_css_selector("span[itemprop='description']")
                tempList = list()
                for comment in comments:
                    tempList.append(comment.text)
                    print(comment.text)
                product["comments"] = tempList
                
        except:
            ...
        
        return products