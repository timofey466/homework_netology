from aiogram import types
from aiogram.dispatcher import FSMContext
from data.config import admins
from keyboards.default.cb import back, question_list, adminback, new_adminback
from keyboards.inline.callback_data import by_callback
from loader import dp, bot
from states.sleep_state import get_message
from utils.misc import rate_limit

user_text = []
user_chat_id = []
photo_user = []
photo_chat = []


@rate_limit(limit=5)
@dp.message_handler(commands=['start'])
async def started(message: types.Message):
    await message.reply(
        "Привет!\nДля начала, хотим сказать спасибо за выбор нашего магазина. Это нас очень вдохновляет.\nА еще для "
        "нас важно твое впечатление о нашей продукции.\nПоэтому мы дарим 150 RUB за отзыв о каждом заказанном "
        "продукте магазина SHBNV, оставленный на Wildberries.\nКлассно, правда?\nЕсли ты вдруг уже оставил (-а) свой "
        "отзыв, то наш денежный бонус все равно к тебе прилетит😉\n1.  Пришли цифру 1, если уже оставил (-а) "
        "отзыв\n2.  Пришли цифру 2, чтобы узнать условия получения бонуса\n3.  Пришли цифру 3, если возник вопрос / "
        "проблема",
        reply_markup=question_list)


@rate_limit(limit=5)
@dp.message_handler(text='1.оставил (-а) отзыв')
async def qrcode(message: types.Message, state: FSMContext):
    await message.answer("В Личном кабинете на сайте WB все оставленные отзывы можно найти в разделе \"Профиль\" - "
                         "\"Отзывы и вопросы\".",
                         reply_markup=new_adminback)
    await get_message.photo_admin_wait.set()
    async with state.proxy() as proxy:
        file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
        if len(message.text) > 0:
            photo_chat.append(message.chat.id)
            photo_user.append(message.text)


@rate_limit(limit=5)
@dp.message_handler(text='2.узнать условия получения бонуса')
async def knowbone(message: types.Message):
    await message.answer(
        "Для того, чтобы получить свой денежный бонус, тебе нужно оставить отзыв.\nРасскажи, что тебе понравилось в "
        "SHBNV: продукт, упаковка, сервис, доставка.\nПрикрепи фото (это по желанию, но нам будет приятно).\n\nСледуй "
        "по пунктам, и у тебя все получится 🤍:\n\n1️⃣ Зайди в Личный кабинет\n2️⃣ Найди раздел “Покупки”\n3️⃣ Выбери "
        "товар SHBNV, который ты приобрел(-а).\n4️⃣ Кликни на “Отзыв”, далее – “Оставить отзыв”\n5️⃣ Напиши, "
        "чем тебе понравился наш бренд\n6️⃣ Кликни “Опубликовать отзыв”\n7️⃣ Сделай скриншот готового отзыва и "
        "прикрепи в наш чат-бот\n❗️Чтобы вернуться в начало, отправь \"Назад\"", reply_markup=back)


@rate_limit(limit=5)
@dp.message_handler(text='3.возник вопрос / проблема')
async def error_helps(message: types.Message):
    await message.answer(
        "Опиши проблему, которая у тебя возникла. Менеджер SHBNV тебе поможет и ответит на все твои вопросы.\n❗️Чтобы "
        "вернуться в начало, отправь \"Назад\"", reply_markup=adminback)
    await get_message.wait.set()


@dp.message_handler(state=get_message.wait)
async def error_helps(message: types.Message, state: FSMContext):
    async with state.proxy() as proxy:
        user_text.append(message.text)
        user_chat_id.append(message.chat.id)
    await state.finish()


@rate_limit(limit=5)
@dp.message_handler(text="Назад")
async def backdoor(message: types.Message):
    await message.reply(
        "Привет!\nДля начала, хотим сказать спасибо за выбор нашего магазина. Это нас очень вдохновляет.\nА еще для "
        "нас важно твое впечатление о нашей продукции.\nПоэтому мы дарим 150 RUB за отзыв о каждом заказанном "
        "продукте магазина SHBNV, оставленный на Wildberries.\nКлассно, правда?\nЕсли ты вдруг уже оставил (-а) свой "
        "отзыв, то наш денежный бонус все равно к тебе прилетит😉\n1.  Пришли цифру 1, если уже оставил (-а) "
        "отзыв\n2.  Пришли цифру 2, чтобы узнать условия получения бонуса\n3.  Пришли цифру 3, если возник вопрос / "
        "проблема",
        reply_markup=question_list)


@rate_limit(limit=5)
@dp.message_handler(text="Ответить")
async def error_helps(message: types.Message, state: FSMContext):
    try:
        if message.from_user.id in admins:
            for i1 in user_text:
                for i2 in user_chat_id:
                    await message.reply(i1)
                    async with state.proxy() as proxy:
                        await bot.send_message(chat_id=i2, text=f'{message.text}')
                        user_text.remove(i1)
                        user_chat_id.remove(i2)
        elif message.from_user.id not in admins:
            await message.reply("Эта кнопка только для администраторов.Вы не имеете доступа к этой кнопке")
    except Exception as eror:
        await message.reply("Проблем нет")
        print(eror)


@rate_limit(limit=5)
@dp.message_handler(text="Получить скрин")
async def error_helps(message: types.Message, state: FSMContext):
    try:
        if message.from_user.id in admins:
            global file_info
            await bot.send_photo(chat_id=message.chat.id, photo=file_info)
            for i1 in user_text:
                for i2 in user_chat_id:
                    await message.reply(i1)
                    async with state.proxy() as proxy:
                        await bot.send_message(chat_id=i2, text=f'{message.text}')
                        user_text.remove(i1)
                        user_chat_id.remove(i2)
        elif message.from_user.id not in admins:
            await message.reply("Эта кнопка только для администраторов.Вы не имеете доступа к этой кнопке")
    except Exception as eror:
        await message.reply("Скринов нет")
        print(eror)
