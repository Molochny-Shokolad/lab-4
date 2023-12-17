import psycopg2
from vk_api.longpoll import VkLongPoll, VkEventType

# Подключение к базе данных
conn = psycopg2.connect(dbname='your_database', user='your_user', password='your_password', host='your_host', port='your_port')
cur = conn.cursor()

# Настройка VK API
# (Вам нужно установить библиотеку vk_api)
import vk_api
vk_session = vk_api.VkApi(token='your_vk_token')
longpoll = VkLongPoll(vk_session)

# Обработка событий
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        # Получение данных о сообщении
        user_id = event.user_id
        message_text = event.text

        # Вставка данных в базу данных
        insert_query = "INSERT INTO messages (user_id, message_text) VALUES (%s, %s);"
        data = (user_id, message_text)
        cur.execute(insert_query, data)
        conn.commit()

# Закрытие соединения с базой данных
cur.close()
conn.close()
