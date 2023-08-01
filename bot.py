from aiogram import Bot, Dispatcher
from aiogram.types import Message

from config_data.config import load_config, Config

config: Config = load_config()

bot = Bot(token=config.bot_token)
dp: Dispatcher = Dispatcher()


@dp.message()
async def echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text='Тип не поддерживается')


if __name__ == '__main__':
    dp.run_polling(bot)
