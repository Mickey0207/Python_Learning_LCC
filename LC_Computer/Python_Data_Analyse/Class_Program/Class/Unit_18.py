import pandas as pd

def missing_data():

    df = pd.read_csv(
        'C:/Users/notel/OneDrive/IE/GitHub/Python_Learning_LCC/LC_Computer/Class_Program/Class/Other File/missing_data.csv'
        )

    df1 = df.dropna()   # 一個 NaN 就刪除
    print('一個 NaN 就刪除\n', df1, '\n')
    
    df2 = df.dropna(how = 'all')   # 全部都 NaN 才刪除
    print('全部都 NaN 才刪除\n', df2, '\n')
    
    df3 = df.dropna(subset = ['COL_B','COL_C'])     # COL_B 和 COL_C 有 NaN 的才刪除
    print('COL_B 和 COL_C 有 NaN 的才刪除\n', df3, '\n')
    
    df4 = df.fillna(value = 1.3)        # NaN 換成 1.3\n
    print('NaN 換成 1.3\n', df4, '\n')
    
    df['COL_C'] = df['COL_C'].fillna(df['COL_C'].mean())    # 將 COL_C 的 NaN 替換成平均值
    print('將 COL_C 的 NaN 替換成平均值\n', df, '\n')
    df.to_html(
        'C:/Users/notel/OneDrive/IE/GitHub/Python_Learning_LCC/LC_Computer/Class_Program/Class/Other File/missing_data.html'
        )
    df.to_sql(
        'C:/Users/notel/OneDrive/IE/GitHub/Python_Learning_LCC/LC_Computer/Class_Program/Class/Other File/missing_data.sql'
        )
    
