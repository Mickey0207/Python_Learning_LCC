import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd
import math

def Chart_Creative():
    x = [
        0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,
        5.5,6,6.5,7,7.5,8,8.5,9,9.5,10
        ]
    
    sinus = [math.sin(v) for v in x]
    sns.set_style('whitegrid')
    sns.lineplot(x = x, y = sinus)
    plt.show()
    
def Chart_Creative2():
    df = sns.load_dataset('tips')
    sns.set()
    sns.relplot(x = 'total_bill', y = 'tip',
                hue = 'smoker', style = 'smoker', data = df)
    plt.show()
    
def Chart_Creative3():
    df = sns.load_dataset('tips')
    sns.set()
    sns.relplot(df['total_bill'], kde = False)
    plt.show()

def Chart_Creative4():
    df = sns.load_dataset('tips')
    sns.set()
    sns.distplot(df['total_bill'], kde = False)
    sns.distplot(df['total_bill'], kde = False, bins = 20)
    sns.distplot(df['total_bill'], kde = False, bins = 30)
    plt.show()
    
def Chart_Creative5():
    df = sns.load_dataset('tips')
    sns.set()
    sns.distplot(df['total_bill'], hist = False)
    plt.show()    
    sns.distplot(df['total_bill'] )
    plt.show()
    
def Chart_Creative6():
    df = sns.load_dataset('tips')
    sns.pairplot(df)
    plt.show()
    
def Chart_Creative7():
    df = sns.load_dataset('iris')        
    sns.pairplot(df, kind = 'scatter', diag_kind = 'kde', 
                 hue = 'species', palette = 'husl')
    plt.show()

Chart_Creative7()