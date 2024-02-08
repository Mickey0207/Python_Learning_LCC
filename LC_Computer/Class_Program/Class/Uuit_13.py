import pandas as pd

def panda():

    product = {'分類' : ['居家','居家','娛樂','娛樂','科技','科技'],
               '商店' : ['家樂福','大潤發','家樂福','全聯超','大潤發','家樂福'],
               '價格' : [11.42,23.50,19.99,15.95,55.75,111.55]}

    ordinals = ['A','B','C','D','E','F']
    o_small = ['a','b','c','d','e','f']

    global df1 ,df2
    df1 = pd.DataFrame(product, index = ordinals)
    df2 = pd.DataFrame(product, index = o_small)

    df1.to_html("C:/Users/notel/OneDrive/IE/GitHub/Python_Learning_LCC/LC_Computer/Class_Program/Class/Other File/DataFrame.html")
    df2.to_csv("C:/Users/notel/OneDrive/IE/GitHub/Python_Learning_LCC/LC_Computer/Class_Program/Class/Other File/DataFrame.csv", index = True, encoding="utf-8-sig")
    df2.to_json("C:/Users/notel/OneDrive/IE/GitHub/Python_Learning_LCC/LC_Computer/Class_Program/Class/Other File/DataFrame.json", force_ascii = False )

# 陣列取值
def DF_get():
    print(df2.head(2))  # 從陣列的頭取兩個
    print(df2.tail(2))  # 從陣列的尾取兩個

# 走訪DF
def VisitDF():
    
    global df
    df = pd.read_csv("C:/Users/notel/OneDrive/IE/GitHub/Python_Learning_LCC/LC_Computer/Class_Program/Class/Other File/DataFrame.csv", encoding = 'utf-8-sig')

    for index, row in df.iterrows():
        print(index, row['分類'], row['商店'], row['價格'])
        print("====================")

# DF_sort
def DF_sort():
    global df3
    df3 = df1.set_index(['價格'])
    print(df3)
    df3.sort_index(ascending = True, inplace = True)  # ascending : 上升排序 ; inplace :　置換資料表
    print(df3)

# 陣列定位
def index_position():
    
    global df5
    df5 = pd.DataFrame([[1,2,3,4], [100,200,300,400], [1000,2000,3000,4000]],
          columns = ['a','b','c','d'], index = ['p','q','r'])

    print(df5.loc['r','d'])             #索引定位 4000
    print(df5.loc['q':'r','c':'d'])     #索引交叉定位 cd , qr
    print(df5.iloc[0])
    print(df5.iloc[1:3])

# 股票資料
import twstock as ts
import pandas as pd
import plotly.express as e

def stock_data1():

    stock = ts.realtime.get('1101')     # 取得單一股票資料
    print(stock['success'])
    
    result = pd.DataFrame(stock).T.iloc[1:2]
    result.columns = ['代號','地區','股票名稱','公司名稱','時間',
                      '最新成交價','成交量','累計成交量','最佳五檔賣出量','最佳五檔買出價',
                      '最佳五檔買進量','最佳五檔買進價','開盤','最高','最低']
    
    print(result)

def stock_data2():
    capacity = []

    stock = ts.Stock('1101')
    date = stock.date           #日期
    price = stock.price         #收盤價
    capacity = stock.capacity  #成交量
    
    data = pd.DataFrame({'日期':date, '收盤價':price, '成交量':capacity})    
    
    price_line = e.line(data, x = '日期', y = '收盤價', title = '收盤價')
    capacity_bar = e.bar(data, x = '日期', y = '成交量', title = '成交量(單位:股)')    

    price_line.show()
    capacity_bar.show()

stock_data2()