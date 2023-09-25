"""# datetime 모듈의 datetime 함수를 dt라는 별명으로 사용
from datetime import datetime as dt

print(dt.now())"""

"""from pytz import timezone 
tz = timezone('Asia/Seoul')
tz = timezone('UTC')
print("timezone : ", dt.now(tz))

dt.now(timezone)
dt.strptime
object.strftime"""

"""# 문자열을 날짜로 변환
date_string = "2021-09-25"
date_object = dt.strptime(date_string, '%Y-%m-%d')
print(date_object)                           

# 날짜를 문자열로 변환
date_object = dt.now()
date_string = date_object.strftime('%Y-%m-%d')
print(date_string)"""

"""import mod.utils as mu

dtnow = mu.get_dtnow()
print(dtnow)

ret = mu.cvt_time2str("2023-09-25")
print(ret)

res = mu.cvt_time2str()
print(res)"""

"""import os

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
print(os.listdir())"""

"""import mod.utils as mu
import os

print(mu.get_curdir())

pname = "python"
mu.os_mkdir(pname)
print(os.listdir())

os.rmdir(pname)
print(os.listdir())"""

"""import sys

# 버전정보 출력 
print(sys.version)

# 명령 인수 확인 
print(sys.argv)"""


# stack

"""st = []

# 스택에 값 넣기
st.append(1)
st.append(2)
st.append(3)
st.append(4)
st.append(5)

# 스택의 상태 확인
print(st) # [1, 2, 3]

# 스택에서 값 빼기
top = st.pop()
print(top) # 3
print(st) #
print(len(st)) #"""

queue = []

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

print(queue) # [1, 2, 3]

front = queue.pop(0)
print(front) # 1
print(queue) # [2, 3]
print(len(queue))

qlist = []