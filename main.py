from sentimentAnalysis import SentimentAnalysis
from pcHepsiBurada import pcHepsiBurada
from pcGittiGidiyor import pcGittiGidiyor


sentA = SentimentAnalysis()
driver_path = "chromedriver.exe"




search = "lenovo laptop"

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

for id,product in products.items():
    product["rating"] = sentA.analysis(product["comments"])
    del product["comments"]

products = sorted(products.items(), key = lambda x: (x[1]['price'], x[1]['rating']), reverse=True)

print(products)

