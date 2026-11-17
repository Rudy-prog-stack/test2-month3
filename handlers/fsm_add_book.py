from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

class Addbook(StatesGroup):
    number = State()
    name = State()
    author = State()
    janre = State()

router_add_book = Router()


@router_add_book.message(Command('add_book'))
async def add_start_fsm(message: Message, state: FSMContext):
    await message.answer('Введите номер книги:')
    if not message.text.isdigit():
        await message.answer('Введите номер книги (только цифры):')
        return
    await state.set_state(Addbook.number)


@router_add_book.message(Addbook.number)
async def add_name(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    await message.answer('Введите название книги:')
    await state.set_state(Addbook.name)


@router_add_book.message(Addbook.name)
async def add_author(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Введите имя автора:')
    await state.set_state(Addbook.author)


@router_add_book.message(Addbook.author)
async def add_janre(message: Message, state: FSMContext):
    await state.update_data(author=message.text)
    await message.answer('Введите жанр книги:')
    await message.answer('Конец')

    await state.clear()

