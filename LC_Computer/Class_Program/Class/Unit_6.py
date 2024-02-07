#%%
a = [1,2,3,4,5]
b = [6,7,8]
a.extend(b)
a.insert(2,9)
a.pop(4)           #依照索引值去除元素
a.remove(3)        #依照元素的值去除物件
print(a)

#%% 
import timeit
list_test = timeit.timeit(stmt = "[1,2,3,4,5]", number = 10000000)
tuple_test = timeit.timeit(stmt = "(1,2,3,4,5)", number = 10000000)
print("list time is", list_test)
print("tuple time is", tuple_test)
# %% numpy試驗
import numpy as np
a = np.array([4,5,6])
b = np.array((1,2,3))
a[0] = 12
b[0] = 7
print(a)
print(b)
print(type(a))
print(type(b))

#%% numpy產生隨機數
n = 10
w = np.random.rand(n)
print(w)
wi = np.random.randint(1,50,size=6)
print(wi)
w2 = np.arange(1.3,10.8,3) #在設定範圍內依照特定間距產生樣本
print(w2)
w3 = np.linspace(1,50,6) #在設定範圍內隨機產生特定個數樣本
print(w3)

#%%
print(np.arange(10))        #整數數列
print(np.arange(3,10))      #可以指定起頭的數列
print(np.arange(1,100,6))   #可以指定間隔
#%% linespace 線性空間的等差數列
x = np.linspace(1,100)
x1 = np.linspace(1,100,10)
print(x)
print(x1)

#%% 索引取值
fruits = np.array(["apple","orange","grape"])
print(fruits[-1])
print(fruits[0:2])

#%% 陣列運算
# np可與原生串列作各種不同的運算
a = np.array([1,2,3])
b = np.array([4,5,6])
c = []
fruits = np.array(['apple','orange','grape'])
for i in range(len(fruits)):
    l = len(fruits[i])
    c.append(l)
result = a + b
print(result)
result1 = a + b + c
print(result,c)

# %% 內積
a = np.array([1,2,3])
b = np.array([4,5,6])

print(np.dot(a,b))