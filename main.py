from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


##/home/salusmoon/Desktop/ws/webMining/final/product_price_crawling_and_sentiment_analysis

driver_path = "/home/salusmoon/Desktop/ws/webMining/final/product_price_crawling_and_sentiment_analysis/chromedriver"

# without windows setting 
# op = webdriver.ChromeOptions()
# op.add_argument('headless')
# driver = webdriver.Chrome(executable_path=driver_path,options=op)

# with windows
driver = webdriver.Chrome(executable_path=driver_path)

# sayfada geri gitme
# driver.back()

# print('Enter your name:')
# product = input()
product = "lenova laptop"

## Hepsiburada
driver.get("https://www.hepsiburada.com")
search = driver.find_element_by_xpath("//*[@id='SearchBoxOld']/div/div/div[1]/div[2]/input")
search.send_keys(product)
driver.find_element_by_xpath("//*[@id='SearchBoxOld']/div/div/div[2]").click()
                                        

productList = driver.find_element_by_class_name("product-list results-container do-flex list")

# product1 = driver.find_element_by_xpath("//*[@id='73bf8bea-e6aa-4ec0-a590-49246091eaba']/div/div/ul/li[2]/div/a/div[2]/h3").text
# product2 = driver.find_element_by_xpath("//*[@id='73bf8bea-e6aa-4ec0-a590-49246091eaba']/div/div/ul/li[2]/div/a/div[2]/h3").text
# product3 = driver.find_element_by_xpath("//*[@id='6f68548b-5874-4a1e-bf9f-e6b584c16368']/div/div/ul/li[3]/div/a/div[2]/h3/div/p/span").text



## gittigidiyor
driver.get("https://www.gittigidiyor.com")