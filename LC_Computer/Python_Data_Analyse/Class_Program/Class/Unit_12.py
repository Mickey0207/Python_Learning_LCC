# class 練習
from ast import Name

class ReadFile():
    def __init__(self, path):
        self.name = path
        self.fileobj = open(self.name, 'r', encoding = 'utf-8')
    
    def ReadFile(self):
        return self.fileobj.readlines()
    
def ReadFile_implement():
    F_path = "C:/Users/notel/OneDrive/IE/GitHub/Python_Learning/Python_Learning/LC_Computer/Class_Program/Class/0116.txt"
    F = ReadFile(F_path)
    txt = F.ReadFile()
    for  t in txt:
        print(t)
        
class Father():
    def __init__(self):
        self.color3 = 'orange'
    def move(self):
        print('running fast')
        
class Son(Father):
    def __init__(self, legs):
        super().__init__()      #繼承父系屬性
        self.legs = legs
    def move(self):
        print('running fast')

# 作業    
class Personal():
    def __init__(self, name = 'name', id = 'id', fee = 'fee'):
        self.name = name
        self.id = id
        self.fee = fee
        
    def info(self):
        print(f'會員編號 : {self.id}')
            
    def get_discount(self):
        print(f'的費用是 : {self.fee} 元')
            
class memeber(Personal):
    def member(self):    
        super().info()
        print("您是一般會員")
    def get_discount(self):
        money = self.fee * 0.8
        print(f'的費用是 : {self.fee} 元，打折後為 : {money}')
        
class GoldMember(memeber):
    def member(self):
        super().info()
        print("您是金卡會員")
    def get_discount(self):
        money = self.fee * 0.6
        print(f'的費用是 : {self.fee} 元，打折後為 : {money}')
        
member1 = GoldMember('lee', '10052', 15000)
member1.member()
member1.get_discount()

# Pandas 資料處理函數
''' 
    States          Population        Postal
0   California      39613493          CA
1   Texas           29730311          TX
2   Florida         21944577          FL
3   New York        19299981          NY

'''

# Pandas Series

import pandas as pd
fruits = ['apple', 'orange', 'lemon', 'grape', 'banana', 'tomato']
num  = [1, 3, 5, 7, 9, 11]

s = pd.Series(num, index = fruits)
print(s)
print(s.index)
print(s.values)
print('orange = ', s['orange'])             #取一個索引值
print('orange = ', s[['orange','lemon']])   #取兩個索引值
print((s + 5)*3)

print("\n\n")

product = {'分類' : ['居家','居家','娛樂','娛樂','科技','科技'],
           '商店' : ['家樂福','大潤發','家樂福','全聯超','大潤發','家樂福'],
           '價格' : [11.42,23.50,19.99,15.95,55.75,111.55]}
df = pd.DataFrame(product)
print(df)

ordinals = ['A','B','C','D','E','F']
o_small = ['a','b','c','d','e','e']

df1 = pd.DataFrame(product, index = ordinals)
df2 = pd.DataFrame(product, index = o_small)
print(df1)
print(df2)

df1.to_html("C:/Users/notel/OneDrive/IE/GitHub/Python_Learning_LCC/LC_Computer/Class_Program/Class/Other File/DataFrame.html")
# <mete charset = "utf-8"> # html 的編碼轉換，填在第一行