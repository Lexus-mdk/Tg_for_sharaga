from config import telegram_token
from api import get_schedule_from_api
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text


bot = Bot(token=telegram_token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ["Shedule"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer("Действия", reply_markup=keyboard)


@dp.message_handler(Text(equals="Shedule"))
async def get_all_news(message: types.Message):
    get_schedule_from_api('101', 'Вторник')


if __name__ == '__main__':
    executor.start_polling(dp)