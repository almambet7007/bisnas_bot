from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from database.sql_commands import Database
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_button = KeyboardButton("/start")
update_product_button = KeyboardButton("/update_product")


start_markup = ReplyKeyboardMarkup(resize_keyboard= True,one_time_keyboard=True)

start_markup.row(
    start_button,
    update_product_button
)

async def start_button(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = types.KeyboardButton("/start")
    markup.add(item)
    await message.reply("Press /start to begin registration", reply_markup=start_markup)


class Rerister(StatesGroup):
    nickname = State()
    admin_or_sotrudnick = State()

async def fsm_start(message: types.Message):
    await message.reply('Send me your nickname')
    print(message.from_user.id)
    await Rerister.nickname.set()

async def load_nickname(message: types.Message,
                        state: FSMContext):
    async with state.proxy() as data:
        data['nickname'] = message.text
    await Rerister.next()
    await message.reply("send me who are you, if you admin enter password else you sotrudnick")

async def load_admin_or_sot(message: types.Message,
                            state: FSMContext):
    if int(message.text) == 1212:
        async with state.proxy() as data:
            data['admin_or_sotrudnick'] = 1
            await message.reply("you admin")
            await message.reply("registration ended")
            await state.finish()
    else:
        async with state.proxy() as data:
            data['admin_or_sotrudnick'] = 0
            await message.reply("you sotrudnick")
            await message.reply("registration ended")
            await state.finish()
    Database().sql_insert_fsm_table(
        telegram_id=message.from_user.id,
        nickname=data["nickname"],
        admin_or_sot=data["admin_or_sotrudnick"],
    )

def register_start_handler(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands=["start"])
    dp.register_message_handler(load_nickname,
                                content_types=["text"],
                                state=Rerister.nickname)

    dp.register_message_handler(load_admin_or_sot,
                                content_types=["text"],
                                state=Rerister.admin_or_sotrudnick)
