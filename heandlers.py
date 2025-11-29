from aiogram import Router,F
from aiogram.types import Message
from aiogram.filters import Command
from config import menu_btn,start_train
router = Router()
@router.message(Command('start'))
async def command(message:Message):
    user = message.from_user.username
    await message.answer(f'Привет {user}\n🏋Вас приветствует бот личный фитнес-тренер\nВыберите из меню что вы желаете:',reply_markup=menu_btn)
@router.message(Command('help'))
async def commanand_help(message:Message):
    await message.answer(f'🛠 Чтобы связаться с разработчиком пишите на аккаунт @um1dov7, если возникнут проблемы')
@router.message(Command('about'))
async def command_about(message:Message):
    await message.answer('''Этот бот поможет тебе:

📅 Создать персональный план тренировок по дням недели

💪 Получать пошаговые упражнения для разных групп мышц

🥗 Узнать, сколько калорий тебе нужно и как питаться правильно

🔥 Следить за прогрессом и мотивировать тебя каждый день''')



