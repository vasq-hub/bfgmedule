from aiogram import Dispatcher, types
from assets.antispam import antispam

@antispam
async def bot_reply(message: types.Message):
    if message.text.lower() == "бот":
        await message.reply("✅На месте! 😊")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(bot_reply, lambda message: message.text.lower() == "бот")

MODULE_DESCRIPTION = {
    'name': '✅ На месте',
    'description': 'Бот отвечает "На месте", когда его зовут'
}
