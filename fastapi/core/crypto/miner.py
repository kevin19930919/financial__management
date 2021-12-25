from ctypes import *

# ==== initial miner handler(golang) ====
go_module = cdll.LoadLibrary("./golang/miner.so")

class go_string(Structure):
    _fields_ = [
        ("p", c_wchar_p)
    ]

def showDockerNodeList(containerID):
    CID = go_string(c_wchar_p(containerID))
    stdout, stderr = go_module.ShowSwarmNodeInfo(CID)
    if stderr:
        print('something wrong', stderr)
    else:
        print('success', stdout)


# def callGOReturnVal():
#     result = go_module.ReturnDockerImagesNum()
#     print(f"go return result:{result}")


if __name__=='__main__':

    showDockerNodeList('w2mrwgxy5btyta8xm5qgl8equ')

    # callGOReturnVal()  
