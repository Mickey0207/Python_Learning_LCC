import requests
import pandas as pd

def get_web():
    headers = {
        'User-Agent': 'Mozilla/5.0 (<system-information>) <platform> (<platform-details>) <extensions>'
        }
    url = 'https://rate.bot.com.tw/xrt?Lang=zh-TW'

    dfs = pd.read_html(url)
    
    df = dfs[0]
    df.columns = df.columns.get_level_values(1)
    
    df1 = df.iloc[:,0:5]
    df1.columns = ['幣別','現金匯率_本行買入','現金匯率_本行賣出','即期匯率_本行買入','即期匯率_本行賣出']    
    df1.to_csv('C:/Users/notel/OneDrive/IE/GitHub/Python_Learning_LCC/LC_Computer/Class_Program/Class/Other File/currency.csv')

    print(df1)

def date_practise():
    df = pd.read_csv('C:/Users/notel/OneDrive/IE/GitHub/Python_Learning_LCC/LC_Computer/Class_Program/Homework/0210.csv')
    df.index = pd.to_datetime(df.index, format = '%Y%m%d')

    
    
date_practise()