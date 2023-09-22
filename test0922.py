import calc
print(dir(calc))

"""import calc
add_res = calc.add(8, 4)
sub_res = calc.sub(8, 4)
mul_res = calc.mul(8, 4)
div_res = calc.div(8, 4)"""

"""print(calc.add(8, 4))
print(calc.sub(8, 4))
print(calc.mul(8, 4))
print(calc.div(8, 4))"""

"""import calc as cl

print(cl.add(8, 4))
print(cl.sub(8, 4))
print(cl.mul(8, 4))
print(cl.div(8, 4))"""

"""import mod.circle_mod as cm

print(cm.pi)
print(cm.cc_area(4))
print(cm.cc_len(5))

import mod.str_util as smod

url = "https://www.notion.so/test/4-1/a1fe5ef0df1/41f7a1aa9ec01/3a859a"
res = smod.cutword(url, "/", 3)

def cutstr(st, wd, idx) :
    tmp = st.split(wd)
    res = tmp[idx]
    return res

url = "https://www.notion.so/test/4-1/a1fe5ef0df1/41f7a1aa9ec01/3a859a"
res = smod.cutword(url, "/", 3)
print(res)


import mod.str_util as smod

url = "https://www.notion.so/test/4-1/a1fe5ef0df1/41f7a1aa9ec01/3a859a"
res = smod.cutword(url, "/", 3)"""

"""import math
sq_res = math.sqrt(6)
print(sq_res)

sq_res = math.sin(math.pi /2)
print(sq_res)

e_res = math.log(math.e)
print(e_res)

exp_res = math.exp(3)
print(exp_res)

pi_res = math.pi
print(pi_res)"""

"""import mod.utils as mu

res = mu.mt.sqrt(2)
print(res)

sin = mu.mt_sinpi()
print(sin)

el = mu.mt_elog
print(el)

ep = mu.mt_exp(3)
print(ep)

pi = mu.mt_pi()
print(pi)"""

import random as rd

res = rd.randint(1, 100)
print(res)

my_list = ["apple", "banana", "cherry"]
lres = rd.choice(my_list)
print(lres)

fres = rd.random()
print(fres)

nvres = rd.normalvariate()
print(nvres)