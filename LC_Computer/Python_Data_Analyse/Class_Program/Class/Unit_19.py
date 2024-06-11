from sqlite3 import Cursor
from tkinter import CHAR
import pymysql


def DataBase_Read():
    # 主機 ， 使用者 ， 密碼 ， 資料庫 ， 字元集
    data_base = pymysql.connect(
        host = 'localhost', user = 'root', password = 'Walkerkevin2580', 
        database = 'mybooks'
        )

    cursor = data_base.cursor()
    cursor.execute('select * from books')   # MySQL program
    data = cursor.fetchall()
    
    for row in data:
        print(row[0], row[1], row[3])
        
    data_base.close()   # close SQL
    


def DataBase_Write():
    
    book = 'Q0003,py and mysql,邱,666,線上,2023-02-17'
    f = book.split(',')
    
    data_base = pymysql.connect(
        host = 'localhost', user = 'root', password = 'Walkerkevin2580', 
        database = 'mybooks'
        )
    cursor = data_base.cursor()   
    
    sql = '''
        insert into books(id, title, author, price, category, pubdate)
        value('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')
        '''
    sql = sql.format(f[0],f[1],f[2],f[3],f[4],f[5])
    cursor.execute(sql)     # 帶入要寫的資料
    data_base.commit()      # 確認交易
    print('新增一筆紀錄')

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import math

def data_analyis():
    x = [0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10]
    
    sinus = [math.sin(v) for v in x]
    cosinus = [math.sin(v) for v in x]
    
    sns.set()       # open seaborn
    fig, axea = plt.subplots(1, 2, figsize = (12, 8))
    ax1 = sns.lineplot(x = x, y = sinus, ax = axea[0])
    ax2 = sns.scatterplot(x = x, y = cosinus, ax = axea[1])
    plt.show()
    
data_analyis()