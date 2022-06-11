from typing import List, Optional
from fastapi import Depends, FastAPI, HTTPException, APIRouter
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import sys
sys.path.append('../core/')
from core.cakeresume_crawler import *
from core.mail import *
from core.elasticsearch_interface import *
from celery_interface import send_craw_report
import yaml
with open(r'./fastapi/config/config.yaml', 'r') as file:
    config = yaml.full_load(file)

CakeresumeRouter = APIRouter(prefix="/cakeresume",tags=["cakeresume"])

@CakeresumeRouter.post("/jobs")
def create_CryptoTrade(Filter: Filter):
    try:
        cakeresume_crawler = CakeresumeCrawler(filters=Filter)
        result = cakeresume_crawler.craw_page()
        es = ElasticsearchHandler()
        for receiver in config["cakeresume_receivers"]:
            send_result = send_craw_report.delay(receiver=receiver, subject=f"cakeresume craw result:{Filter.query}", content=result)
        return JSONResponse(content=result)
    except Exception as e:
        print('=======create crypto record fail=========:',e)
        raise HTTPException(status_code = 500, detail =  "server error")