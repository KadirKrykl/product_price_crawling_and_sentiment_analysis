from sentimentAnalysis import SentimentAnalysis
from pcHepsiBurada import pcHepsiBurada
from pcGittiGidiyor import pcGittiGidiyor
import pprint



sentA = SentimentAnalysis()
driver_path = "chromedriver.exe"




search = input("What are you looking for? \n")

products = dict()
# {
#     productId:{
#         price: int,
#         comments: [list],
#         url: str
#     }
# }

## Hepsiburada
hepsiburada = pcHepsiBurada()
products.update(hepsiburada.getProducts(search))

## Gittigidiyor
gittigidiyor = pcGittiGidiyor()
products.update(gittigidiyor.getProducts(search))

#Transform comments to ratings with sentiment analysis
for id,product in products.items():
    product["rating"] = sentA.analysis(product["comments"])
    del product["comments"]

#Sorting with price and rating
products = sorted(products.items(), key = lambda x: (x[1]['price'], x[1]['rating']))

pprint.pprint(products)

