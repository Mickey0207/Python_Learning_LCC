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

plt.plot(a,b,'go--',a,c,'r^-.',a,d,'b+-',linewidth=2,markersize=8)
plt.title("random_number")
plt.xlabel("fixed_number")
plt.ylabel("random_number")
plt.grid()         #增加圖表的格子
plt.legend(['random1','random2','random3'],loc = 9) 
#增加圖例,loc:調整位置 1=右上，2=左上
plt.show()