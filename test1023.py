# 6-1. 파일처리

"""import os

fp = "temp.txt"

file = open(fp, "w")

if os.path.exists(fp) :
    print("ok")
else :
    print("error")"""
    
"""import os

def dir_print(p) :
	files = os.listdir(p)
	for f in files :
		print(f)
  
fp = "temp.txt"

f = open(fp, "w")
f.close()

dir_print("./")

os.remove(fp)
print("----------------\n\n")
dir_print("./")         #temp.txt 삭제 확인 가능!"""

"""import os

fp = "new.txt"

f = open(fp, "w")
f.close()

os.rename(fp, "new1.txt")
print("new1.txt")"""

"""import os

fp = "new.txt"
tp = "new1.txt"

f = open(fp, "w")
f.close()

if os.path.exists(tp):
    print("exists, same name file")
    
else :
    os.rename(fp, "new1.txt")
    print("new1.txt")"""
    
import os

def dir_print(p) :
	files = os.listdir(p)
	for f in files :
		print(f)

fp = "new.txt"
tp = "new1.txt"

f = open(fp, "w")
f.close()

dir_print("./")
print("-------------------------------")

if os.path.exists(tp):
    dir_print("./")
    print("exists, same name file")
    
else :
    os.rename(fp, "new1.txt")
    dir_print("./")
    print("new1.txt")