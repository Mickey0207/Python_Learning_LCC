def printmsg():         #print global value
    msg1 = 'global'
    print('print function', msg1)
    global global_index         #global 可宣告為全域變數
    global_index = 'global' 
    
class dog():
    def __init__(self):
        self.color = 'black'
        self.leg = 'sort'
    def eating(self):
        print('my dog is eating.')
    def running(self):
        print('my dog is running.')

class bank():
    def __init__(self, username, money):
        self.__name = username
        self.__balance = money
    
    def save_money(self, money):
        self.__balance = self.__balance + money
        
    def withdraw_money(self, money):
        self.__balance = self.__balance - money
        
    def get_balance(self):
        print('Money in account is : ', self.__balance)
        
leebank = bank('lee', 50000)
leebank.__get_balance()
leebank.__save_money(50000)
leebank.__get_balance()
leebank.__withdraw_money(50000)
leebank.__get_balance()