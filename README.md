# 搜狗Search_Dog-中原浪浪AI辨識追蹤系統

以LineBot串接雲端及邊緣運算的方式，達到 AIoT、行動化技術，進行校狗的辨識及追蹤，並推廣動服社活動，協助狗狗們找到一個家。

- AI影像辨識模型

以Yolo系列模型進行模型訓練及調用

- AIoT應用

將模型轉檔導入邊緣運算裝置Jetson nano
使用MQTT協定將辨識資料存入DB
建構MySQL資料庫

- LineBot

以Cloud Run及Compute Engine部屬程式
