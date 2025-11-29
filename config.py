from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menu_btn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='🏋️‍Начать тренировку'),KeyboardButton(text='🥗Питание')],
        [KeyboardButton(text='📅План тренировки'),KeyboardButton(text='🔥Мотивация')]
    ],
    resize_keyboard=True,one_time_keyboard=True
)
start_train = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='🔥Грудь&Трицепс'),KeyboardButton(text='💪Спина&Бицепс')],
        [KeyboardButton(text='🦵Ноги&Плечи'),KeyboardButton(text='🏃Кардио')]
    ],resize_keyboard=True,one_time_keyboard=True
)
start_process = ReplyKeyboardMarkup(
    keyboard=[
    [KeyboardButton(text='🚀Начать процесс тренировки')]
    ],resize_keyboard=True,one_time_keyboard=True
)
triseps_next = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='➡  Следующее упражнение на 💪 Грудь&Трицепс')]
    ],resize_keyboard=True,one_time_keyboard=True
)
biseps_next = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='➡️Следующее упражнение на 💪Спина&Бицепс')]
    ],resize_keyboard=True,one_time_keyboard=True
)
legs_next = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='➡️Следующее упражнение на 🦵Ноги&Плечи')]
    ],resize_keyboard=True,one_time_keyboard=True
)
cardio_finish = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Завершить тренеровку на кардио')]
    ],resize_keyboard=True,one_time_keyboard=True
)




