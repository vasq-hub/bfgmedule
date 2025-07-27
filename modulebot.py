from aiogram import Dispatcher, types
from assets.antispam import antispam

@antispam
async def bot_reply(message: types.Message):
    if message.text.lower() in ("бот", "bot"):
        await message.reply("✅ На месте! 😊")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(bot_reply, lambda m: m.text and m.text.lower() in ("бот", "bot"))

MODULE_DESCRIPTION = {
    'name': '✅ Ответ на вызов',
    'description': 'Отвечает "На месте", когда пользователь пишет "бот"'
}
