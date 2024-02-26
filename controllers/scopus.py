from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import time

def scopus():
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    service = Service('./chromedriver')
    driver = webdriver.Chrome(service=service, options=option)

    sintaLink = "https://sinta.kemdikbud.go.id/authors/profile/5973952"
    driver.get(sintaLink)

    content = driver.page_source
    driver.quit()

    data = BeautifulSoup(content, 'html.parser')

    result_list = []
    for area in data.find_all('div', class_='ar-list-item mb-5'):
        title = area.find('div', class_='ar-title').get_text()
        publication = area.find('a', class_='ar-pub').get_text()
        year = area.find('a', class_='ar-year').get_text()
        cited = area.find('a', class_='ar-cited').get_text()

        result_temp = {
            'title': title,
            'publication': publication,
            'year': year,
            'cited': cited,
            'tipe': 'SCOPUS'
        }
        result_list.append(result_temp)

    return result_list


