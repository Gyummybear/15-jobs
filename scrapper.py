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

def search_saramin(keyword, pages):
    jobs = []
    # 사람인은 차단 방지를 위해 headers가 꼭 필요합니다. (살짝 추가)
    headers = {"User-Agent": "Mozilla/5.0"}

    for i in range(pages):
        # 인크루트는 i * 30이었지만, 사람인은 그냥 페이지 번호를 씁니다.
        url = f"https://www.saramin.co.kr/zf_user/search/recruit?searchword={keyword}&recruitPage={i+1}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        # [변경포인트 1] li.c_col 대신 div.item_recruit를 찾습니다.
        lis = soup.find_all("div", class_="item_recruit")

        for li in lis:
            # [변경포인트 2] 클래스 이름을 사람인에 맞게 수정합니다.
            # 인크루트: cpname -> 사람인: corp_name
            company = li.find("div", class_="corp_name").find("a").text.strip()
            
            # 인크루트: cl_top -> 사람인: job_tit
            title_tag = li.find("div", class_="job_tit").find("a")
            title = title_tag.text.strip()
            
            # 인크루트: 0번째 span -> 사람인: 0번째 span (동일)
            location = li.find("div", class_="job_condition").find_all("span")[0].text.strip()
            
            # 링크도 태그 안에서 가져오기 (도메인 추가)
            link = "https://www.saramin.co.kr" + title_tag["href"]
        
            job_data = {
                "company" : company,
                "title" : title,
                "location": location,
                "link" : link
            }
            jobs.append(job_data)
            
    return jobs