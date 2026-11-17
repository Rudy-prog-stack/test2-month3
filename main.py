import asyncio 
import logging

from config import bot, dp 
from handlers import commands, echo
from database import db
from handlers import fsm_add_book

async def main():

    dp.include_router(router=commands.router_commands)
    dp.include_router(router=fsm_add_book.router_add_book)
    dp.include_router(router=echo.router_echo)

    await db.init_db()  
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
