from selenium.webdriver.ie.service import Service
import twstock as ts
import pandas as pd
import plotly.express as e
import plotly.graph_objects as g
def stock1():
    stock = ts.Stock('0050')
    date = stock.date           #日期
    price = stock.price         #收盤價
    amount = stock.capacity     #成交量

    data = pd.DataFrame({'日期':date, '收盤價':price, '成交量':amount})

    fig1 = e.bar(data, x = '日期', y = '成交量', title = '0050 成交量')
    fig2 = e.line(data, x = '日期', y = '收盤價', title = '0050 收盤價')
    fig1.show()
    fig2.show()
    

def stock2():

    stock = ts.Stock('1101')
    date = stock.date           #日期
    price = stock.price         #收盤價
    amount = stock.capacity     #成交量

    data = pd.DataFrame({'日期':date, '收盤價':price, '成交量':amount})

    fig1 = e.bar(data, x = '日期', y = '成交量', title = '0050 成交量')
    fig2 = e.line(data, x = '日期', y = '收盤價', title = '0050 收盤價')

    five = date[4:]     #將前四筆資料裝入五日均價中
    average = stock.moving_average(price, 5)
    ma5 = pd.DataFrame({'日期':five, '五日均價':average})  #資料項目對齊
    
    ten = date[9:]     
    average = stock.moving_average(price, 10)
    ma10 = pd.DataFrame({'日期':ten, '十日均價':average})  
    
    twenty = date[19:]     
    average = stock.moving_average(price, 20)
    ma20 = pd.DataFrame({'日期':twenty, '二十日均價':average})  
    
    result = g.Figure()
    
#===============================收盤價
    result.add_trace(
        g.Scatter(
            x = data['日期'],
            y = data['收盤價'],
            name = '收盤價',
        )
    )
    #result.show()
    
#===============================五日均價
    result.add_trace(
        g.Scatter(
            x = ma5['日期'],
            y = ma5['五日均價'],
            name = '五日均價',
        )
    )
    #result.show()
    
#===============================五日均價
    result.add_trace(
        g.Scatter(
            x = ma10['日期'],
            y = ma10['十日均價'],
            name = '十日均價',
        )
    )
    #result.show()
    
#===============================五日均價
    result.add_trace(
        g.Scatter(
            x = ma20['日期'],
            y = ma20['二十日均價'],
            name = '二十日均價',
        )
    )
    result.show()

from selenium import webdriver
import os

def Web_data():
    driver = webdriver.Chrome()
    url1 = 'https://www.google.com.tw/'
    url2 = 'https://rate.bot.com.tw/xrt?Lang=zh-TW'

    driver.get(url2) 
    os.system("pause")  #程序暫停
    print(driver.title)
    
Web_data()

