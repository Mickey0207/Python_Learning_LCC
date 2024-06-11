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