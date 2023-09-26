from aiogram import  types, Dispatcher
from config import  bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import  admin
from database.sql_commands import Database
from datetime import datetime, timedelta

async def secret_word(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton(
        "product_list",
        callback_data="list_of_products"
    )
    markup.add(button_call_1)
    if message.from_user.id == 1036061654 :
        await message.reply("ehalo boss, Ehaloooooooo!!!",
                            reply_markup=markup) #является кнопкой (список пользователей) у сообщения
def register_handlers_delete(dp: Dispatcher):
    dp.register_message_handler(secret_word, lambda word: "go" in word.text)