import re
import requests
from bs4 import BeautifulSoup

# Get jobs from stackoverflow.com

def get_job(keyword):
    # Request a page to stackoverflow.com/jobs
    baseURL = "https://stackoverflow.com"
    URL_with_keyword=f"https://stackoverflow.com/jobs?q={keyword}"
    
    # Get the total page number
    page = requests.get(URL_with_keyword)
    soup = BeautifulSoup(page.text, 'html.parser')
    total_page = int(soup.find('div', class_='s-pagination').find_all('a')[-2].get_text())
    
    if total_page == None:
        total_page = 1

    # Cut down the page number to 7
    if total_page > 7:
        total_page = 7

    job_list = []
    # Scrape the job information in every page
    for pagenumber in range(1, total_page+1):
        URL_with_keyword_and_page = f"https://stackoverflow.com/jobs?q={keyword}&pg={pagenumber}"
        page = requests.get(URL_with_keyword_and_page)
        soup = BeautifulSoup(page.content, 'html.parser')
        job_list_from_page = soup.find("div", {"class": "listResults"}).find_all("div", {"class": re.compile('^-job js-result')})
        job_list.extend(job_list_from_page)

    # Get the job data into a list of dictionaries.
    jobs = []
    for job in job_list:
        dict = {}

        # Get the tags that I need to retrieve data from
        a = job.find("a", {"class": "s-link"})
        h3 = job.find("h3", {"class": re.compile('^fc-black-700')})
        ul = job.find("ul", {"class": re.compile('^fs-caption')})
        a_logo = job.find("img", {"class": "s-avatar--image"})

        # Get the data from the tags
        title = a['title']
        link = baseURL + a['href']
        company = h3.span.text.strip()
        location = h3.find("span", {"class": "fc-black-500"}).text.strip()
        post_date = ul.span.text.strip()
        if a_logo is None:
            logo = "https://www.clipartmax.com/png/full/33-330391_briefcase-work-job-work-icon-ico.png"
        else: 
            logo = a_logo['src']

        # Add the data to the dictionary
        dict['title'] = title
        dict['link'] = link
        dict['company'] = company
        dict['location'] = location
        dict['post_date'] = post_date
        dict['logo'] = logo

        # Add the dictionary to the list
        jobs.append(dict)

    return jobs

get_job("python")