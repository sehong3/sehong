"""
my_list = [9, 4, 3, 7, 8, 'hi']
print(4 in my_list)
print(2 in my_list)
print(2 not in my_list)

my_dic = {"key1" : "v1", "k2" : "v2"}

x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is y)  
print(x is z)  
print(x is not y)  

a = 5
b = 5
print(a is b)
print(a is not b)
print(3==3.0)
print(3 is 3.0)"""

"""
"""

"""a = [3 , 5, 1]
b = a

print(a is b)

a = 2 ** 3 ** 2
print(a)    

b = 10 / 5 / 2
print(b)

c = 2 ** (3 ** 2)
print(c)

d = 10 % 3 % 2
print(d)

e = 1 + 2 > 3 and 4 - 1 < 2
print(e)

f = 1 & 2 | 3 ^ 4
print(f)

g = 5 in [3, 4, 5] or 2 not in [1, 2, 3]
print(g)

h = 2 * -3 // 2
print(h)

i = 1== 2 != 3
print(i)

x = 10

if x > 0:
    print("x is positive")

elif x < 0:
    print("x is negative")

else:
    print("x is zero")
    
    char = a
if char==a:
    print("문자는 a입니다.")
else:
    print("문자는 b입니다.")
      
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
    
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in my_list:
    for num in row:
        print(num)
        

my_list=[1,2,3,4,5,6,7,8,9]
my_list.reverse()
for num in my_list:
    print(num)
        
rang = [5, 8, 3, 1, 6]

for i in rang:
	print("element : ", i)
else :
	print("end process")

for i in range(10):
    if i == 7:
        break
    elif i == 1:
        continue
    else:
        pass

    print(i)
    
i = 1

while i <= 5:
    print(i)
    i += 1"""

for i in range (0, 10): print(i)
print("\n")


list1=[10, 20, 30, 40, 50, 60]
for i in reversed(list1): print(i)
print("\n")

for i in sorted(list1, reverse = True): print(i)

for i in range(1, 10) :
    for j in range(1, 10) :
        print(i, "X", j, "=", i*j)
        


""" while """
i = 0
w = "hello world"
while i < len(w):
    print(w[i])
    i += 1


i = 1
while  i<= 5 :
    print(i)
    i += 1
    
    
i = 0
while(i<10):
    
    print(i)
    i += 1
    
sum = 0
i = 1
while(i <= 10) :
    sum += i
    i += 1

i = 1
while(i <= 100) :
    if(i%2==0):print("짝수")
    else : print("홀수")
    i += 1

i = 1
while(i<=100) :
    if(i%7==0): print("7의 배수이다")
    i += 1
