import aiosqlite
from database import queries


path_db = 'database/sqlite3.db'

async def init_db():
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(queries.create_books_table)
        await conn.execute(queries.create_books_details_table)
        await conn.commit()
