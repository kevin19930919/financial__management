from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.action_chains import ActionChains

from dataclasses import dataclass
from typing import List

import argparse

@dataclass
class Filter:
    query: str
    base_salary: int
    tech_label: List[str]
    item_number: int


class CakeresumeCrawler():
    base_url = "https://www.cakeresume.com/jobs"
    def __init__(self, filters):
        self.job_filters = filters
    
    def construct_query_url(self):
        self.base_url += f"?q={self.job_filters.query}"
        self.base_url += f"&refinementList%5Bsalary_type%5D=per_year&refinementList%5Bsalary_currency%5D=TWD"
        for index, label in enumerate(self.job_filters.tech_label):
            self.base_url += f"&refinementList%5Bpage.tech_labels%5D%5B{index}%5D={label}"
        self.base_url += f"&range%5Bsalary_range%5D%5Bmin%5D={self.job_filters.base_salary}"
        return self.base_url    

    def craw_page(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-notifications")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--headless')
        driver = webdriver.Chrome('./chromedriver', chrome_options=options)
        # print(self.construct_query_url())
        driver.get(self.construct_query_url())
        # driver.implicitly_wait(20)
        title_list = self.scrap_title(driver)
        salary_list = self.scrap_salary(driver)
        result = self.concate_result(title_list, salary_list)
        driver.quit()
        return result

    def scrap_title(self, driver):
        title_list = []
        for i in range(1, self.job_filters.item_number+1):
            title_xpath = f'//*[@id="root"]/div/div[2]/div/div/div[1]/div[7]/div/div[{i}]/div[1]/div[1]/h2/div/a'
            title = driver.find_element_by_xpath(title_xpath).text
            title_list.append(title)
        return title_list  

    def scrap_salary(self, driver):
        salary_list = []
        for i in range(1, self.job_filters.item_number+1):
            salary_xpath = f'//*[@id="root"]/div/div[2]/div/div/div[1]/div[7]/div/div[{i}]/div[1]/div[2]/div[1]/div[2]/span'
            salary = driver.find_element_by_xpath(salary_xpath).text
            salary_list.append(salary)
        return salary_list

    def concate_result(self, titles, salarys):
        results =  {}
        for index in range(len(titles)):
            results[titles[index]] == salarys[index]

        return results

         

