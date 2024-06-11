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