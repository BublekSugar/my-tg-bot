import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiohttp import web # Добавили библиотеку для работы с портом 8000

T = '8482191197:AAGt7k7zOWOeQdUoZjX1JToFqPOyogsErJw'
I = 1187723773

b = Bot(token=T)
d = Dispatcher()

# Функция, которая говорит Koyeb "Я живой!", если тот постучится на порт 8000
async def handle(request):
    return web.Response(text="Bot is active")

@d.message(Command("start"))
async def start_cmd(m: types.Message):
    await m.answer("привет, в своем сообщении укажи свой юзернейм чтобы я смог тебе ответить")

@d.message()
async def h(m: types.Message):
    if m.from_user.id != I:
        # Логика с юзернеймом, которую ты просил
        user_info = f"@{m.from_user.username}" if m.from_user.username else f"ID: {m.from_user.id}"
        await b.send_message(I, f"Сообщение от {user_info}:\n{m.text}")
        await m.answer("Отправлено!")

async def main():
    # Настройка мини-сервера для порта 8000
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8000) # Слушаем тот самый порт 8000
    
    # Запускаем бота и сервер одновременно
    await asyncio.gather(d.start_polling(b), site.start())

if __name__ == '__main__':
    asyncio.run(main())
