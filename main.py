import json

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By


class AvitoParser:

    def __init__(self, url: str, items: list, version_main=None):
        self.url = url
        self.items = items  #for searching by keywords(not ready yet)
        self.version_main = version_main #version_mane can be used if you got not last version of chrome
        self.data = []

    def __set_up(self):
        """Selenium set up with UC"""
        self.driver = uc.Chrome()

    def __get_url(self):
        """Url of the site"""
        self.driver.get(self.url)

    def __parse_page(self):
        titles = self.driver.find_elements(By.CSS_SELECTOR, "[data-marker='item']")
        for title in titles:
            name = title.find_element(By.CSS_SELECTOR, "[itemprop='name']").text.strip()
            description = title.find_element(By.CSS_SELECTOR,
                                             ".iva-item-descriptionStep-C0ty1 .styles-module-root-_KFFt").text
            url = title.find_element(By.CSS_SELECTOR, "[data-marker='item-title']").get_attribute('href')
            price = title.find_element(By.CSS_SELECTOR, "[itemprop='price']").get_attribute('content')
            data = {
                'name': name,
                'description': description,
                'url': url,
                'price': price
            }
            self.data.append(data)
        self.__save_data()

    def __paginator(self):
        """if there is a "next page" button on the page, then it will be clicked to go to the next page (there won't
        be one on the last page)"""
        while self.driver.find_elements(By.CSS_SELECTOR, '[data-marker="pagination-button/nextPage"]'):
            self.__parse_page()
            self.driver.find_element(By.CSS_SELECTOR, '[data-marker="pagination-button/nextPage"]').click()

    def __save_data(self):
        """Saving data in JSON format"""
        with open('items.json', 'w', encoding='utf-8') as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)

    def parse(self):
        self.__set_up()
        self.__get_url()
        self.__paginator()


if __name__ == '__main__':
    AvitoParser(url='https://www.avito.ru/krasnodar/kvartiry/sdam/na_dlitelnyy_srok/2-komnatnye'
                    '-ASgBAgICA0SSA8gQ8AeQUswIkFk?cd=1&f'
                    '=ASgBAgECA0SSA8gQ8AeQUswIkFkCRY4uFHsiZnJvbSI6NSwidG8iOm51bGx9xpoMFXsiZnJvbSI6MCwidG8iOjM1MDAwfQ',
                items=['iphone', ]).parse()
