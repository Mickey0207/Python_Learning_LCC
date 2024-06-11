import requests
import pandas as pd
import plotly.graph_objects as g

def get_web():
    headers = {
        'User-Agent': 'Mozilla/5.0 (<system-information>) <platform> (<platform-details>) <extensions>'
        }
    url = 'https://rate.bot.com.tw/xrt/quote/ltm/USD'

    dfs = pd.read_html(url)
    
    df = dfs[0]
    df.columns = df.columns.get_level_values(1)
    df1 = df.iloc[0:,lambda df: [0,4,5]]
    df1.columns = ['日期','即期匯率_本行買入','即期匯率_本行賣出']
    dfr = df1.iloc[::-1]    #座標反轉
    dfr.to_csv('C:/Users/notel/OneDrive/IE/GitHub/Python_Learning_LCC/LC_Computer/Class_Program/Homework/0210.csv', encoding = 'utf-8-sig')

    result = g.Figure()
    result.add_trace(
        g.Scatter(
            x = dfr['日期'],
            y = dfr['即期匯率_本行買入'],
            name = '即期匯率_本行買入',
        )
    )
    result.add_trace(
        g.Scatter(
            x = dfr['日期'],
            y = dfr['即期匯率_本行賣出'],
            name = '即期匯率_本行賣出',
        )
    )
    result.show()
 
    
get_web()