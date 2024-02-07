def build_vip_homework(): 
    
    import csv
    id, name, tel, choose = [], [], [], 'y'
    
    while True:
        
        if choose == 'y':
            id.append(input("Enter your ID : "))
            name.append(input("Enter your name : "))
            tel.append(input("Enter your tel : "))
            choose = input("Continue a next data? y/n ")
        elif choose == 'n':
            break                   
        else:
            choose = input("Continue a next data? y/n ")
            
    import csv
    path = 'C:/Users/notel/Desktop/data_file.csv'
    with open(path,'w',newline='') as data_file:
        writer = csv.writer(data_file)
        writer.writerow(['ID','Name','Phone','\n'])
        
        for a in range(len(id)):  
            #Write data
            writer.writerow([id[a],name[a],tel[a],'\n'])
    print('Welcome to use again.')  #作業