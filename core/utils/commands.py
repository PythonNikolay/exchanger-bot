from aiogram import Bot
from aiogram.types import BotCommand


async def set_commands(bot: Bot):
  commands = [
    BotCommand(
      command='start',
      description='Run bot',
    ),
    BotCommand(
      command='help',
      description='Help'
    ),
    BotCommand(
      command='restart',
      description='Restart bot'
    )
  ]

  await bot.set_my_commands(commands)