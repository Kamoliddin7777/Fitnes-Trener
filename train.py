from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from config import menu_btn, start_train, start_process,triseps_next,biseps_next,legs_next,cardio_finish

train = Router()
user_progress = {}
plans = [
        {
            "name": "Жим штангой лежа",
            "sets": 4,
            "reps": "8–12 повторений",
            "rest": "40 секунд",
            "video": "https://www.youtube.com/shorts/jWdzYreqKLc"
        },
        {
            "name": "Гантели на наклоне",
            "sets": 3,
            "reps": "8-10 повторений",
            "rest": "60 секунд",
            "video": "https://www.youtube.com/shorts/o0M00osJgRU?feature=share"
        },
        {
            "name": "Жим узким хватом",
            "sets": 3,
            "reps": "8-10 повторений",
            "rest": "60 секунд",
            "video": "https://www.youtube.com/shorts/gjjUI8dsOAs?feature=share"
        },
        {
            "name": "Трицепс косичка",
            "sets": 3,
            "reps": "10–12 повторений",
            "rest": "60 секунд",
            "video": "https://www.youtube.com/shorts/XarMK6Gp930?feature=share"
        }
    ]
plans_for_biseps = [{
    "name": "Подтягивание",
    "sets": 3,
    "reps": "Максимум повторений",
    "rest": "40 секунд",
    "video": "https://www.youtube.com/shorts/ysowB11xYVc?feature=share"
},
    {
        "name": "Тяга вертикального блока",
        "sets": 3,
        "reps": "8-10 повторений",
        "rest": "60 секунд",
        "video": "https://www.youtube.com/shorts/o0M00osJgRU?feature=share"
    },
    {
        "name": "Тяга горизантального блока",
        "sets": 3,
        "reps": "8-10 повторений",
        "rest": "60 секунд",
        "video": "https://youtu.be/hUV6XDtNTLU"
    },
    {
        "name": "Бицепс EZ штагой",
        "sets": 3,
        "reps": "10–12 повторений",
        "rest": "60 секунд",
        "video": "https://www.youtube.com/shorts/9cJPHyzMkCQ?feature=share"
    },
    {
        "name": "Бицепс с гантелями сидя",
        "sets": 3,
        "reps": "12 повторений",
        "rest": "60 секунд",
        "video": "https://www.youtube.com/shorts/92GLb1CAvIc?feature=share"
    },
    {
        "name": "Сгибание на скамье скотта",
        "sets": 3,
        "reps": "12 повторений",
        "rest": "60 секунд",
        "video": "https://www.youtube.com/shorts/dtmECpSY3fI?feature=share"
    }
]
plan_for_leg = [
{
    "name": "Присед со штангой",
    "sets": 5,
    "reps": "10",
    "rest": "60 секунд",
    "video": "https://www.youtube.com/shorts/Iw5oDuAQhdE?feature=share"
},
    {
        "name": "Жим ногами",
        "sets": 4,
        "reps": "10-12 повторений",
        "rest": "60 секунд",
        "video": "https://www.youtube.com/shorts/b6DQ3lADYac?feature=share"
    },
    {
        "name": "Махи в сторону с гантелями",
        "sets": 3,
        "reps": "8-10 повторений",
        "rest": "60 секунд",
        "video": "https://www.youtube.com/shorts/o5G87yvbqIQ?feature=share"
    },
    {
        "name": "Сгибание в тренажоре",
        "sets": 3,
        "reps": "10 повторений",
        "rest": "60 секунд",
        "video": "https://www.youtube.com/shorts/3I4U-OpDd_s?feature=share"
    },
    {
        "name": "Разгибание в тренажоре",
        "sets": 3,
        "reps": "10 повторений",
        "rest": "60 секунд",
        "video": "https://www.youtube.com/shorts/bRsUaHc6g50?feature=share"
    },
    {
        "name": "Махи в наклоне",
        "sets": 3,
        "reps": "10 повторений",
        "rest": "60 секунд",
        "video": "https://www.youtube.com/shorts/F8wdZx3yyPg?feature=share"
    }
]
@train.message(F.text == '🏋️‍Начать тренировку')
async def start_training(message: Message):
    await message.answer(
        'До начала тренеровки сделайте разминку как в этом видео\nhttps://www.youtube.com/shorts/4uxICP0RM8Y?feature=share',
        reply_markup=start_process)


@train.message(F.text == '🚀Начать процесс тренировки')
async def start_process_training(message: Message):
    await message.answer('🛠Выберите тип тренеровки,который хотите выполнить:', reply_markup=start_train)


@train.message(F.text == '🔥Грудь&Трицепс')
async def triseps_plan(message: Message):
    user_id = message.from_user.id
    user_progress[user_id] = 0
    plan = plans[0]
    await message.answer(
        f'📌Название упражнения: {plan["name"]}\n'
        f'📊Подходов: {plan["sets"]}\n'
        f'🔁Повторений: {plan["reps"]}\n'
        f'⏱Отдых: {plan["rest"]}\n'
        f'🎥Техника выполнения: {plan["video"]}')
    await message.answer('!💧 Напоминание: не забывайте пить воду между подходами!',reply_markup=triseps_next)

@train.message(F.text == '➡  Следующее упражнение на 💪 Грудь&Трицепс')
async def next_tricseps(message:Message):
    user_id = message.from_user.id

    if user_id not in user_progress:
        await message.answer('Сначала начни тренеровку командой 🔥Грудь&Трицепс')
        return
    user_progress[user_id] += 1
    index = user_progress[user_id]
    if index<len(plans):
        plan = plans[index]
        await message.answer(
            f'📌 Название упражнения: {plan["name"]}\n'
            f'📊 Подходов: {plan["sets"]}\n'
            f'🔁 Повторений: {plan["reps"]}\n'
            f'⏱ Отдых: {plan["rest"]}\n'
            f'🎥 Видео: {plan["video"]}',
            reply_markup=triseps_next
        )
        await message.answer('💧 Пей воду и готовься к следующему подходу!')
    else:
        await message.answer('🎉 Тренировка завершена! Отличная работа! 💪',reply_markup=menu_btn)
        user_progress.pop(user_id, None)

@train.message(F.text == '💪Спина&Бицепс')
async def train_for_biseps(message:Message):
    user_id = message.from_user.id
    user_progress[user_id] = 0
    plan = plans_for_biseps[0]
    await message.answer(
        f'📌Название упражнения: {plan["name"]}\n'
        f'📊Подходов: {plan["sets"]}\n'
        f'🔁Повторений: {plan["reps"]}\n'
        f'⏱Отдых: {plan["rest"]}\n'
        f'🎥Техника выполнения: {plan["video"]}')
    await message.answer('!💧 Напоминание: не забывайте пить воду между подходами!', reply_markup=biseps_next)

@train.message(F.text == '➡️Следующее упражнение на 💪Спина&Бицепс')
async def next_biseps(message:Message):
    user_id = message.from_user.id

    if user_id not in user_progress:
        await message.answer('Сначала начни тренеровку командой 💪Спина&Бицепс')
        return
    user_progress[user_id] += 1
    index = user_progress[user_id]
    if index < len(plans_for_biseps):
        plan = plans_for_biseps[index]
        await message.answer(
            f'📌 Название упражнения: {plan["name"]}\n'
            f'📊 Подходов: {plan["sets"]}\n'
            f'🔁 Повторений: {plan["reps"]}\n'
            f'⏱ Отдых: {plan["rest"]}\n'
            f'🎥 Видео: {plan["video"]}',
            reply_markup=biseps_next
        )
        await message.answer('💧 Пей воду и готовься к следующему подходу!')
    else:
        await message.answer('🎉 Тренировка завершена! Отличная работа! 💪', reply_markup=menu_btn)
        user_progress.pop(user_id, None)
@train.message(F.text == '🦵Ноги&Плечи')
async def leg_plan(message: Message):
    user_id = message.from_user.id
    user_progress[user_id] = 0
    plan = plan_for_leg[0]
    await message.answer(
        f'📌Название упражнения: {plan["name"]}\n'
        f'📊Подходов: {plan["sets"]}\n'
        f'🔁Повторений: {plan["reps"]}\n'
        f'⏱Отдых: {plan["rest"]}\n'
        f'🎥Техника выполнения: {plan["video"]}')
    await message.answer('!💧 Напоминание: не забывайте пить воду между подходами!',reply_markup=legs_next)
@train.message(F.text == '➡️Следующее упражнение на 🦵Ноги&Плечи')
async def next_legs(message:Message):
    user_id = message.from_user.id

    if user_id not in user_progress:
        await message.answer('Сначала начни тренеровку командой 🦵Ноги&Плечи')
        return
    user_progress[user_id] += 1
    index = user_progress[user_id]
    if index < len(plan_for_leg):
        plan = plan_for_leg[index]
        await message.answer(
            f'📌 Название упражнения: {plan["name"]}\n'
            f'📊 Подходов: {plan["sets"]}\n'
            f'🔁 Повторений: {plan["reps"]}\n'
            f'⏱ Отдых: {plan["rest"]}\n'
            f'🎥 Видео: {plan["video"]}',
            reply_markup=legs_next
        )
        await message.answer('💧 Пей воду и готовься к следующему подходу!')
    else:
        await message.answer('🎉 Тренировка завершена! Отличная работа! 💪', reply_markup=menu_btn)

@train.message(F.text == '🏃Кардио')
async def cardio_plan(message: Message):
    await message.answer('Сделай тренеровку на кардио как в этом видео\nhttps://youtu.be/-hSma-BRzoo',reply_markup=cardio_finish)
@train.message(F.text == 'Завершить тренеровку на кардио')
async def next_legs(message:Message):
    await message.answer('🎉 Тренировка завершена! Отличная работа! 💪', reply_markup=menu_btn)