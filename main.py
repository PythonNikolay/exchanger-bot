import logging, asyncio, os
from aiogram import Bot, Dispatcher, F
from core.handlers.basic import get_start, get_currency_today, get_help
from core.utils.commands import set_commands
from core.handlers import form
from core.utils.statesform import StepsMilesKm, StepsKmMiles, StepsKgLbs, StepsLbsKg, StepsCF, StepsFC
from aiogram.client.bot import DefaultBotProperties

bot_token = os.getenv('BOT_TOKEN')
admin_id = os.getenv('ADMIN_ID')
log_level = os.getenv('LOG_LEVEL')

logging.basicConfig(level=log_level,
    format="%(asctime)s - [%(levelname)s] - %(name)s - "
    "(%(filename)s) .%(funcName)s(%(lineno)d) - %(message) s")

default_bot_properties = DefaultBotProperties(parse_mode='HTML')

async def start_bot(bot: Bot):
  await set_commands(bot)
  await bot.send_message(admin_id, text='Bot has been started!')
async def stop_bot(bot: Bot):
  await bot.send_message(admin_id, text='Bot has been stopped!')


async def start():
  bot = Bot(token=bot_token, default=default_bot_properties)
  dp = Dispatcher()
  dp.message.register(get_currency_today, F.text.lower().startswith('currency exchange rates'))

  dp.message.register(form.get_miles, F.text.lower().startswith('miles to km'))
  dp.message.register(form.get_miles_result, StepsMilesKm.GET_MILES)

  dp.message.register(form.get_km, F.text.lower().startswith('km to miles'))
  dp.message.register(form.get_km_result, StepsKmMiles.GET_KM)

  dp.message.register(form.get_lbs, F.text.lower().startswith('lbs to kg'))
  dp.message.register(form.get_lbs_result, StepsLbsKg.GET_LBS)

  dp.message.register(form.get_kg, F.text.lower().startswith('kg to lbs'))
  dp.message.register(form.get_kg_result, StepsKgLbs.GET_KG)

  dp.message.register(form.get_fahrenheit, F.text.lower().startswith('°f to °c'))
  dp.message.register(form.get_fahrenheit_result, StepsFC.GET_F)

  dp.message.register(form.get_celsius, F.text.lower().startswith('°c to °f'))
  dp.message.register(form.get_celsius_result, StepsCF.GET_C)

  dp.message.register(get_start, F.text.lower().startswith('/start'))
  dp.message.register(get_start, F.text.lower().startswith('/restart'))
  dp.message.register(get_help, F.text.lower().startswith('/help'))

  dp.startup.register(start_bot)
  dp.shutdown.register(stop_bot)


  try:
    await dp.start_polling(bot)
  finally:
    await bot.session.close()

if __name__ == '__main__':
  asyncio.run(start())




