# library
import csv

# 開啟 CSV 檔案
with open('sample_input.csv', newline='') as csvFile:
    
    # 3.轉成一個 dictionary, 讀取 CSV 檔內容，將每一列轉成字典
    rows = csv.DictReader(csvFile)
    
    
    
    max=[-1.0, -1.0, -1.0, -1.0, -1.0]
    min=[100.0, 100.0, 100.0, 100.0, 100.0]
    # 迴圈輸出 指定欄位
    for row in rows:
        if row['WDSD'] == '-99.000' or row['WDSD'] == '-999.000':
            row.clear()
        else:
            
            # print(row['station_id'],row['WDSD'])
            if row['station_id'] == 'C0A880':
                if float(row['WDSD']) > max[0]:
                    max[0] = float(row['WDSD'])
                if float(row['WDSD']) < min[0] and float(row['WDSD'])>=0:
                    min[0] = float(row['WDSD'])
            if row['station_id'] == 'C0F9A0':
                #print(row['station_id'],row['WDSD'])
                if float(row['WDSD']) > max[1]:
                    max[1] = float(row['WDSD'])
                if float(row['WDSD']) < min[1] and float(row['WDSD'])>=0:
                    min[1] = float(row['WDSD'])
            if row['station_id'] == 'C0G640':
                #print(row['station_id'],row['WDSD'])
                if float(row['WDSD']) > max[2]:
                    max[2] = float(row['WDSD'])
                if float(row['WDSD']) < min[2] and float(row['WDSD'])>=0:
                    min[2] = float(row['WDSD'])
            if row['station_id'] == 'C0R190':
                #print(row['station_id'],row['WDSD'])
                if float(row['WDSD']) > max[3]:
                    max[3] = float(row['WDSD'])
                if float(row['WDSD']) < min[3] and float(row['WDSD'])>=0:
                    min[3] = float(row['WDSD'])
if row['station_id'] == 'C0X260':
    #print(row['station_id'],row['WDSD'])
    if float(row['WDSD']) > max[4]:
        max[4] = float(row['WDSD'])
            if float(row['WDSD']) < min[4] and float(row['WDSD'])>=0:
                min[4] = float(row['WDSD'])



rng=[]
i=0
    while i<5:
        if max[i]>0 and min[i]<100 and max[i]!=min[i]:
            rng.append(round(max[i]-min[i], 1))
        else:
            rng.append('None')
        #print("rng:",rng[i])
        i+=1

a=[['C0A880', rng[0]], [['C0F9A0'], rng[1]], [['C0G640'], rng[2]], [['C0R190'], rng[3]], [['C0X260'], rng[4]]]
print(a)


