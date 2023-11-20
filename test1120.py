"""import faker as fk
import os

# temp = fk()
temp = fk("ko-KR")
print(temp.name())

folder = "data/"
if not os.path.isdir(folder):
    os.mkdir(folder)    

with open(folder + "fktemp.csv", "w", encoding='utf8') as f :
    f.write("name,address,postcode,company,job,phone,email,id,ip_prv,ip_pub,catch_parase,color\n")

with open(folder + "fktemp.csv", "w", newline='', encoding='utf8') as f :
    for i in range(30) :
        f.write(temp.name() + "," + 
                temp.address() + "," + 
                temp.postcode() + "," + 
                temp.company() + "," + 
                temp.job() + "," + 
                temp.phone_number() + "," + 
                temp.email() + "," + 
                temp.user_name() + "," + 
                temp.ipv4_private() + "," + 
                temp.ipv4_public() + "," + 
                temp.catch_phrase() + "," + 
                temp.color_name() + "\n")

import pandas as pd

folder = "data/"
target = folder + "fktemp.csv"
df = pd.read_csv(target)

print(df.name == "김병철")

temp = df[df.postcode > 70000]
print(temp)

res = df[df.color == "Beige"].head(1)
print(res)

res = df[df.postcode > 70000][["name", "postcode"]]
print(res)
print(res.count())

df[df.postcode > 70000]


temp = df[df.color == "Ivory"].postcode.mean(1)
print(temp)

temp = df(df.postcode > df.postcode.mean())(["mean", "postcode"])
print(temp)

temp = df.company.insnull()
print(temp)

temp = df[df.company.isnull()][["name"]]
print(temp)

temp = df.compamy.insnull()
for el in temp:
    if el == True:
        print(el)
        
temp = df.name.empty
temp = df[df.company.insnull()][["name", "postcode"]]

temp = df[(df.color == "Beige")]
temp = df[~(df.color == "Beige")]
print(temp)
print(temp.count)
print(temp.color.count())

temp =df[(df.color == "Ivory")& (df.postcode > 70000)]
print(temp)

temp = df.sort_values("postcode")
print(temp)
temp = df.sort_values("name", ascending=False)
temp = df.sort_values("name", abcdefg=True)
print(temp)

# pivot, 데이터 재배열

import pandas as pd

col = ['Machine','Country','Price','Brand']
data = [['TV','Korea',1000,'A'],
        ['TV','Japan',1300,'B'],
        ['TV','China',300,'C'],
        ['PC','Korea',2000,'A'],
        ['PC','Japan',3000,'E'],
        ['PC','China',450,'F']]
df = pd.DataFrame(data=data, columns=col)
print(df)

print("\n-------------------------\n")
print(df.pivot(index='Machine',columns='Country',values='Price'))"""
