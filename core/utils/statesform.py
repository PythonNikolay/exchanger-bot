from aiogram.fsm.state import StatesGroup, State


class StepsMilesKm(StatesGroup):
  GET_MILES = State()

class StepsKmMiles(StatesGroup):
  GET_KM = State()

class StepsLbsKg(StatesGroup):
  GET_LBS = State()

class StepsKgLbs(StatesGroup):
  GET_KG = State()

class StepsFC(StatesGroup):
  GET_F = State()

class StepsCF(StatesGroup):
  GET_C = State()

class StepsOzMl(StatesGroup):
  GET_OZ = State()

class StepsMlOz(StatesGroup):
  GET_ML = State()