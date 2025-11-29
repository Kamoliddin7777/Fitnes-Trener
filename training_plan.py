from aiogram import Router,F
from aiogram.types import Message,InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery
train_plan = Router()
days = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Понедельник', callback_data='monday'),
        InlineKeyboardButton(text='Вторник', callback_data='tuesday')
    ],
    [
        InlineKeyboardButton(text='Среда', callback_data='wednesday'),
        InlineKeyboardButton(text='Четверг', callback_data='thursday')
    ],
    [
        InlineKeyboardButton(text='Пятница', callback_data='friday'),
        InlineKeyboardButton(text='Суббота', callback_data='saturday')
    ],
    [
        InlineKeyboardButton(text='Воскресенье', callback_data='sunday')
    ]
])
user_days = {}
@train_plan.callback_query(F.data.in_({'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'}))
async def handle_days(callback:CallbackQuery):
    user_id = callback.from_user.id
    day_map = {
        'monday': 'Понедельник',
        'tuesday': 'Вторник',
        'wednesday': 'Среда',
        'thursday': 'Четверг',
        'friday': 'Пятница',
        'saturday': 'Суббота',
        'sunday': 'Воскресенье'
    }

    day = day_map[callback.data]
    if user_id not in user_days:
        user_days[user_id]=[]
    if day in user_days[user_id]:
        await callback.answer(f'⚠ {day} уже выбран!', show_alert=True)
        return
    user_days[user_id].append(day)
    if len(user_days[user_id])==4:
        selected_days = "\n".join(f"• {day}" for day in user_days[user_id])

        await callback.message.edit_text(f'📅 Вы выбрали 4 дня:\n{selected_days}')
        await callback.message.answer(f'Вот вам план тренровки\n{user_days[user_id][0]}:🦵Ноги&Плечи \n{user_days[user_id][1]}:🔥Грудь&Трицепс\n{user_days[user_id][2]}:💪Спина&Бицепс\n{user_days[user_id][3]}:🏃Кардио')
@train_plan.message(F.text == '📅План тренировки')
async def show_plan(message: Message):
    await message.answer('Веберите 4 свободных дней для тренировки',reply_markup=days)




