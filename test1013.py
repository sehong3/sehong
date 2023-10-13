# 파일 생성 / 쓰기
# f = open('new.txt', 'w')
"""
file = open('c:/Users/Catholic/temp.txt', 'a')

for i in range(101) :
    file.write(f"{i}\n")

file.write("hello\n")
file.write("world")

file.close()
"""

"""
# 파일 읽기
file = open('c:/Users/Catholic/temp.txt', "r")
# res = file.read()
# res = file.readline()   # 0나옴
# res = file.readlines()   # ['0\n, '1\n' ...]

for i in range(110) :
    res = file.readline()
    print(res)

file.close()
"""

"""f = open('c:/Users/Catholic/temp.txt', "r")
line = f.readlines()
for l in line :
    print(l)"""
    
f = open('c:/Users/Catholic/temp.txt', "r")    
for line in f :
    print(line)
f.close()