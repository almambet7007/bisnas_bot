from aiogram import types,Dispatcher
from database.sql_commands import  Database
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton

async def list_of_product(call: types.CallbackQuery):
   users = Database().sql_select_product_table()
   print(users)
   print(str(users))
   data = []
   for user in users:
       if not user["name"]:
          data.append("not information")
       else:
           data.append(user[""])

   data = '\n'.join(data)
   await call.message.reply(data)

def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(list_of_product, lambda call: call.data == "list_of_products")