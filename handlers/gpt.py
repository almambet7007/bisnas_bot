from aiogram import types, Dispatcher
from database.sql_commands import Database
import openai

async def gpt_bot(message: types.Message):
    is_aunteticate = Database().sql_select_fsm_table()
    for i in is_aunteticate:
        if message.from_user.id in i:
            is_aunteticate=True
            break

    if is_aunteticate==True:

        openai.api_key = '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'

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[],
            temperature=0.8,
            max_tokens=256
        )
        await message.answer(response['choices'][0]['text'])
    else:
        await message.answer(message.text)

def register_gpt_messages(dp: Dispatcher):
    dp.register_message_handler(gpt_bot)