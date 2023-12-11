import requests
import sqlite3
import datetime
__all__ = ['update_sqlite_data']
def download_air_data()->list[dict]:
    '''
    下載 
    https://data.moenv.gov.tw/swagger/#/%E5%A4%A7%E6%B0%A3/get_aqx_p_07
    curl -X GET "https://data.moenv.gov.tw/api/v2/aqx_p_07?api_key=cbb6f9c0-9c3b-4086-b464-80594cd61f78" -H "accept: */*"
    '''
    air_url = 'https://data.moenv.gov.tw/api/v2/aqx_p_07?api_key=1f7402cf-f22f-4253-95d7-02821ce4bf65'
    response = requests.get(air_url)
    response.raise_for_status()
    print("下載成功")
    return response.json()

def __create_table(conn:sqlite3.Connection):
    cursor = conn.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS 空氣品質監測站基本資料 (
            "id" INTEGER,
            "測站名稱"	TEXT,
            "測站英文名稱"	TEXT NOT NULL,
            "空品區"	TEXT NOT NULL,
            "城市"	TEXT NOT NULL,
            "鄉鎮"	TEXT NOT NULL,
            "測站地址"	TEXT,
            "經度" INTEGER,
            "緯度" INTEGER,
            "測站類型"	TEXT NOT NULL,
            "測站編號" INTEGER,
            "更新時間" DATETIME NOT NULL,
            PRIMARY KEY("id" AUTOINCREMENT),
            UNIQUE(測站名稱,更新時間) ON CONFLICT REPLACE
        );
        '''
    )
    conn.commit()

def __insert_data(conn:sqlite3.Connection, VALUES: list[any]) -> None:
    cursor = conn.cursor()
    cursor_time = datetime.datetime.utcnow()
    sql = '''
    REPLACE INTO 空氣品質監測站基本資料 (測站名稱, 測站英文名稱, 空品區, 城市, 鄉鎮, 測站地址, 經度, 緯度, 測站類型, 測站編號, 更新時間)
    VALUES(?,?,?,?,?,?,?,?,?,?,?)
    '''
    VALUES.append(cursor_time)
    cursor.execute(sql, VALUES)
    conn.commit()

def update_sqlite_data():
    '''
    下載,並更新資料庫
    '''
    data = download_air_data()
    conn = sqlite3.connect("air.db")
    __create_table(conn)
    for item in data["records"]:
        __insert_data(conn,[item['sitename'],item['siteengname'],item['areaname'],item['county'],item['township'],item['siteaddress'],item['twd97lon'],item['twd97lat'],item['sitetype'],item['siteid']])
    conn.close()