import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
'''print(soup.title.get_text)
print(soup.a)
print(soup.a.attrs)
print(soup.a["href"])'''

#print(soup.find("li", attrs={"class":"rank01"}))

#rank1 = soup.find("li", attrs={"class":"rank01"})
#print(rank1.parent)

#rank2 = rank1.find_next_sibling("li")
#print(rank2.a.get_text())'''

#print(rank1.find_next_sibling("li"))

webtoon = soup.find("a", text="독립일기-11화 밥공기 딜레마")
print(webtoon)