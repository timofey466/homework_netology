from random import randrange
import sqlalchemy
from vk_info import city, age, title, best_family, gender, vk_id
from sqlalchemy_ import People
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

token = input('Token: ')

vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)
Dns = 'postgresql://postgres:adminglocalhost:5432/postgres'
engine = sqlalchemy.create_engine(Dns)


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': randrange(10 ** 7)})


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:
            request = event.text

            if request == "привет":
                write_msg(event.user_id, f"Хай, {event.user_id} Это чат бот сделаный на основе Tinder")
                write_msg(event.user_id, "чтобы начать знакомство напишите Начать")

            elif len(title) == 0:
                write_msg(event.from_user, "Чтобы начать работу напишите своё имя ")

            elif len(best_family) == 0:
                write_msg(event.from_user, "Чтобы начать работу напишите своё семейное положение")

            elif len(age) == 0:
                write_msg(event.from_user, "Чтобы начать работу напишите свой возраст")

            elif len(gender) == 0:
                write_msg(event.from_user, "Чтобы продолжить работу напишите свой пол")

            elif len(city) == 0:
                write_msg(event.user_id, "Чтобы Начать работу напишите название своего города")

            with engine.connect() as connection:
                result = connection.execute(f"SELECT id FROM people WHERE big_city == {city}")
                title_result = connection.execute(f"SELECT name, vk FROM people WHERE id == {result}")
                write_msg(event.user_id, f"Под ваши параметры подходит {title_result}")
                write_msg(event.user_id, f"ссылка на страницу пользователя: https://vk.com/id{vk}")
                black_list_id = []
                black_list_id.append(People.vk)

                if request.lower() == "повторный поиск":
                    result = connection.execute(f"SELECT id FROM people WHERE big_city == {city}")
                    title_result = connection.execute(f"SELECT name, vk FROM people WHERE id == {result}")
                    write_msg(event.user_id, f"Под ваши параметры подходит {title_result}")
                    write_msg(event.user_id, f"ссылка на страницу пользователя: https://vk.com/id{People.vk}")
                    black_list_id = []
                    black_list_id.append(People.vk)





