from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message
from config import bot


router_commands = Router()

@router_commands.message(Command('start'))
async def start_handler(message: Message):
    await message.answer('Здравствуйте!')

    await bot.send_message(chat_id=message.chat.id, 
                           text=f'Привет! {message.from_user.full_name} \nТвой телеграм ID > {message.from_user.id}')

