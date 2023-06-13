import json
from datetime import datetime
import paho.mqtt.client as mqtt
import pymysql

# MQTT 連接設定 雲端上broker = localhost
mqtt_broker = '34.68.187.213' 
mqtt_topic = 'dog/#'

# Google Cloud SQL 連接設定
db_host = '34.133.22.97'
db_user = 'user1'
db_password = '1234'
db_database = 'dog'

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")
    client.subscribe(mqtt_topic)

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    json_data = json.loads(msg.payload)
    device_id = json_data['device_id']
    dog_name = json_data['dog_name']
    date_time = json_data['date_time']
    connection = pymysql.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_database
    )

    cursor = connection.cursor()

    sql = "INSERT INTO dog.dog (device_id, dog_name, date_time) VALUES (%s, %s, %s)"
    values = (device_id, dog_name, date_time)

    cursor.execute(sql, values)

    connection.commit()

    cursor.close()
    connection.close()

# 連接到 MQTT 伺服器
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(mqtt_broker, 1883, 60)

# 持續接收 MQTT 訊息
client.loop_forever()

