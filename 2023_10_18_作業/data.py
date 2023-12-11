#建立一個台積電的資料庫#在資料庫內建立資料表
#將台積電.csv整理為json格式
#把json格式的資料進入資料表

import yfinance as yf
import csv
import json
# 語法是 yf.download(股票代號, start=開始日期, end=完結日期)
data = yf.download("2330.TW", start = '2023-01-01')
data.to_csv('tsmc.csv')

# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath):
     
    # create a dictionary  
    data_dict = {}
     
    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
         
        # Convert each row into a dictionary and add it to data
        for rows in csvReader:
             
            # Add this python dict to json array
            key = rows['Date']
            data_dict[key] = rows
 
    # Open a json writer, and use the json.dumps() function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        # 寫入資料：json.dump(資料, 檔案物件)
        jsonf.write(json.dumps(data_dict, indent=4))
 
# Decide the two file paths according to your 
# computer system
csvFilePath = r'tsmc.csv'
jsonFilePath = r'tsmc.json'
 
# Call the make_json function
make_json(csvFilePath, jsonFilePath)