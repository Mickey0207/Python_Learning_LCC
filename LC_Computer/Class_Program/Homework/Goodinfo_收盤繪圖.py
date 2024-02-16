import os
import requests
import pandas as pd
import plotly.express as e

from cgitb import text
from bs4 import BeautifulSoup
from selenium import webdriver

def web_analysis2():    # 優化 = prettify
    # User agent
    headers = {'User-Agent': 'Mozilla/5.0 (<system-information>) <platform> (<platform-details>) <extensions>'}
    # URL
    res = requests.get('https://goodinfo.tw/tw/StockBzPerformance.asp?STOCK_ID=1101', headers = headers)

    # res encoding : utf-8
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'lxml')
    table_data = soup.select_one('#txtFinDetailData')
    
    # pandas : read html , prettify data ; Clean Data
    dfs = pd.read_html(table_data.prettify())
    df = dfs[0]
    df.columns = df.columns.get_level_values(1)    # Stay only columns
    
    # Stock make a price chart.
    fig2 = e.line(df, x = '年度', y = '收盤', title = '1101 收盤價')
    fig2.show()

web_analysis2()