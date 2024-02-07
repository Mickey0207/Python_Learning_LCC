#圖表製作
#%%
a = []                      #月份資料集合
b = []                      #每月支出資料集合
for i in range(1,7):        #產出六個月的資料
    a.append(i)             #輸入月份資料
    b.append(2**i)          #輸入每月支出資料
print('a = ' ,a,'b = ',b)   #列印資料

import matplotlib.pyplot as plt
plt.plot(a,b)
#%%
a = []                      #月份資料集合
b = []
c = []                      #每月支出資料集合
for i in range(1,7):        #產出六個月的資料
    a.append(i)             #輸入月份資料
    b.append(2**i)          #輸入每月支出資料
#print('a = ' ,a,'b = ',b)  #列印資料

import matplotlib.pyplot as plt
plt.plot(a,b)
plt.show()                  #消除輸出註解
#%%                      
a = []                      #月份資料集合
b = []                      #每月支出資料集合
for i in range(1,7):        #產出六個月的資料
    a.append(i)             #輸入月份資料
    b.append(2**i)          #輸入每月支出資料
#print('a = ' ,a,'b = ',b)  #列印資料

import matplotlib.pyplot as plt
plt.plot(a,b,color ='red',linewidth=2,markersize=12)        #plot:繪製長條圖
plt.show()                  #圖表啟用

# %%
a = []                      #月份資料集合
b = []                      #每月支出資料集合
for i in range(1,7):        #產出六個月的資料
    a.append(i)             #輸入月份資料
    b.append(2**i)          #輸入每月支出資料
#print('a = ' ,a,'b = ',b)  #列印資料

import matplotlib.pyplot as plt
plt.bar(a,b,width=0.3,color = 'green')      #bar:繪製長條圖
plt.title("Money")          #標題設置
plt.xlabel("month")         #X軸標籤
plt.ylabel("Money")         #Y軸標籤
plt.show()                  #圖表啟用

#%%
import matplotlib.pyplot as plt
a = []
b = []
money = 100000
c = int(input("請問要存幾個年?"))
rate = float(input("請問你的年利率?"))
for i in range(1,c+1):
    a.append(i)
    money = money*(1+rate)
    b.append(money)
plt.plot(a,b)
plt.title("all_money")
plt.xlabel("year")
plt.ylabel("money")
plt.show()
# %% 圓餅圖繪製
a = []
for i in range(1,7):
    a.append(i)
a = ['trans','food','book','game','clean','cel']
b = [5,9,4,2,1,3]
exp = [0.2,0,0,0,0,0]
import matplotlib.pyplot as plt
plt.pie(b,labels=a,autopct='%.1f%%',explode = exp)
plt.show()

#Note: %.1%%
# %...% :控制字元
# f :小數
# %.3f : 3位小數
# autopct : 數字加入%
# explode : 圓餅圖的爆炸
# %% 隨機圖表繪製
import matplotlib.pyplot as plt
import random       #隨機函數
a = []
b = []
c = [1,3,4,8,9,6]
for i in range(1,7):
    r = random.randrange(1,9)
    a.append(i)
    b.append(r) 
plt.plot(a,b,'go--',a,c,'r^--',linewidth=2,markersize=8,)
plt.grid()         #增加圖表的格子
plt.legend(['normal','random'],loc = 9) 
#增加圖例,loc:調整位置 1=右上，2=左上
plt.show()
# %% 作業
import matplotlib.pyplot as plt
import random       #隨機函數
a = [1,2,3,4,5,6]   #X軸固定
b = []              #第一條數
c = []              #第二條數
d = []              #第三條數
num1 = input("請選擇第一條數是 隨機 或 自行輸入?") 
num2 = input("請選擇第二條數是 隨機 或 自行輸入?")
num3 = input("請選擇第三條數是 隨機 或 自行輸入?")

if num1 == '自行輸入':
   b = input("請輸入6位數集合")
else:
   for i in range(1,7):
        r = random.randrange(1,9)
        b.append(r)

if  num2 == '自行輸入':
    c = input("請輸入6位數集合")
else:
    for j in range(1,7):
        t = random.randrange(1,9)
        c.append(t)

if num3 == '自行輸入':
    d = input("請輸入6位數集合")
else:
    for k in range(1,7):
        u = random.randrange(1,9)
        d.append(u)

plt.plot(a,b,'go--',a,c,'r^-.',a,d,'b+--',linewidth=2,markersize=8)
plt.title("random_number")
plt.xlabel("fixed_number")
plt.ylabel("random_number")
plt.grid()         #增加圖表的格子
plt.legend(['random1','random2','random3'],loc = 9) 
#增加圖例,loc:調整位置 1=右上，2=左上
plt.show()