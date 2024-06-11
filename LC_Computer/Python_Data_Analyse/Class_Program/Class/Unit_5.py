#%% 第四堂課回顧
def mult2(x):
    y = 2*x
    return y
# %% 引用函式
mult2(5)
#%% 距離函式 自己寫
import math
def sqr2(x1,y1,x2,y2):
    d1 = (x2 - x1)**2
    d2 = (y2 - y1)**2
    mydis = math.sqrt(d1 + d2) #sqrt:開根號
    return mydis
# %%
sqr2(3,3,6,7)
# %% 距離函式 用套件

import math
a = [3,3]
b = [6,7]
dist = math.dist(a,b)  #dist:畢氏定理
print(dist)
# %% 函數注意事項
def hello_function(word1):
    return f'{word1},sir'
hello_function("hi")

# %% list 不同元素串列產生
a = [3,6,-9]
a.append(-12)
print(a)
a.append("test")
a.append([1,2])
print(a)

#%%
import random
a = []

for i in range(7):
    r = random.randint(1,39)
    a.append(r)
print("開獎結果",a)
print("開獎結果",a[0])

# Note:
# a[0] :指定取用第一個串列元素
# a[-1] :指定取用倒數第一個串列元素
# a[0:3] :指定取用第一個到第三個串列元素
# a[3] = 99 :置換串列第四個元素成為99

# List 基本指令
# list.extend       接龍
# append            加入元素
# insert[2,a]       插入元素
# remove 指定值     刪除
# clear()           清空
# sort              排序
# reverse           反轉

# %%分數比對 作業

num = []
n = int(input("請問有幾個學生?"))
score1 = input("請輸入學生的分數串列")
temp = score1.split("/") #分隔符使用 /

for i in range(n): 
    num.append(int(temp[i]))
num.sort()
if num[0] >= 60:
    print("全班都有過")
    print("最低分",num[0])
    print(num)
elif num[n-1]:
    print("全班都沒過")
    print("最高分",num[n-1])
    print(num)
else:
    print("有的有過有的沒過")