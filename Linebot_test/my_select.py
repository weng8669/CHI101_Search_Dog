import pymysql

def get_device_id(dog_name):
    # 建立資料庫連線
    connection = pymysql.connect(
        host='34.133.22.97',
        user='user1',
        password='1234',
        database='dog'
    )

    try:
        # 建立游標物件
        cursor = connection.cursor()

        # 執行查詢
        sql = "SELECT device_id, date_time FROM dog.dog WHERE dog_name = %s AND date_time = (SELECT MAX(date_time) FROM dog.dog WHERE dog_name = %s)"
        cursor.execute(sql, (dog_name, dog_name))

        # 取得查詢結果
        result = cursor.fetchone()

        # 如果有查詢結果，取得 device_id
        device_id = result[0] if result else None
        date_time = result[1] if result else None
        return device_id, date_time

    finally:
        # 關閉游標
        cursor.close()

        # 關閉資料庫連線
        connection.close()

