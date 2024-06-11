str1 = '美元(USD) 美元(USD)'

str2 = str1.replace('美元','')

list1 = str2.split()
str3 = ','.join(list1)

print(str3[0:5])