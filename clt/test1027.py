# 속성 출력

"""class Person :
	name = "python"
	age = 23
	number = "01012345678"
 
p = Person()
print(p.name)
print(p.age)
print(p.number)

p1 = Person()
print(p1.name)
print(p1.age)
print(p1.number)"""

# 메서드, 셀프

"""class Person :
	name = "python"
	age = 23
	number = "01012345678"

	def getIntroduce(self):
		return f"My name is {self.name}"

p = Person()
print(p.name)
print(p.age)
print(p.number)
print(p.getIntroduce())"""

# 생성자 메서드

"""class Person :
	def __init__(self, name, age, number):
		self.name = name
		self.age = age
		self.number = number
  
p = Person("hello", 24, "01111111111")
p1 = Person("hi", 21, "0100")
p2 = Person("hiiiii", 29, "11100000")

print(p.name)
print(p.age)
print(p.number) 

print(p1.name)
print(p1.age)
print(p1.number) 

print(p2.name)
print(p2.age)
print(p2.number) """

# 클래스 변수

class Person :
	count = 0
	
	def __init__(self, name, age, number):
		self.name = name
		self.age = age
		self.number = number
		Person.count +=1
@classmethod
def getCount(cls) : 
    return cls.count

  
p = Person("hello", 24, "01111111111")
p1 = Person("hi", 21, "0100")
p2 = Person("hiiiii", 29, "11100000")

print(p.name)
print(p.getCount())

print(p1.name)
print(p1.getCount())

print(p2.name)
print(p2.getCount())
