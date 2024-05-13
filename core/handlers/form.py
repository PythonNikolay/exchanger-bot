from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.utils.statesform import StepsMilesKm, StepsKmMiles, StepsLbsKg, StepsKgLbs, StepsCF, StepsFC, StepsOzMl, StepsMlOz

async def convert_units(message: Message, state: FSMContext, source_unit: str, target_unit: str, conversion_factor: float, offset: float = 0):
    try:
        value = float(message.text.replace(',', '.'))
    except ValueError:
        await message.answer("<b>Error: please enter number(s) only!</b>")
        await state.clear()
        return

    result = round(value * conversion_factor + offset, 1)
    await message.answer(f'{value} {source_unit} is {result} {target_unit}')
    await state.clear()

# Miles to KM
async def get_miles(message: Message, state: FSMContext):
    await message.answer(f'Please enter mile(s):')
    await state.set_state(StepsMilesKm.GET_MILES)

async def get_miles_result(message: Message, state: FSMContext):
    await convert_units(message, state, 'miles', 'km', 1.60934)

# KM to Miles
async def get_km(message: Message, state: FSMContext):
    await message.answer(f'Please enter kilometer(s):')
    await state.set_state(StepsKmMiles.GET_KM)

async def get_km_result(message: Message, state: FSMContext):
    await convert_units(message, state, 'km', 'miles', 0.621371)

# Pounds to KG
async def get_lbs(message: Message, state: FSMContext):
    await message.answer(f'Please enter pound(s):')
    await state.set_state(StepsLbsKg.GET_LBS)

async def get_lbs_result(message: Message, state: FSMContext):
    await convert_units(message, state, 'lbs', 'kg', 0.453592)

# KG to Pounds
async def get_kg(message: Message, state: FSMContext):
    await message.answer(f'Please enter killogram(s):')
    await state.set_state(StepsKgLbs.GET_KG)

async def get_kg_result(message: Message, state: FSMContext):
    await convert_units(message, state, 'kg', 'lbs', 2.20462)

# Celsius to Fahrenheit
async def get_celsius(message: Message, state: FSMContext):
    await message.answer(f'Please enter celsius degree(s):')
    await state.set_state(StepsCF.GET_C)

async def get_celsius_result(message: Message, state: FSMContext):
    await convert_units(message, state, '°C', '°F', 1.8, 32)

# Fahrenheit to Celsius
async def get_fahrenheit(message: Message, state: FSMContext):
    await message.answer(f'Please enter fahrenheit degree(s):')
    await state.set_state(StepsFC.GET_F)

async def get_fahrenheit_result(message: Message, state: FSMContext):
    value = message.text.replace(',', '.')
    if value.replace('.', '').isdigit():
        result_f = round((float(value) - 32) * 5/9, 1)
        await message.answer(f'{value} °F is {result_f} °C')
        await state.clear()
    else:
        await message.answer("<b>Error: please enter number(s) only!</b>")
        await state.clear()

# Fl oz to Ml
async def get_oz(message: Message, state: FSMContext):
    await message.answer(f'Please enter ounce(s):')
    await state.set_state(StepsOzMl.GET_OZ)

async def get_oz_result(message: Message, state: FSMContext):
    await convert_units(message, state, 'oz', 'ml', 29.5735)

# Ml to Fl oz
async def get_ml(message: Message, state: FSMContext):
    await message.answer(f'Please enter milliliter(s):')
    await state.set_state(StepsMlOz.GET_ML)

async def get_ml_result(message: Message, state: FSMContext):
    await convert_units(message, state, 'ml', 'oz', 0.033814)