from aiogram import Dispatcher, types
from assets.antispam import antispam

@antispam
async def bot_reply(message: types.Message):
    if message.text and message.text.lower() in ['бот', 'bot']:
        await message.reply('? На месте! ??')

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(bot_reply, lambda message: message.text and message.text.lower() in ['бот', 'bot'])

MODULE_DESCRIPTION = {
    'name': '? Ответ бота',
    'description': 'Отвечает на слова "бот" и "bot"'
}
