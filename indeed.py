import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"


def extract_last_pages():

    # url의 html소스 객체생성
    result = requests.get(URL);

    # html소스로부터 parser객체 생성
    soup = BeautifulSoup(result.text, 'html.parser')

    # <div class="pagination"></div> 가져오기
    # class는 파이썬에서 예약어로 쓰이므로 class_로 쓴다.
    pagination = soup.find("div", class_="pagination")
    # print(pagination)

    # 페이지네이션 안에 모든 a태그 가져옴
    links = pagination.find_all('a')
    # print(pages)
    pages = []

    # 모든 a태그안에서 각각의 span태그 가져옴
    for link in links[:-1]:
        pages.append(int(link.find('span').string))

    # 마지막 페이지를 가져온거임
    max_page = pages[-1]
    return max_page


def extract_job(html):
    title = html.find('div', class_='title').find('a')['title']

    company = html.find('span', class_='company')  # 이게 없는게 있다고..??

    # print(html)
    # print(company)
    if company is not None:
        company_anchor = company.find('a')
        if company_anchor is not None:
            company = str(company_anchor.string)
        else:
            company = str(company.string)
    else:
        company = 'empty'

    company = company.strip()  # 공백없앰
    location = html.find('div', class_='recJobLoc')['data-rc-loc']
    return {'title':title, 'company':company, 'location':location}


def extract_jobs(last_page):

    jobs = []
    for page in range(last_page):
        print(f"Scrapping page {page}---- {URL}&start={page*LIMIT}")
        result = requests.get(f"{URL}&start={page*LIMIT}")
        # result = requests.get(f"{URL}&start={0 * LIMIT}")
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all('div', class_="jobsearch-SerpJobCard")
        for result in results:
            jobs.append(extract_job(result))

    return jobs

def get_jobs():
    # 마지막 페이지 구한거
    last_page = extract_last_pages()
    print("lasg page : ", last_page)

    # 매 페이지의 직업정보 를 가져옴
    jobs = extract_jobs(1)

    return jobs