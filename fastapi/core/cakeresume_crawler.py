from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from dataclasses import dataclass
from typing import List
@dataclass
class Filter:
    query: str
    base_salary: int
    tech_label: List[str]


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
        driver.get(construct_query_url)
        # driver.set_window_size(800,600)
        # print(f"======== render done ======")
        button = driver.find_element_by_id('Animal')
        desired_y = (button.size['height'] / 2) + button.location['y']
        print("======== target position:",button.size['height'],button.location['y'])
        # current_y = (driver.execute_script('return window.innerHeight') / 2) + driver.execute_script('return window.pageYOffset')
        print("======= current_y:",driver.execute_script('return window.pageYOffset'))
        # scroll_y_by = desired_y - current_y
        # print("======scroll_y_by:",scroll_y_by)
        driver.execute_script("window.scrollTo(0,1310);")
        time.sleep(3)
        print("======= current_y2:",driver.execute_script('return window.pageYOffset'))

        ActionChains(driver).move_to_element_with_offset(button,5,5).click(button).perform()

        time = 0
        while True: 
            try:
                driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/table/tr[1]/td[5]/button').click()
                print("press success count",time)
                time += 1
            except Exception as e:
                print(e)    

        dirver.quit()