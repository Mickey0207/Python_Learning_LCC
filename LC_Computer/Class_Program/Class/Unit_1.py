price=25
print(price>10 and price<20)
print(price>10 or price<20)
print(not price< 10)

temp = 18
if temp > 30:
    print("今天很熱")
else:
    print("今天天氣很好")

num = 30
#num = int(input("請問您的評價?"))
print(str((num))+ ("分"))
if num > 90:
    print("分數是" + str((num)) + "分")
    print("超好吃")
elif num > 80:
    print("分數是" + str((num)) + "分")
    print("不錯")
elif num > 70:
    print("分數是" + str((num)) + "分")
    print("好吃")      
elif num > 60:
    print("分數是" + str((num)) + "分")
    print("不好吃")      
else:
    print("分數是" + str((num)) + "分")
    print("難吃")

#字串格式化，用於抓資料等，便捷運用
#f-string 開始
    name = 'Mickey'
    place = 'Taichung'
    age = '21'

    text = f'Hello! My name is {name},{age} years old, live in {place}'
    print(text)

#for 迴圈 基本練習
    for i in range(2,9):
        print(i)

money = 100000
rate = 0.02

for i in range(1,i+1):
    money = money*(1+rate)
    print(f'第{i}年本利和是{round(money)}:')

for j in range(1,10):
    for k in range(1,10):
        print(f'{j}*{k}={j*k:2}',end = ' , ')
    print()
#Note:{j*k:2},中的:是指輸出時會有兩格字元的輸出
#Note:end = ' ',這是指輸出結果最後的輸出字元
#Note:round(),四捨五入的數學函數

#串列 list 資料表 datafrome
    #[]串列list  ()元組tuple  {}字典dictionary
    #a.append(),加入元素，點點前的a是指程式設計者所定義的串列
a = []
for i in range(10):
    a.append(i)
    print(a)

money = 100000
rate = 0.02
m = []
for i in range(1,i+1):
    money = money*(1+rate)
    m.append(round(money,2))
    print(f'第{i}年本利和是{round(money)}:')
print(m)