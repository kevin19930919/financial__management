import sys
sys.path.append("../core")
from docker import *
import pytest
CONTAINERNAME = "cakeresume-container"
IMAGEREPO = "cakeresume_craw"
IMAGETAG = "v3"
TARGETPATH="/home/cakeresume"
KEYWORD="backend"
BASESALARY="1000000"
TECHS = ["Python", "Go"]
ITEMNUMBER="10"
class TestCakeresume():
    start_container = run_container(CONTAINERNAME, IMAGEREPO, IMAGETAG)
    assert start_container == True 
    
    if start_container:
        docker_handler = DockerContainer(CONTAINERNAME)

    def test_copy_file(self):
        #copy cakeresume module in container
        copy_result = self.docker_handler.copy_file_in_container(target_path=TARGETPATH, file_path="../core/cakeresume_crawler.py")
        assert copy_result == True

    def test_exec_command_in_container(self):
        techs = ""
        for tech in TECHS:
            techs += tech+" "
        command=f'cd /home/cakeresume;python3 cakeresume_crawler.py --keyword={KEYWORD} --base-salary={BASESALARY} --techs {techs} --item-number={ITEMNUMBER};bash'
        self.docker_handler.exec_command_in_container(command)

    def test_stop_container(self):
        stop_reuslt = self.docker_handler.stop_container()
        assert stop_reuslt == True  
    
    def test_api(self):
        json_compatible_filter = jsonable_encoder(self.filters)
        req = requests.post("http://0.0.0.0:1219/cakeresume/jobs", json_compatible_filter)
        assert req.status_code == req.ok
        



