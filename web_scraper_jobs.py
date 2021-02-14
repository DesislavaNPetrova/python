### 
    HTML Elements: A single job posting lives inside of a div element with the class name result. Inside there are other elements. You can find the specific info you're looking for here:

Link: In the href attribute of the <a> Element that is a child of the title <h2> element
Title: The text of the link in the <h2> element which also contains the link URL mentioned above
Location: A <span> element with the telling class name location
Company: A <span> element with the telling class name company

resource realpython.com
###

pip install requests
pip3 install beautifulsoup4


import requests
from bs4 import BeautifulSoup

def get_jobs(title, location, page=1):
    loc = location.replace(' ', '+')  # for multi-part locations
    base_url_indeed = f'https://www.indeed.com/jobs?q={title}&l={loc}&start='
    results_start_num = page*10
    url = f'{base_url_indeed}{results_start_num}'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    page = requests.get(url, headers=headers)
    return page


def parse(soup):
    results = soup.find(id='resultsCol')
    jobs = results.find_all('div', class_='result')
    base_url = 'https://www.indeed.com'

    job_list = list()
    for job in jobs:
        title = job.find('h2').find('a').text.strip()
        link = base_url + job.find('h2').find('a')['href']
        location = job.find(class_='location').text
        company = job.find(class_='company').text.strip()
        job_list.append({'title': title, 'link': link, 'location': location, 'company': company})

    return job_list    


def get_the_dream_job(title, location, amount=100):
    results = list()
    for page in range(amount//10):
        site = get_jobs(title, location, page=page)
        soup = BeautifulSoup(site.content)
        page_results = parse(soup)
        results += page_results
    return results



wow = get_the_dream_job('devops', 'new york', 10)
wow 






