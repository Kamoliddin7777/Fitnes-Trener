from aiogram import Bot,Dispatcher
import os
from dotenv import load_dotenv
import asyncio
from heandlers import router
from train import train
from mitivation import motivation
from training_plan import train_plan
from nutrition import nutrition
load_dotenv()
async def main():
    token = os.getenv('TOKEN')
    bot = Bot(token)
    dp = Dispatcher()
    dp.include_router(router)
    dp.include_router(train)
    dp.include_router(motivation)
    dp.include_router(train_plan)
    dp.include_router(nutrition)

    await dp.start_polling(bot)


if __name__=='__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот завершил работу')



