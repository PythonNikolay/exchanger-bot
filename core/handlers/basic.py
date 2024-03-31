from aiogram import Bot
from aiogram.types import Message
from core.keyboards.reply import get_reply_keyboard
from core.function.rate import get_exchange_rate
from datetime import datetime

async def get_start(message: Message, bot: Bot):
  await bot.send_message(message.from_user.id, f'Hi, <b>{message.from_user.first_name}</b>! How can I help you?',
                         reply_markup=get_reply_keyboard())


async def get_currency_today(message: Message):
    exchange_rate_usd_rub = await get_exchange_rate('USD', 'RUB')
    exchange_rate_usd_uzs = await get_exchange_rate('USD', 'UZS')
    current_date = datetime.now().strftime('%d/%m/%Y')
    if exchange_rate_usd_rub is not None or exchange_rate_usd_uzs is not None:
      await message.answer(f'Сurrency rate on <b>{current_date}</b> is:\r\n\r\n'
                          f'1 USD 🇺🇸 =      {exchange_rate_usd_rub} RUB 🇷🇺\r\n'
                          f'1 USD 🇺🇸 = {exchange_rate_usd_uzs} SOM 🇺🇿', reply_markup=get_reply_keyboard())
    else:
      await message.answer('<b>Error: something went wrong!</b>', reply_markup=get_reply_keyboard())


async def get_help(message: Message):
  await message.answer(f"Hi! {message.from_user.first_name} I'm a bot assistant! \r\n" \
                       f'I can convert values and find out exchange rates!')
