from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from  aiogram.types import ContentType, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters.state import State, StatesGroup
from database.sql_commands import Database
from config import bot
from handlers.start import start_markup

class ProductState(StatesGroup):
    title = State()
    count = State()
    description = State()
    price = State()
    photo = State()

async def product_start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = types.KeyboardButton("Update Product")
    markup.add(item)
    await message.reply("Enter product title", reply_markup=start_markup)
    await ProductState.title.set()
async def load_title(message: types.Message,
                     state: FSMContext):
    async with state.proxy() as data:
        data['title'] = message.text
    await ProductState.next()
    await message.reply("enter product count")


async def load_count(message: types.Message,
                     state: FSMContext):
    async with state.proxy() as data:
        data['count'] = message.text
    await ProductState.next()
    await message.reply("enter product description")


async def load_description(message: types.Message,
                           state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await ProductState.next()
    await message.reply("enter product price")

async def load_price(message: types.Message,
                     state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text
    await ProductState.next()
    await message.reply("enter product photo")

async def load_photo(message: types.Message,
                     state: FSMContext):
    select = Database()
    path = await message.photo[-1].download(
        destination_dir="C:\ACER\PycharmProjects\Month_3_alma_dz\media")
    async  with state.proxy() as data:
        data["photo"] = path.name
        Database().sql_insert_product_table(
            title=data['title'],
            county=data['count'],
            name=message.from_user.username,
            description=data['description'],
            price=data['price'],
            photo=data['photo']
        )

        with open(path.name, 'rb') as photo:
            await bot.send_photo(message.chat.id,
                                 photo=photo,
                                 caption=data)
        await message.reply("finished loading product")
        await state.finish()

    # markup = InlineKeyboardMarkup()
    # button_call_1 = InlineKeyboardButton(
    #     "Update Product",
    #     callback_data="update_product"  # Связываем кнопку с командой "update_product"
    # )
    # markup.add(button_call_1)

def register_update_product_handler(dp: Dispatcher):
    dp.register_message_handler(product_start, commands=["update_product"])
    dp.register_message_handler(load_title, content_types=["text"],
                                state=ProductState.title)
    dp.register_message_handler(load_count, content_types=["text"],
                                state=ProductState.count)
    dp.register_message_handler(load_description, content_types=["text"],
                                state=ProductState.description)
    dp.register_message_handler(load_price, content_types=["text"],
                                state=ProductState.price)
    dp.register_message_handler(load_photo,content_types=ContentType.PHOTO)




    # Затем отправляем эту кнопку в чат
    # dp.register_message_handler(product_start, state="*")  # Регистрируем обработчик для начала
    # dp.register_message_handler(product_start, content_types=types.ContentTypes.TEXT, state="*")  # Регистрируем обработчик для текстовых сообщений



