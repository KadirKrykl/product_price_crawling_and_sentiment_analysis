from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sentimentAnalysis import SentimentAnalysis
from pcHepsiBurada import pcHepsiBurada
from pcGittiGidiyor import pcGittiGidiyor


sentA = SentimentAnalysis()
driver_path = "chromedriver.exe"




search = "lenova laptop"

products = dict()
# {
#     productId:{
#         price: int,
#         comments: [list],
#         url: str
#     }
# }

# without windows setting 
op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(executable_path=driver_path,options=op)

# with windows
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.maximize_window()

## Hepsiburada
# hepsiburada = pcHepsiBurada(driver)
# products.update(hepsiburada.getProducts(search))

## Gittigidiyor
gittigidiyor = pcGittiGidiyor(driver)
products.update(gittigidiyor.getProducts(search))

for id,product in products.items():
    product["rating"] = sentA.analysis(product["comments"])
    del product["comments"]

sorted(products, key=lambda x: (products[x]['price'], products[x]['rating']))

print(products)
driver.quit()

