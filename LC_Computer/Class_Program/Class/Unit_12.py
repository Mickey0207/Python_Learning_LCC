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