from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

def penelitian():
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    service = Service('./chromedriver')
    driver = webdriver.Chrome(service=service, options=option)

    sinta_link = "https://sinta.kemdikbud.go.id/authors/profile/5973952/?view=researches"

    driver.get(sinta_link)

    content = driver.page_source
    driver.quit()

    data = BeautifulSoup(content, 'html.parser')

    result_list = []

    for area in data.find_all('div', class_='ar-list-item mb-5'):
        title = area.find('div', class_='ar-title').get_text()
        publication = area.find('a', class_='ar-pub').get_text()
        year = area.find('a', class_='ar-year').get_text()


        result_dict = {
            'Title': title,
            'Publication': publication,
            'Year': year,
            'Tipe': 'PENELITIAN'
        }

        result_list.append(result_dict)

    return result_list