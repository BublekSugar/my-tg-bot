import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiohttp import web

T = '8482191197:AAGt7k7zOWOeQdUoZjX1JToFqPOyogsErJw'
I = 1187723773

b = Bot(token=T)
d = Dispatcher()

async def handle(request):
    return web.Response(text="Bot is active")

@d.message(Command("start"))
async def start_cmd(m: types.Message):
    # Добавили уведомление для тебя при нажатии /start
    user_info = f"@{m.from_user.username}" if m.from_user.username else f"ID: {m.from_user.id}"
    if m.from_user.id != I:
        await b.send_message(I, f"Пользователь {user_info} запустил бота!")
    
    await m.answer("жду сообщение...")

@d.message()
async def h(m: types.Message):
    if m.from_user.id != I:
        user_info = f"@{m.from_user.username}" if m.from_user.username else f"ID: {m.from_user.id}"
        await b.send_message(I, f"Сообщение от {user_info}:\n{m.text}")
        await m.answer("Отправлено!")

async def main():
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8000)
    
    await asyncio.gather(d.start_polling(b), site.start())

if __name__ == '__main__':
    asyncio.run(main())
    
