# 參考 https://yhhuang1966.blogspot.com/2018/04/python-sqlite_28.html 
import sqlite3
import json

def create_table(conn):
    # 呼叫 conn.cursor() 建立 Cursor 物件
    cursor = conn.cursor()
    # 呼叫 cursor.execute() 執行 CRUD 操作 ， 新增、修改、刪除、查詢 ( CRUD )
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
        # print(type(item))
        insert_data(conn,(item[0], item[1], item[2], item[3], item[4], item[5], item[6]))
        # insert_data(conn,(item['Date'], item['Open'], item['High'], item['Low'], item['Close'], item['Adj Close'], item['Volume']))