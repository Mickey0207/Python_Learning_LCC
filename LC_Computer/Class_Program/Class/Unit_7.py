#%% for迴圈內積計算
import numpy as np
import time

vec_len = 100000
w = np.random.rand(vec_len)
x = np.random.rand(vec_len)
now = time.time()

c = 0 
for i in range(vec_len):
    c += w[i]*x[i]      #c = c+內積

over = time.time()
print("for花費時間",1000*(over - now))
print(now,over)

#%% 內積計算
import numpy as np
vec_len = 100000
w = np.random.rand(vec_len)
x = np.random.rand(vec_len)

now1 = time.time()
c1 = np.dot(w,x)
over1 = time.time()
print('np內積時間',1000*(over1-now1))

#%% 字典練習
menu = {'雞腿飯':100,'排骨麵':90,'餛飩麵':80}
print(menu['雞腿飯'])

fruits = {'apple':90,'orange':55,'banana':60}
print(fruits['orange'])
print(fruits.get('melon',200))  #get('索引值',傳回預設值)

fruits['melon'] = 50        #字典加值
print(fruits)

fruits.update({'apple':100,'orange':65})    #字典更新
print(fruits)

new_fruits = fruits.copy()  #字典複製
print(new_fruits)

del(new_fruits['orange'])   #字典元素刪除
print(new_fruits)

new_fruits.clear()      #清空字典
print(new_fruits)

del new_fruits      #刪除字典

print(list(fruits.keys()))  #印出字典索引值
print(list(fruits.values()))  #印出字典值

a = []
for i,j in tra_dict.items():    #字典轉串列
    #print(i,j,end=',')
    a.append(i)
    a.append(j)
print(a)
print(type(a))

#%% 作業
tra_dict = {}
while True:
    name = input('請輸入名字')
    location = input('請輸入地點')
    tra_dict[name] = location
    en = input('請問要繼續輸入嗎?')
    if en == 'n':
        break
for i,j in tra_dict.items():
    print(i,j,end=',')