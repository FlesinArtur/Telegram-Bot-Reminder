from aiogram import Bot, Dispatcher, executor, types

from secret import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
bot_dispatcher = Dispatcher(bot=bot)


@bot_dispatcher.message_handler(commands=['start'])
async def hello_message(message: types.Message):
    await bot.send_message(message.from_user.id, 'Hello, I`am Bot-Reminder')


if __name__ == '__main__':
    executor.start_polling(bot_dispatcher)
