import sys
sys.path.append("../core")
from cakeresume_crawler import *
import pytest

class TestCakeresumeCrawler():
    # initial filter
    filters = Filter(query="backend", base_salary=1000000, tech_label=["Python", "Go"], item_number=10)
    cakeresume_crawler = CakeresumeCrawler(filters=filters)

    def test_construct_query_url(self):
        result = self.cakeresume_crawler.construct_query_url()
        assert result == "https://www.cakeresume.com/jobs?q=backend&refinementList%5Bsalary_type%5D=per_year&refinementList%5Bsalary_currency%5D=TWD&refinementList%5Bpage.tech_labels%5D%5B0%5D=Python&refinementList%5Bpage.tech_labels%5D%5B1%5D=Go&range%5Bsalary_range%5D%5Bmin%5D=1000000"

    def test_craw_page(self):
        result = self.cakeresume_crawler.craw_page()
        print(result)