# from bs4 import BeautifulSoup as bs
# import requests as rq

# url = "https://news.daum.net/"
# res = rq.get(url)

"""hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')

item = res_html.select_one("body > div.container-doc > main > section > div > div.content-article > div.box_g.box_news_issue > ul > li:nth-child(1) > div > div > strong > a")
print(item)
print(item.get_text())

wt = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_detail > a > div > span.txt_name")
print(wt)
print(wt.get_text())

goods = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_reply > div > button > strong")
print(goods)
print(goods.get_text())"""

"""hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')

iss = res_html.select("a.wrap_thumb")
print("\n------------------------\n")

for i in iss:
    issue = i.get_text()
    print(issue)
    
print("\n------------------------\n")
ct = res_html.select("a.wrap_thumb")
for j in ct:
    c = j.attrs["data-flare-custom"]
    print(c = "\a")"""
    
"""from bs4 import BeautifulSoup as bs
import requests as rq
import os
from urllib.request import urlretrieve as rl

url = "https://news.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, "html.paper")

img = res_html.select("img")
print(img)
print("\n-------------------------\n")

linkings = []

for i in img:
    img = i.attrs["sec"]
    print(img + "\n")
    linkings.append(img)
    
folder = "img"
if not os.path.isdir(folder):
    os.mkdir(folder)
    
i = 0
for ln in linkings:
    if str(ln).find("\n") == False :
        print(ln)
        continue
    
    else:
        pass
    
    i == i
    rl(ln, folder + f"(i).img")"""
    

"""#import pandas.Series
from pandas import Series as sr
data = [10, 20, 30, 40]
sdata = sr(data)
print(data)"""

"""import numpy as np
data = np.arange(1, 5)
sdata = sr(data)
print(data)"""

# from pandas import Series as sr

# data = [10, 20,30, 40]
# sdata = sr(data)
# print(sdata.index)
# print(sdata.index.to_list())

"""print(sdata)
print("\n------------\n")
sdata.index = ['a', 'b', 'c', 'd']
print(sdata)"""

"""data = [10, 20,30, 40]
idx = ["a", "b", "c", "d"]
sdata = sr(data, idx)
print(sdata)"""

"""dt = [10, 20,30, 40]
idx = ["a", "b", "c", "d"]
sdata = sr(index=idx, data=dt)
print(sdata)"""

"""dt = [10, 20,30, 40]
idx = ["a", "b", "c", "d"]
sdata = sr(data=dt, index=idx)
sd = sdata.reindex(["a", "j", "c"])
print(sd)"""

"""dt = [10, 20,30, 40]
idx = ["a", "b", "c", "d"]
sdata = sr(data=dt, index=idx)

sd = sdata.reindex(["b"])
print(sd)
print("\n----------\n")
print(sdata["b"])
print("\n----------\n")
print(sdata.iloc[0])
print(sdata.iloc[2])
print("\n----------\n")
print(sdata.loc["a"])
print(sdata.loc["d"])"""

from pandas import Series as sr

"""dt = ["alpha", "beta", "charlie", "delta"]
idx = ["ab", "bc", "cd", "de"]

sdata = sr(data=dt, index=idx)
print(sdata.loc["bc" : "cd"])
print("\n----------\n")
print(sdata.loc["bc" : ])
print("\n----------\n")
print(sdata.loc[:"bc"])"""

"""dt = ["사과", "바나나", "수박", "참외"]
idx = ["가", "나", "다", "라"]
sdata = sr(data=dt, index=idx)

print(sdata.iloc[1:2])
print(sdata.iloc[2:])
print(sdata.iloc[:2])"""

"""dt = ["alpha", "beta", "charlie", "delta"]
idx = ["ab", "bc", "cd", "de"]
sdata = sr(data=dt, index=idx)

# sdata.loc["cd"] = "echo"
# sdata.iloc[1] = "fox"
# sdata.loc["ef"] = "golf"
# print(sdata.drop("bc"))
print(sdata)"""

"""s1 = sr([100, 200, 300], index=["a", "b", "c"])
s2 = sr([100, 200, 300], index=["b", "c", "a"])

sum = s1 + s2
print(sum.max())
print(sum.mean())
print(sum.min())
print("\n----------\n")
sub = s1 - s2
print(sub.max())
print(sub.mean())
print(sub.min())
print("\n----------\n")
mul = s1 * s2
print(mul.max())
print(mul.mean())
print(mul.min())
print("\n----------\n")
div = s1 / s2
print(div.max())
print(div.mean())
print(div.min())"""

"""data = {
    "삼성전자": "전기,전자",
    "LG전자": "전기,전자",
    "현대차": "운수장비",
    "NAVER": "서비스업",
    "카카오": "서비스업"
}

sdata = sr(data)
uniq = sdata.unique()
print(uniq)

sdata.count()

sdata.value_counts()"""

"""idx = ["a", "b", "c", "d", "e"]
s1 = sr([1100, 270, 30, 450, 50], index=idx)
s2 = sr([150, 740, 810, 40, 25], index=idx)

# 시리즈내 데이터 비
fil = s1 > 300
print(fil)
print("\n----------\n")

fil = s1 > 300
print(fil)
print("\n----------\n")

# 시리즈간 비교
fil1 = s2 > s1
print(fil1)
print(s2[fil1])
print(s2[fil1].index)

# 인덱싱 출력
s2[s2 > s1].index"""

idx = ["a", "b", "c", "d", "e"]
dt = [1100, 270, 30, 450, 50]
sl = sr(data=dt, index=idx)

sw = sl.sort_values()
print(sw)
print("\n----------\n")
