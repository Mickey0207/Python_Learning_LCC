#%%
while True:
    a = input("請輸入資料")
print("881")

# %% 資料輸出到記事本但不收錄Q
path = 'C:/Users/walke/Desktop/Mickey01.txt'    #python的目錄分隔字元使用\
f = open(path,'w')
b = []

while True:
    a = input("請輸入資料")
    if a != "Q":                    #!= :是不等於的意思
        f.write(a + "\n")           #\n :是換行
        b.append(a)
    else:
        break

f.close()
print("881")
# %% 資料輸出到記事本但不收錄Q with open mode
path = 'C:/Users/walke/Desktop/Mickey01.txt'    #python的目錄分隔字元使用\
b = []
with open(path,"a") as f:

    while True:
        a = input("請輸入資料")
        if a != "Q":                    #!= :是不等於的意思
            f.write(a + "\n")           #\n :是換行
            b.append(a)
        else:
            break

print("881")

#%% 小作業
path = 'C:/Users/walke/Desktop/Mickey01.txt'
b = []
i = 1
print("今天過的好嗎?")
with open(path,"a") as f:

    while True:
        a = input("請輸入資料")
        i = i+1
        if a != "Q":                    #!= :是不等於的意思
            f.write(a + "\n")           #\n :是換行
            b.append(a)
        else:
            break
print("您的輸入已完成，您總共輸入" + str(i-1) + "次")

# %% CSV檔建置
import csv
path = 'C:/Users/walke/Desktop/data_file.csv'
with open(path,'w',newline='') as data_file:
    writer = csv.writer(data_file)

    #Write data
    writer.writerow(['姓名','身高','體重'])
    writer.writerow(['又成','180','80'])
    writer.writerow(['結語','170','70'])
print("寫入完成")
# %% CSV檔讀取
import csv
path = 'C:/Users/walke/Desktop/Data.csv'
with open(path,'r',encoding='utf8') as data_file:
    read = csv.reader(data_file)

    #Read data
    for r in read:
        print(r)
        
print("讀取完成")
#Note : multibyte 是多重字元的意思。

# %% 函式 def

def sayhello():
    print("hello world")

sayhello()
# %% 建立函式函數

def mysum(x,y):
    rs = 0
    for i in range(x,y+1):
        rs = rs+i 
        print(rs)
    return rs

mysum(1,6)
# %% def 作業

def ftoc(f_temp):
    c_temp = float((f_temp-32)*5 / 9)
    print("華氏"+str(f_temp)+"度"+"攝氏"+str(c_temp)+"度")

ftoc(100)