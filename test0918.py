#type

# print(pow(2, 2))
# print(pow(2, 6))

# print(divmod(10, 3))

# print(round(3.14))

# a = (3, 5, 7)
# b = list(a)
# c = tuple(b)

# print(b)
# print(c)

# print(type(a))
# print(type(b))
# print(type(c))

# ctrl / 같이 누르면 주석 처리

# range

# for i in range (2, 7): 
#     print(i)
    
# # max, min, sum

# a = [3, 5, 6, 9]
# print(max(a))
# print(min(a))
# print(sum(a))

# abs

# print(abs(-3))
# print(abs(3.0))
# print(abs(-3.0))

# sorted

# a = [5, 3, 1, 9, 4]
# print(sorted(a))
# print(sorted(a, reverse=True))

# enumerate

# a = [5, 3.14, False, 9, "string"]
# print(enumerate(a))
# print(*enumerate(a))

# zip

# a = [1, 2, 3]
# b = [4, 5, 6]
# print(zip(a, b))
# print(*zip(a, b))

# a = [True, True, False]
# print(any(a))
# print(all(a))

# format

"""a = 20
b = 23
c = "a 는 {}, b 는 {}, {}".format(a, b, "python")
print(c)"""

"""a = 3
print(globals())
print(locals())
print(dir(a))
print(callable(a))"""

"""add = lambda a, b : a + b
sub = lambda a, b : a - b
mul = lambda a, b : a * b
div = lambda a, b : a / b 

print(add(2,3))
print(sub(4,7))
print(mul(2,7))
print(div(8,2))"""

"""def add_numbers(x, y):
    return x + y

# 함수 호출
result = add_numbers(4, 5)
print(result)"""

"""def greet(name):
    print(name)
    print("Hello, " + name + ". How are you?")
greet("python")"""
    
"""def add(a, b) : 
	print(a + b)
 
# return 하는 것 권장. 
def sub(a, b) :
	return a - b

def mul() :
	return 2 * 4

def div() :
	print(4 / 2)

add(3, 5)
print(sub(3, 5))
print(mul())
div()"""

"""def is_even(n) : 
    if n % 2 == 0 :
        print("짝수")
    else : 
        print("홀수")
num = input("숫자를 입력하세요 : ")

is_even(int(num))"""

"""def reverse_string(msg) :
  return msg[::-1]

in_str = input("문자열 : ")
print(reverse_string(in_str))"""

"""def add(a, b) : 
    return int(a) + int(b)

def sub(a, b) : 
    return int(a) - int(b)

def mul(a, b) :
    return int(a) * int(b)

def div(a, b) : 
    return int(a) / int(b)

a = input("a 를 입력하세요.")
b = input("b 를 입력하세요.")

print("더하기 : ", add(a, b))
print("빼기 : ", sub(a, b))
print("곱하기 : ", mul(a, b))
print("나누기 : ", div(a, b))"""

def sum_num(num) :
    return sum(num)

nums =  []

for i in range (1, 6) :
    innum = int(input(f"{1} 번째 숫자 입력 : "))
    nums.append(innum)
    
    print(sum_num(nums))
    
    # debug... 중요함!....