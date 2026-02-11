import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

T = '8482191197:AAGt7k7zOWOeQdUoZjX1JToFqPOyogsErJw'
I = 1187723773

b = Bot(token=T)
d = Dispatcher()

# 1. Обработка команды /start
@d.message(Command("start"))
async def start_cmd(m: types.Message):
    await m.answer("привет, в своем сообщении укажи свой юзернейм чтобы я смог тебе ответить")

# 2. Пересылка всех остальных сообщений
@d.message()
async def h(m: types.Message):
    if m.from_user.id != I:
        await b.send_message(I, f"Сообщение от {m.from_user.id}:\n{m.text}")
        await m.answer("Отправлено!")

async def main():
    await d.start_polling(b)

if __name__ == '__main__':
    asyncio.run(main())
