from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

c1 = KeyboardButton('1๐ญ')
c2 = KeyboardButton('2๐ญ')
c3 = KeyboardButton('3๐ญ')
c4 = KeyboardButton('4๐ญ')
c5 = KeyboardButton('5๐ญ')
c6 = KeyboardButton('6๐ญ')
c7 = KeyboardButton('7๐ญ')
c8 = KeyboardButton('8๐ญ')


btnReload = KeyboardButton('ะกัะณัะฐัั ัะฝะพะฒะฐ')
btnEndGame = KeyboardButton('๐ ะััะพะด ๐ญ')


kb_candy = ReplyKeyboardMarkup(resize_keyboard=True)
kb_candy.row(c1, c2, c3, c4). row(c5, c6, c7, c8).row(btnEndGame)

kb_konfeta_end = ReplyKeyboardMarkup(resize_keyboard=True)
kb_konfeta_end.add(btnReload).add(btnEndGame)