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