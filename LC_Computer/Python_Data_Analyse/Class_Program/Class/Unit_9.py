'''集合演算法

1.issubset()   ; 語法 : set1.issubset(set2) ; sub(負數,子層級)
2.issuperset() ; 語法 : set1.issuperset(set2) ; super(主層級)
3.isdisjoint() ; 語法 : set1.isdisjoint(set2) ; dis(否定性的) ; joint(不結合)

'''

from multiprocessing import Value


def set_practise():
    set1 = {1,2,3,'3'}
    set2 = {1,2}
    set3 = {3,3}
    print(set1.issuperset(set2))
    print(set3.issubset(set1))
    print(set1.isdisjoint(set1))

def set_repeat_text_judgment():
    a = 'zxcvbbbbbbbbbb' 
    b = 'qwertjpppp'
    a_set = set(a)
    b_set = set(b)
    print(a_set)
    print(b_set)
    
    if len(a_set & b_set) > 0:
        print("True")
        print(len(a_set & b_set))
    else:
        print("false")
        
'''前章的考試作業測驗'''

def advanced_def_quiz(num,q,a):
    q_and_a = {q:a}
    print(num,q_and_a)
    print(type(q_and_a))
    print(len(q) + len(a))


'''Vip_Data_System'''
def build_vip(id,name,tel = '0960'):
    vip_dict = {'vipid':id,'name':name,'tel':tel}
    if tel:
        vip_dict['tel'] = tel
    return vip_dict 

def build_vip_homework(): 
    
    import csv
    id, name, tel, choose = [], [], [], 'y'
    
    while True:
        
        if choose == 'y':
            id.append(input("Enter your ID : "))
            name.append(input("Enter your name : "))
            tel.append(input("Enter your tel : "))
            choose = input("Continue a next data? y/n ")
        elif choose == 'n':
            break                   
        else:
            choose = input("Continue a next data? y/n ")
            
    import csv
    path = 'C:/Users/notel/Desktop/data_file.csv'
    with open(path,'w',newline='') as data_file:
        writer = csv.writer(data_file)
        writer.writerow(['ID','Name','Phone','\n'])
        
        for a in range(len(id)):  
            #Write data
            writer.writerow([id[a],name[a],tel[a],'\n'])
    print('Welcome to use again.')  

def mailmsg(students):
    str1 = 'classmate hello'
    str2 = 'advanced Python'
    for student in students:
        msg = student + str1 + str2
        print(msg)

'''當引數個數不確定'''
def make_icecream(itype,*cookies):
    print('This', itype, 'Icecream is a :')
    for cookie in cookies:
        print('======', cookie) 
        
'''當字典長度不確定'''
def build_nbadict(name, age, **playerinfo):
        info = {}
        info['name'] = name
        info['age'] = age
        for key , Value in playerinfo.items:    
            info[key] = Value
        return info

'''函數內的函數'''
def dist(x1, y1, x2, y2):
    def myroot(z):
        return z**0.5
    dx = (x2 - x1)**2
    dy = (y2 - y1)**2
    return myroot(dx + dy)