from aiogram.utils import executor
from config import dp
from handlers import start,update_product, callback, delete_product
from database import sql_commands

start.register_start_handler(dp=dp)
update_product.register_update_product_handler(dp=dp)
callback.register_handlers_callback(dp=dp)
delete_product.register_handlers_delete(dp=dp)

async def on_startup(_):
    db = sql_commands.Database()
    db.sql_create_db()
    print("bot is ready")

if __name__ == "__main__":
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=on_startup,
                           )