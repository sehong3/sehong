import math 
import random 
from datetime import datetime as dt

def mt_sqrt(x) :
    return math.sqrt(x)

def mt_sinpi() :
    return math.sin(math.pi / 2)

def mt_elog() :
    return math.log(math.e)

def mt_exp(x) :
    return math.exp(x)

def mt_pi() :
    return math.pi

def rd_int(x, y) :
    return random.randint(x, y)

def rd_list(this) :
    return random.choice(this)

def rd_rd() :
    return random.random()

def rd_nmvar() :
    return random.normalvariate(0, 1)

"""res = rd.randint(1, 100)
print(res)

my_list = ["apple", "banana", "cherry"]
lres = rd.choice(my_list)
print(lres)

fres = rd.random()
print(fres)

nvres = rd.normalvariate()
print(nvres)

sq_res = mt.sqrt(6)
print(sq_res)

sin_res = mt.sin(mt.pi /2)
print(sq_res)

e_res = mt.log(mt.e)
print(e_res)

exp_res = mt.exp(3)
print(exp_res)

pi_res = mt.pi
print(pi_res)"""

def get_dtnow() :
    return dt.now()

def cvt_time2str(objtime) :
    return dt.strptime(objtime, '%Y-%m-%d')

def cvt_time2str(strtime) :
    return dt.strftime(strtime, '%Y-%m-%d')

def cvt_str2time(strtime) :
    obj = dt.now()
    return obj.strftime('%Y-%m-%d')

def get_curdir() :
    return os.getcwd()

def os_mkdir(pname) :
    return os.mkdir(pname) 

import os

# 현재 디렉토리 출력 
print(os.getcwd())

# 상위 디렉토리로 변경, 상대경로, 절대경로 
os.chdir("../")

# 변경된 디렉토리 출력
print(os.getcwd())

# 파일목록 출력 
print(os.listdir())

# 폴더 생성 
os.mkdir("new_directory")
print(os.listdir())

# 폴더 삭제 
os.rmdir("new_directory")
print(os.listdir())