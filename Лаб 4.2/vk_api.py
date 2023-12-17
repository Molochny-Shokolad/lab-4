import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import spacy

# Загрузка NLP модели spaCy
nlp = spacy.load("en_core_web_sm")

def write_msg(user_id, message):
    vk_session.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': 0})

# Авторизация в ВКонтакте
token = ''
vk_session = vk_api.VkApi(token=token)
#vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
# Обработка сообщений

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        text = event.text
        print(text)
        # Применение NLP модели для обработки текста
        doc = nlp(text)
        # Получение ответа на основе анализа текста
        response = "Привет! Я бот. Вы сказали: " + text
