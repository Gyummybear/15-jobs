import requests
from bs4 import BeautifulSoup

keyword="파이썬"
url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}&startno=0"
response = requests.get(url)
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")

lis = soup.find_all("li", class_ = "c_col")

# print(len(lis))
# print(lis[0])

for li in lis:
    # company = li.find("a", class_= "cpname").text.strip()
    # title = li.find("div, class_="cell_mid").find("div", class_= "cl_top").find("a").text.strip()

    # location = li.find("div",class_='cl_md).find_all("span")[0].text.strip()')
    # print(location)

    l