import requests
from bs4 import BeautifulSoup

def search_incruit(keyword, pages):

    jobs= []
    for i in range(pages):
        page = i * 30

        
        url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}&startno={page}"
        print(url)

        response = requests.get(url)

        soup = BeautifulSoup(response.text, "html.parser")
        lis = soup.find_all("li", class_ = "c_col")




        for li in lis:
            company = li.find("a", class_= "cpname").text.strip()
            title = li.find("div", class_="cell_mid").find("div", class_="cl_top").find("a").text.strip()
            location = li.find("div", class_="cl_md").find_all("span")[0].text.strip()
            link = li.find("div", class_="cell_mid").find("div", class_="cl_top").find("a")["href"]
        
            job_data = {
            "company" : company,
            "title" : title,
            "location": location,
                "link" : link
            }

            jobs.append(job_data)
            
    return jobs

keyword = "파이썬"
url = f"https://www.jobkorea.co.kr/Search?stext=%ED%8C%8C%EC%9D%B4%EC%8D%AC&tabType=recruit&Page_No=1"
ur2 = f"https://www.saramin.co.kr/zf_user/search?search_area=main&search_done=y&search_optional_item=n&searchType=search&searchword={keyword}"

response = requests.get(url)
print(response.text)
