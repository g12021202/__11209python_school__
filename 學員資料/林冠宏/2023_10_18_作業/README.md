2023.10.18作業  
建立一個台積電的資料庫#在資料庫內建立資料表  
將台積電.csv整理為json格式  
把json格式的資料進入資料表 

python套件需求
- yfinance  
- csv  
- json  
- sqlite3  

[data.py](./data.py)
```
import yfinance as yf
import csv
import json

data = yf.download("2330.TW", start = '2023-01-01')
data.to_csv('tsmc.csv')

def make_json(csvFilePath, jsonFilePath):
    data_dict = {}
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
             
            key = rows['Date']
            data_dict[key] = rows
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        # 寫入資料：json.dump(資料, 檔案物件)
        jsonf.write(json.dumps(data_dict, indent=4))

csvFilePath = r'tsmc.csv'
jsonFilePath = r'tsmc.json'
 
make_json(csvFilePath, jsonFilePath)
```

[main.py](./main.py)
```
# 參考 https://yhhuang1966.blogspot.com/2018/04/python-sqlite_28.html 
import sqlite3
import json

def create_table(conn):
    # 呼叫 conn.cursor() 建立 Cursor 物件
    cursor = conn.cursor()
    # 呼叫 cursor.execute() 執行 CREATE 操作
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS 台積電 (
            "id"    INTEGER NOT NULL,
            "日期"	INTEGER NOT NULL,
            "開市"	INTEGER NOT NULL,
            "最高"	INTEGER NOT NULL,
            "最低"	INTEGER NOT NULL,
            "收市"	INTEGER NOT NULL,
            "經調整收市價"	INTEGER NOT NULL,
            "成交量"	INTEGER,
            PRIMARY KEY("id" AUTOINCREMENT)
        );
        '''
    )
    conn.commit()
def insert_data(conn,values):
    cursor = conn.cursor()
    sql = '''
        INSERT INTO 台積電 (日期, 開市, 最高, 最低, 收市, 經調整收市價, 成交量)
        VALUES(?,?,?,?,?,?,?)
        '''
    # 傳回 Cursor 物件
    cursor.execute(sql, values)
    # 寫回資料庫
    conn.commit()
# 連接資料庫檔案
conn = sqlite3.connect("stock.db")
create_table(conn)
# 寫回資料庫
conn.commit()

with open("tsmc.json",mode="r") as file:
    data = json.load(file)
    for item in data:
        insert_data(conn,(item[0], item[1], item[2], item[3], item[4], item[5], item[6]))
```