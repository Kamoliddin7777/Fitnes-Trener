from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

nutrition = Router()

# Машина состояний (FSM)
class NutritionForm(StatesGroup):
    weight = State()
    height = State()
    age = State()
    gender = State()
    activity = State()
    goal = State()

# Старт: пользователь нажимает кнопку "🥗Питание"
@nutrition.message(F.text == '🥗Питание')
async def start_nutrition(message: Message, state: FSMContext):
    await state.set_state(NutritionForm.weight)
    await message.answer("Введите ваш вес (в кг):")

# Вес
@nutrition.message(NutritionForm.weight)
async def process_weight(message: Message, state: FSMContext):
    await state.update_data(weight=float(message.text))
    await state.set_state(NutritionForm.height)
    await message.answer("Введите ваш рост (в см):")

# Рост
@nutrition.message(NutritionForm.height)
async def process_height(message: Message, state: FSMContext):
    await state.update_data(height=float(message.text))
    await state.set_state(NutritionForm.age)
    await message.answer("Введите ваш возраст:")

# Возраст
@nutrition.message(NutritionForm.age)
async def process_age(message: Message, state: FSMContext):
    await state.update_data(age=int(message.text))
    await state.set_state(NutritionForm.gender)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="👨 Мужчина", callback_data="male"),
         InlineKeyboardButton(text="👩 Женщина", callback_data="female")]
    ])
    await message.answer("Выберите ваш пол:", reply_markup=keyboard)

# Пол
@nutrition.callback_query(F.data.in_({"male", "female"}))
async def process_gender(callback, state: FSMContext):
    await state.update_data(gender=callback.data)
    await state.set_state(NutritionForm.activity)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🛋️ Минимальная", callback_data="1")],
        [InlineKeyboardButton(text="🚶 Лёгкая (1–2 раза/нед)", callback_data="2")],
        [InlineKeyboardButton(text="🏋 Средняя (3–4 раза)", callback_data="3")],
        [InlineKeyboardButton(text="⚡ Высокая (5–6 раз)", callback_data="4")],
        [InlineKeyboardButton(text="🔥 Очень высокая", callback_data="5")]
    ])
    await callback.message.edit_text("Выберите уровень активности:", reply_markup=keyboard)

# Активность
@nutrition.callback_query(F.data.in_({"1", "2", "3", "4", "5"}))
async def process_activity(callback, state: FSMContext):
    await state.update_data(activity=int(callback.data))
    await state.set_state(NutritionForm.goal)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🏋️ Набор массы", callback_data="gain")],
        [InlineKeyboardButton(text="⚖️ Похудение", callback_data="lose")],
        [InlineKeyboardButton(text="🍎 Поддержание", callback_data="maintain")]
    ])
    await callback.message.edit_text("Какая у вас цель?", reply_markup=keyboard)

# Цель — и финальный расчёт
@nutrition.callback_query(F.data.in_({"gain", "lose", "maintain"}))
async def finish_nutrition(callback, state: FSMContext):
    data = await state.get_data()
    data["goal"] = callback.data

    result = calculate_calories(
        weight=data["weight"],
        height=data["height"],
        age=data["age"],
        gender=data["gender"],
        activity_level=data["activity"],
        goal=data["goal"]
    )

    text = (
        f"🔥 Ваша норма калорий:\n\n"
        f"• BMR (базовый обмен): {result['BMR']} ккал\n"
        f"• TDEE (с активностью): {result['TDEE']} ккал\n\n"
        f"🎯 Для вашей цели ({'набор массы' if data['goal']=='gain' else 'похудение' if data['goal']=='lose' else 'поддержание'}):\n"
        f"➡️ {result['recommended_calories']} ккал в день\n"
        f'Вот вам инструкция как считать калорий:\nhttps://youtu.be/O5ARgecKV0w'
    )

    await callback.message.edit_text(text)
    await state.clear()


# 📊 Формула расчёта калорий
def calculate_calories(weight, height, age, gender, activity_level, goal):
    if gender == 'male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    activity_map = {1: 1.2, 2: 1.375, 3: 1.55, 4: 1.725, 5: 1.9}
    tdee = bmr * activity_map.get(activity_level, 1.2)

    if goal == 'gain':
        calories = tdee * 1.15
    elif goal == 'lose':
        calories = tdee * 0.85
    else:
        calories = tdee
    return {"BMR": round(bmr), "TDEE": round(tdee), "recommended_calories": round(calories)}
