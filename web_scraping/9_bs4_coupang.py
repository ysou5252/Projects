import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=2&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")


items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
#print(items[0].find("div", attrs={"class":"name"}).get_text())
for item in items:
    name = items[0].find("div", attrs={"class":"name"}).get_text()
    price = item.find("strong", attrs={"class":"price-value"}).get_text()
    rate = item.find("em", attrs={"class":"rating"}).get_text()
    rate_cnt = item.find("span", attrs={"class":"rating-total-count"}).get_text()
    if rate:
        rate = rate.get_text()
    else:
        rate = "평점 없음"

    rate_cnt = item.find("span", attrs={"class":"rating-total-count"})