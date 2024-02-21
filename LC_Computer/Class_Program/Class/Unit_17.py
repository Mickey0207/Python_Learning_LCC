""" 資料清理三大指令
    split()     : 切割字元        
    repleace()  : 取代特定字元
    strip()     : 清除特定字元
"""

def string_practise():
    str1 = '''
            Python is a programming language 
            that lets you eork quickly and integrate systems 
            more effectively.
            '''
        
    list1 = str1.split()
    print('將字彙分割變成串列\n', list1, '\n')

    str2 = ','.join(list1)
    print('將串列字彙提出後用逗號分開\n', str2, '\n')

    str3 = ''' Python is a \nprogramming language. \n\r '''
    
    str4 = str3.replace('\n', '').replace('\r','')  # string data replace
    print('特定字元清除', str4, '\n')
    print("前後加引號","'" + str4 + "'", '\n')
    print("消除特定字元","'" + str4.strip() +  "'", '\n')    # strip : 消除特定字元,無指定則消除空格
    
# 刪除標點符號

import string 

def string_test():
    str1 = '#$%^Python -is- *a* $%programming_ language.$'
    print(string.punctuation)   # punctuation can str of clean in the print.
    
    list1 = str1.split(' ')
    print(list1)
    
    for item in list1:
        print(item.strip(string.punctuation))
    
# 引用 正則表達式
# 正則表達式測試網站 : http://regexr-cn.com/

import re

def re_practise():
    pattern1 = 'cat'
    pattern2 = 'bird'
    string = 'dog runs to cat'
    print(pattern1 in string)
    print(re.search(pattern1, string))
    
    print(re.search(r"r[0-9]n", 'dog r7ns to cat'))
    print(re.search(r"r[a-z]n", 'dog runs to cat'))
    print(re.search(r"r[A-Z]n", 'dog rUns to cat'))     
    print(re.search(r"r[0-9a-zA-Z]n", 'dog runs to cat'))
    
string_practise()