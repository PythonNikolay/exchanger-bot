from aiogram import Bot
from aiogram.types import Message
from core.keyboards.reply import get_reply_keyboard
from core.function.rate import get_exchange_rate
from datetime import datetime

async def get_start(message: Message, bot: Bot):
    await bot.send_message(
        message.from_user.id,
        f'Hi, <b>{message.from_user.first_name}</b>! How can I help you?',
        reply_markup=get_reply_keyboard()
    )

async def get_currency_today(message: Message):
    exchange_rate_usd_rub = await get_exchange_rate('USD', 'RUB')
    exchange_rate_usd_uzs = await get_exchange_rate('USD', 'UZS')
    exchange_rate_usd_eur = await get_exchange_rate('USD', 'EUR')
    current_date = datetime.now().strftime('%d/%m/%Y')

    if all(rate is not None for rate in [exchange_rate_usd_rub, exchange_rate_usd_uzs, exchange_rate_usd_eur]):
        await message.answer(
            f'Currency rates on <b>{current_date}</b> are:\r\n\r\n'
            f'1 USD 🇺🇸 = {exchange_rate_usd_rub} RUB 🇷🇺\r\n'
            f'1 USD 🇺🇸 = {exchange_rate_usd_uzs} SOM 🇺🇿\r\n'
            f'1 USD 🇺🇸 = {exchange_rate_usd_eur} EUR 🇪🇺',
            reply_markup=get_reply_keyboard()
        )
    else:
        await message.answer('<b>Error: something went wrong while fetching exchange rates!</b>', reply_markup=get_reply_keyboard())

async def get_help(message: Message):
    await message.answer(
        f"Hi, {message.from_user.first_name}! I'm a bot assistant! \r\n"
        f"I can convert values and provide current exchange rates!"
    )
