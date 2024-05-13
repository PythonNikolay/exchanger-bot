from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_reply_keyboard():
  keyboard_builder = ReplyKeyboardBuilder()
  keyboard_builder.button(text='Currency exchange rates')
  keyboard_builder.button(text='Miles to Km')
  keyboard_builder.button(text='Km to Miles')
  keyboard_builder.button(text='Lbs to Kg')
  keyboard_builder.button(text='Kg to Lbs')
  keyboard_builder.button(text='Fl oz to Ml')
  keyboard_builder.button(text='Ml to Fl oz')
  keyboard_builder.button(text='°F to °C')
  keyboard_builder.button(text='°C to °F')
  keyboard_builder.adjust(1, 2, 2, 2)
  return keyboard_builder.as_markup(resize_keyboard='True', one_time_keyboard='False',
                                    input_field_placeholder='Main menu')


