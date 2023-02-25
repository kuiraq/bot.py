import time
import random
import telebot
from telebot import types
points = 0
crct = ['Верно!', 'Молодец, правильно', 'Ответ верен!', 'Правильно, так держать!']
incrct = ['Неверно :(', 'Неправильно, повнимательнее!', 'Ответ неверен, но ничего', 'Эх, неверно...']
pred = ['knife - нож', 'toiletries — туалетные принадлежности', 'wardrobe — шкаф для одежды',
        'cupboard — шкаф, буфет', 'closet — шкаф, кладовка, чулан',
        'cup – чашка', 'fork – вилка', 'spoon – ложка', 'plate – тарелка', 'blanket – одеяло', 'pillow – подушка',
        'pillowcase – наволочка',
        'sheet (bedsheet) – простыня', 'linens — постельное белье',
        'Bathroom — это санузел дома, то есть комната, где совмещены ванная (bathtub) и туалет. Находясь дома, люди '
        'обычно говорят «bathroom», а не другие варианты. Также, если в доме ванная и туалет раздельные, '
        'то bathroom — это ванная комната. '
        '\nToilet — 1) туалет в доме или квартире с раздельными ванной (bathroom) и туалетом (toilet), 2) унитаз.'
        '\nRestroom — общественный туалет. Находясь в общественном месте, обычно говорят '
        '«I need to go to the restroom», а не «bathroom». '
        '\nLavatory — общественный туалет, особенно на самолете.']


bot = telebot.TeleBot('5683702517:AAFWKHLswuuyUkgzjQhtwJZmH35_6QSwpEQ')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <i><b>{message.from_user.first_name}</b></i>! Этот бот создан для того, чтобы помогать изучать ' \
           f'английский'
    mess1 = f'Здесь вы найдете небольшие подсказки и советы для изучения английского'
    mess2 = f'Данный бот нацелен на аудиторию школьников, будем рады помочь'
    mess3 = f'Используйте /help для того, чтобы узнать функции бота'
    bot.reply_to(message, mess, parse_mode='html')
    bot.send_message(message.chat.id, mess1)
    bot.send_message(message.chat.id, mess2)
    bot.send_message(message.chat.id, mess3)


@bot.message_handler(commands=['help'])
def help(message):
    mes = f'/start - Начало работы бота'
    mes1 = f'/study - Лайфхаки, правила по английскому'
    mes2 = '/minigames - Мини-игры'
    bot.send_message(message.chat.id, mes)
    bot.send_message(message.chat.id, mes1)
    bot.send_message(message.chat.id, mes2)


@bot.message_handler(commands=['minigames'])
def minigames(message):
    markup_reply = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    ret_btn = types.KeyboardButton('В начало ↩')
    quiz1 = types.KeyboardButton('Викторина')
    markup_reply.add(quiz1)
    markup_reply.add(ret_btn)
    bot.send_message(message.chat.id, "В этот разделе ты можешь потренировать себя с помощью викторин и небольших игр. "
                                      "В скором времени они будут пополняться 😋", reply_markup=markup_reply)


@bot.message_handler(func=lambda message: message.text == 'Викторина')
def quiz(message):
    global points
    points = 0
    markup_reply = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    answ1 = types.KeyboardButton('is, a')
    answ2 = types.KeyboardButton('are, an')
    answ3 = types.KeyboardButton('is, an')
    answ4 = types.KeyboardButton('are, a')
    markup_reply.add(answ1, answ3)
    markup_reply.add(answ2, answ4)
    bot.send_message(message.chat.id, "<b>1) Выберите верный вариант:</b>"
                                      "\nWhat a wonderful day! Look, there <i>is/are</i> so many birds outside. "
                                      "I want to go to <i>a/an</i> park today.", reply_markup=markup_reply,
                     parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'is, a')
def answer(message):
    bot.send_message(message.chat.id, random.choice(incrct))
    markup_reply = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    answ1 = types.KeyboardButton('out')
    answ2 = types.KeyboardButton('on')
    answ3 = types.KeyboardButton('off')
    answ4 = types.KeyboardButton('in')
    markup_reply.add(answ1, answ3)
    markup_reply.add(answ2, answ4)
    bot.send_message(message.chat.id, "<b>2) Вставьте верное слово:</b>"
                                      "\nHi, Jack! Do you want to hang _ with me tonight?", reply_markup=markup_reply,
                     parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'are, an')
def answer(message):
    bot.send_message(message.chat.id, random.choice(incrct))
    markup_reply = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    answ1 = types.KeyboardButton('out')
    answ2 = types.KeyboardButton('on')
    answ3 = types.KeyboardButton('off')
    answ4 = types.KeyboardButton('in')
    markup_reply.add(answ1, answ3)
    markup_reply.add(answ2, answ4)
    bot.send_message(message.chat.id, "<b>2) Вставьте верное слово:</b>"
                                      "\nHi, Jack! Do you want to hang _ with me tonight?", reply_markup=markup_reply,
                     parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'is, an')
def answer(message):
    bot.send_message(message.chat.id, random.choice(incrct))
    markup_reply = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    answ1 = types.KeyboardButton('out')
    answ2 = types.KeyboardButton('on')
    answ3 = types.KeyboardButton('off')
    answ4 = types.KeyboardButton('in')
    markup_reply.add(answ1, answ3)
    markup_reply.add(answ2, answ4)
    bot.send_message(message.chat.id, "<b>2) Вставьте верное слово:</b>"
                                      "\nHi, Jack! Do you want to hang _ with me tonight?", reply_markup=markup_reply,
                     parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'are, a')
def answer(message):
    global points
    bot.send_message(message.chat.id, random.choice(crct))
    points += 1
    markup_reply = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    answ1 = types.KeyboardButton('out')
    answ2 = types.KeyboardButton('on')
    answ3 = types.KeyboardButton('off')
    answ4 = types.KeyboardButton('in')
    markup_reply.add(answ1, answ3)
    markup_reply.add(answ2, answ4)
    bot.send_message(message.chat.id, "<b>2) Вставьте верное слово:</b>"
                                      "\nHi, Jack! Do you want to hang _ with me tonight?", reply_markup=markup_reply,
                     parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'out')
def answer(message):
    global points
    bot.send_message(message.chat.id, random.choice(crct))
    points += 1
    markup_reply = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    answ1 = types.KeyboardButton('have done')
    answ2 = types.KeyboardButton('has did')
    answ3 = types.KeyboardButton('had done')
    answ4 = types.KeyboardButton('had did')
    markup_reply.add(answ1, answ3)
    markup_reply.add(answ2, answ4)
    bot.send_message(message.chat.id, "<b>3) Вставьте нужное время:</b>"
                                      "\nI _ _ my work when he came", reply_markup=markup_reply, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'on')
def answer(message):
    bot.send_message(message.chat.id, random.choice(incrct))
    markup_reply = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    answ1 = types.KeyboardButton('have done')
    answ2 = types.KeyboardButton('has did')
    answ3 = types.KeyboardButton('had done')
    answ4 = types.KeyboardButton('had did')
    markup_reply.add(answ1, answ3)
    markup_reply.add(answ2, answ4)
    bot.send_message(message.chat.id, "<b>3) Вставьте нужное время:</b>"
                                      "\nI _ _ my work when he came", reply_markup=markup_reply, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'off')
def answer(message):
    bot.send_message(message.chat.id, random.choice(incrct))
    markup_reply = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    answ1 = types.KeyboardButton('have done')
    answ2 = types.KeyboardButton('has did')
    answ3 = types.KeyboardButton('had done')
    answ4 = types.KeyboardButton('had did')
    markup_reply.add(answ1, answ3)
    markup_reply.add(answ2, answ4)
    bot.send_message(message.chat.id, "<b>3) Вставьте нужное время:</b>"
                                      "\nI _ _ my work when he came", reply_markup=markup_reply, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'in')
def answer(message):
    bot.send_message(message.chat.id, random.choice(incrct))
    markup_reply = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    answ1 = types.KeyboardButton('have done')
    answ2 = types.KeyboardButton('has did')
    answ3 = types.KeyboardButton('had done')
    answ4 = types.KeyboardButton('had did')
    markup_reply.add(answ1, answ3)
    markup_reply.add(answ2, answ4)
    bot.send_message(message.chat.id, "<b>3) Вставьте нужное время:</b>"
                                      "\nI _ _ my work when he came", reply_markup=markup_reply, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'have done')
def answer(message):
    bot.send_message(message.chat.id, random.choice(incrct))
    markup_reply = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    answ1 = types.KeyboardButton('3')
    answ2 = types.KeyboardButton('24')
    answ3 = types.KeyboardButton('12')
    answ4 = types.KeyboardButton('16')
    markup_reply.add(answ1, answ3)
    markup_reply.add(answ2, answ4)
    bot.send_message(message.chat.id, "<b>4) Ответьте:</b>"
                                      "\nСколько всего времён в английском языке (<i>по классической грамматике</i>)",
                     reply_markup=markup_reply, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'has did')
def answer(message):
    bot.send_message(message.chat.id, random.choice(incrct))
    markup_reply = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    answ1 = types.KeyboardButton('3')
    answ2 = types.KeyboardButton('24')
    answ3 = types.KeyboardButton('12')
    answ4 = types.KeyboardButton('16')
    markup_reply.add(answ1, answ3)
    markup_reply.add(answ2, answ4)
    bot.send_message(message.chat.id, "<b>4) Ответьте:</b>"
                                      "\nСколько всего времён в английском языке (<i>по классической грамматике</i>)",
                     reply_markup=markup_reply, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'had done')
def answer(message):
    global points
    bot.send_message(message.chat.id, random.choice(crct))
    points += 1
    markup_reply = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    answ1 = types.KeyboardButton('3')
    answ2 = types.KeyboardButton('24')
    answ3 = types.KeyboardButton('12')
    answ4 = types.KeyboardButton('16')
    markup_reply.add(answ1, answ3)
    markup_reply.add(answ2, answ4)
    bot.send_message(message.chat.id, "<b>4) Ответьте:</b>"
                                      "\nСколько всего времён в английском языке (<i>по классической грамматике</i>)",
                     reply_markup=markup_reply, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'had did')
def answer(message):
    bot.send_message(message.chat.id, random.choice(incrct))
    markup_reply = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    answ1 = types.KeyboardButton('3')
    answ2 = types.KeyboardButton('24')
    answ3 = types.KeyboardButton('12')
    answ4 = types.KeyboardButton('16')
    markup_reply.add(answ1, answ3)
    markup_reply.add(answ2, answ4)
    bot.send_message(message.chat.id, "<b>4) Ответьте:</b>"
                                      "\nСколько всего времён в английском языке (<i>по классической грамматике</i>)",
                     reply_markup=markup_reply, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == '3')
def answer(message):
    bot.send_message(message.chat.id, random.choice(incrct))
    markup_reply = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    answ1 = types.KeyboardButton('Women, Cats, Oxes')
    answ2 = types.KeyboardButton('Women, Cats, Oxen')
    answ3 = types.KeyboardButton('Womans, Cats, Oxes')
    answ4 = types.KeyboardButton('Womans, Cats, Oxen')
    markup_reply.add(answ1, answ3)
    markup_reply.add(answ2, answ4)
    bot.send_message(message.chat.id, "<b>5) Образуйте множественные числа:</b>"
                                      "\nWoman - ..., Cat - ..., Ox - ... ",
                     reply_markup=markup_reply, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == '24')
def answer(message):
    bot.send_message(message.chat.id, random.choice(incrct))
    markup_reply = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    answ1 = types.KeyboardButton('Women, Cats, Oxes')
    answ2 = types.KeyboardButton('Women, Cats, Oxen')
    answ3 = types.KeyboardButton('Womans, Cats, Oxes')
    answ4 = types.KeyboardButton('Womans, Cats, Oxen')
    markup_reply.add(answ1, answ3)
    markup_reply.add(answ2, answ4)
    bot.send_message(message.chat.id, "<b>5) Образуйте множественные числа:</b>"
                                      "\nWoman - ..., Cat - ..., Ox - ... ",
                     reply_markup=markup_reply, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == '12')
def answer(message):
    global points
    bot.send_message(message.chat.id, random.choice(crct))
    points += 1
    markup_reply = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    answ1 = types.KeyboardButton('Women, Cats, Oxes')
    answ2 = types.KeyboardButton('Women, Cats, Oxen')
    answ3 = types.KeyboardButton('Womans, Cats, Oxes')
    answ4 = types.KeyboardButton('Womans, Cats, Oxen')
    markup_reply.add(answ1, answ3)
    markup_reply.add(answ2, answ4)
    bot.send_message(message.chat.id, "<b>5) Образуйте множественные числа:</b>"
                                      "\nWoman - ..., Cat - ..., Ox - ... ",
                     reply_markup=markup_reply, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == '16')
def answer(message):
    bot.send_message(message.chat.id, random.choice(incrct))
    markup_reply = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    answ1 = types.KeyboardButton('Women, Cats, Oxes')
    answ2 = types.KeyboardButton('Women, Cats, Oxen')
    answ3 = types.KeyboardButton('Womans, Cats, Oxes')
    answ4 = types.KeyboardButton('Womans, Cats, Oxen')
    markup_reply.add(answ1, answ3)
    markup_reply.add(answ2, answ4)
    bot.send_message(message.chat.id, "<b>5) Образуйте множественные числа:</b>"
                                      "\nWoman - ..., Cat - ..., Ox - ... ",
                     reply_markup=markup_reply, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'Women, Cats, Oxes')
def answer(message):
    bot.send_message(message.chat.id, random.choice(incrct))
    markup_reply = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    answ1 = types.KeyboardButton("at 4 o'clock yesterday, the whole day, from 5 till 6")
    answ2 = types.KeyboardButton("by that time, by 5 o'clock, before + Past Simple")
    answ3 = types.KeyboardButton('yesterday, a week ago, last night')
    answ4 = types.KeyboardButton('already, never, ever, just')
    markup_reply.add(answ1, answ3)
    markup_reply.add(answ2, answ4)
    bot.send_message(message.chat.id, "<b>6) Выберите наиболее подходящие маркеры времени <u>Past Simple</u>:</b>",
                     reply_markup=markup_reply, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'Women, Cats, Oxen')
def answer(message):
    global points
    bot.send_message(message.chat.id, random.choice(crct))
    points += 1
    markup_reply = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    answ1 = types.KeyboardButton("at 4 o'clock yesterday, the whole day, from 5 till 6")
    answ2 = types.KeyboardButton("by that time, by 5 o'clock, before + Past Simple")
    answ3 = types.KeyboardButton('yesterday, a week ago, last night')
    answ4 = types.KeyboardButton('already, never, ever, just')
    markup_reply.add(answ1, answ3)
    markup_reply.add(answ2, answ4)
    bot.send_message(message.chat.id, "<b>6) Выберите наиболее подходящие маркеры времени <u>Past Simple</u>:</b>",
                     reply_markup=markup_reply, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'Womans, Cats, Oxes')
def answer(message):
    bot.send_message(message.chat.id, random.choice(incrct))
    markup_reply = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    answ1 = types.KeyboardButton("at 4 o'clock yesterday, the whole day, from 5 till 6")
    answ2 = types.KeyboardButton("by that time, by 5 o'clock, before + Past Simple")
    answ3 = types.KeyboardButton('yesterday, a week ago, last night')
    answ4 = types.KeyboardButton('already, never, ever, just')
    markup_reply.add(answ1, answ3)
    markup_reply.add(answ2, answ4)
    bot.send_message(message.chat.id, "<b>6) Выберите наиболее подходящие маркеры времени <u>Past Simple</u>:</b>",
                     reply_markup=markup_reply, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'Womans, Cats, Oxen')
def answer(message):
    bot.send_message(message.chat.id, random.choice(incrct))
    markup_reply = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    answ1 = types.KeyboardButton("at 4 o'clock yesterday, the whole day, from 5 till 6")
    answ2 = types.KeyboardButton("by that time, by 5 o'clock, before + Past Simple")
    answ3 = types.KeyboardButton('yesterday, a week ago, last night')
    answ4 = types.KeyboardButton('already, never, ever, just')
    markup_reply.add(answ1, answ3)
    markup_reply.add(answ2, answ4)
    bot.send_message(message.chat.id, "<b>6) Выберите наиболее подходящие маркеры времени <u>Past Simple</u>:</b>",
                     reply_markup=markup_reply, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == "at 4 o'clock yesterday, the whole day, from 5 till 6")
def answer(message):
    bot.send_message(message.chat.id, random.choice(incrct))
    markup_reply = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    answ1 = types.KeyboardButton("will be do")
    answ2 = types.KeyboardButton("have been doing")
    answ3 = types.KeyboardButton('was been doing')
    answ4 = types.KeyboardButton('will be doing')
    markup_reply.add(answ1, answ3)
    markup_reply.add(answ2, answ4)
    bot.send_message(message.chat.id, "<b>7) Образуйте время:</b>"
                                      "\nI was doing my makeup at 5 o'clock yesterday. - I _ _ _ my makeup at "
                                      "5 o'clock tomorrow.",
                     reply_markup=markup_reply, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == "by that time, by 5 o'clock, before + Past Simple")
def answer(message):
    bot.send_message(message.chat.id, random.choice(incrct))
    markup_reply = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    answ1 = types.KeyboardButton("will be do")
    answ2 = types.KeyboardButton("have been doing")
    answ3 = types.KeyboardButton('was been doing')
    answ4 = types.KeyboardButton('will be doing')
    markup_reply.add(answ1, answ3)
    markup_reply.add(answ2, answ4)
    bot.send_message(message.chat.id, "<b>7) Образуйте время:</b>"
                                      "\nI was doing my makeup at 5 o'clock yesterday. - I _ _ _ my makeup at "
                                      "5 o'clock tomorrow.",
                     reply_markup=markup_reply, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == "yesterday, a week ago, last night")
def answer(message):
    global points
    bot.send_message(message.chat.id, random.choice(crct))
    points += 1
    markup_reply = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    answ1 = types.KeyboardButton("will be do")
    answ2 = types.KeyboardButton("have been doing")
    answ3 = types.KeyboardButton('was been doing')
    answ4 = types.KeyboardButton('will be doing')
    markup_reply.add(answ1, answ3)
    markup_reply.add(answ2, answ4)
    bot.send_message(message.chat.id, "<b>7) Образуйте время:</b>"
                                      "\nI was doing my makeup at 5 o'clock yesterday. - I _ _ _ my makeup at "
                                      "5 o'clock tomorrow.",
                     reply_markup=markup_reply, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == "already, never, ever, just")
def answer(message):
    bot.send_message(message.chat.id, random.choice(incrct))
    markup_reply = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    answ1 = types.KeyboardButton("will be do")
    answ2 = types.KeyboardButton("have been doing")
    answ3 = types.KeyboardButton('was been doing')
    answ4 = types.KeyboardButton('will be doing')
    markup_reply.add(answ1, answ3)
    markup_reply.add(answ2, answ4)
    bot.send_message(message.chat.id, "<b>7) Образуйте время:</b>"
                                      "\nI was doing my makeup at 5 o'clock yesterday. - I _ _ _ my makeup at "
                                      "5 o'clock tomorrow.",
                     reply_markup=markup_reply, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == "will be do")
def answer(message):
    f = open('time.png', "rb")
    bot.send_message(message.chat.id, random.choice(incrct))
    markup_reply = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    answ1 = types.KeyboardButton("quarter past five")
    answ2 = types.KeyboardButton("quarter to five")
    answ3 = types.KeyboardButton('half past four')
    answ4 = types.KeyboardButton('half to five')
    markup_reply.add(answ1, answ3)
    markup_reply.add(answ2, answ4)
    bot.send_photo(message.chat.id, f)
    bot.send_message(message.chat.id, "<b>8) Сколько времени на часах?:</b>"
                                      "\nIt's...",
                     reply_markup=markup_reply, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == "have been doing")
def answer(message):
    f = open('time.png', "rb")
    bot.send_message(message.chat.id, random.choice(incrct))
    markup_reply = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    answ1 = types.KeyboardButton("quarter past five")
    answ2 = types.KeyboardButton("quarter to five")
    answ3 = types.KeyboardButton('half past four')
    answ4 = types.KeyboardButton('half to five')
    markup_reply.add(answ1, answ3)
    markup_reply.add(answ2, answ4)
    bot.send_photo(message.chat.id, f)
    bot.send_message(message.chat.id, "<b>8) Сколько времени на часах?:</b>"
                                      "\nIt's...",
                     reply_markup=markup_reply, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == "was been doing")
def answer(message):
    f = open('time.png', "rb")
    bot.send_message(message.chat.id, random.choice(incrct))
    markup_reply = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    answ1 = types.KeyboardButton("quarter past five")
    answ2 = types.KeyboardButton("quarter to five")
    answ3 = types.KeyboardButton('half past four')
    answ4 = types.KeyboardButton('half to five')
    markup_reply.add(answ1, answ3)
    markup_reply.add(answ2, answ4)
    bot.send_photo(message.chat.id, f)
    bot.send_message(message.chat.id, "<b>8) Сколько времени на часах?:</b>"
                                      "\nIt's...",
                     reply_markup=markup_reply, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == "will be doing")
def answer(message):
    f = open('time.png', "rb")
    global points
    bot.send_message(message.chat.id, random.choice(crct))
    points += 1
    markup_reply = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    answ1 = types.KeyboardButton("quarter past five")
    answ2 = types.KeyboardButton("quarter to five")
    answ3 = types.KeyboardButton('half past four')
    answ4 = types.KeyboardButton('half to five')
    markup_reply.add(answ1, answ3)
    markup_reply.add(answ2, answ4)
    bot.send_photo(message.chat.id, f)
    bot.send_message(message.chat.id, "<b>8) Сколько времени на часах?:</b>"
                                      "\nIt's...",
                     reply_markup=markup_reply, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == "quarter past five")
def answer(message):
    bot.send_message(message.chat.id, random.choice(incrct))
    markup_reply = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    answ1 = types.KeyboardButton("Надеть")
    answ2 = types.KeyboardButton("Положить")
    answ3 = types.KeyboardButton('Втянуть')
    answ4 = types.KeyboardButton('Ставить')
    markup_reply.add(answ1, answ3)
    markup_reply.add(answ2, answ4)
    bot.send_message(message.chat.id, "<b>9) Переведите фразу 'put on' в контексте:</b>"
                                      "\nDon't <i>put</i> me <i>on</i> this deal",
                     reply_markup=markup_reply, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == "quarter to five")
def answer(message):
    global points
    bot.send_message(message.chat.id, random.choice(crct))
    points += 1
    markup_reply = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    answ1 = types.KeyboardButton("Надеть")
    answ2 = types.KeyboardButton("Положить")
    answ3 = types.KeyboardButton('Втянуть')
    answ4 = types.KeyboardButton('Ставить')
    markup_reply.add(answ1, answ3)
    markup_reply.add(answ2, answ4)
    bot.send_message(message.chat.id, "<b>9) Переведите фразу 'put on' в контексте:</b>"
                                      "\nDon't <i>put</i> me <i>on</i> this deal",
                     reply_markup=markup_reply, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == "half past four")
def answer(message):
    bot.send_message(message.chat.id, random.choice(incrct))
    markup_reply = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    answ1 = types.KeyboardButton("Надеть")
    answ2 = types.KeyboardButton("Положить")
    answ3 = types.KeyboardButton('Втянуть')
    answ4 = types.KeyboardButton('Ставить')
    markup_reply.add(answ1, answ3)
    markup_reply.add(answ2, answ4)
    bot.send_message(message.chat.id, "<b>9) Переведите фразу 'put on' в контексте:</b>"
                                      "\nDon't <i>put</i> me <i>on</i> this deal",
                     reply_markup=markup_reply, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == "half to five")
def answer(message):
    bot.send_message(message.chat.id, random.choice(incrct))
    markup_reply = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    answ1 = types.KeyboardButton("Надеть")
    answ2 = types.KeyboardButton("Положить")
    answ3 = types.KeyboardButton('Втянуть')
    answ4 = types.KeyboardButton('Ставить')
    markup_reply.add(answ1, answ3)
    markup_reply.add(answ2, answ4)
    bot.send_message(message.chat.id, "<b>9) Переведите фразу 'put on' в контексте:</b>"
                                      "\nDon't <i>put</i> me <i>on</i> this deal",
                     reply_markup=markup_reply, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == "Надеть")
def answer(message):
    pr = round(points * 11.1111)
    markup_reply = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    ret_btn = types.KeyboardButton('В начало ↩')
    markup_reply.add(ret_btn)
    bot.send_message(message.chat.id, random.choice(incrct))
    bot.send_message(message.chat.id, f"<b>Викторина окончена:</b>"
                                      f"\nВаш результат - {points} ({pr}%)", reply_markup=markup_reply,
                     parse_mode='html')


@bot.message_handler(func=lambda message: message.text == "Положить")
def answer(message):
    pr = round(points * 11.1111)
    markup_reply = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    ret_btn = types.KeyboardButton('В начало ↩')
    markup_reply.add(ret_btn)
    bot.send_message(message.chat.id, random.choice(incrct))
    bot.send_message(message.chat.id, f"<b>Викторина окончена:</b>"
                                      f"\nВаш результат - {points} ({pr}%)", reply_markup=markup_reply,
                     parse_mode='html')


@bot.message_handler(func=lambda message: message.text == "Втянуть")
def answer(message):
    global points
    markup_reply = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    ret_btn = types.KeyboardButton('В начало ↩')
    markup_reply.add(ret_btn)
    bot.send_message(message.chat.id, random.choice(crct))
    points += 1
    pr = round(points * 11.1111)
    bot.send_message(message.chat.id, f"<b>Викторина окончена:</b>"
                                      f"\nВаш результат - {points} ({pr}%)", reply_markup=markup_reply,
                     parse_mode='html')


@bot.message_handler(func=lambda message: message.text == "Ставить")
def answer(message):
    markup_reply = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    ret_btn = types.KeyboardButton('В начало ↩')
    markup_reply.add(ret_btn)
    pr = round(points * 11.1111)
    bot.send_message(message.chat.id, random.choice(incrct))
    bot.send_message(message.chat.id, f"<b>Викторина окончена:</b>"
                                      f"\nВаш результат - {points} ({pr}%)", reply_markup=markup_reply,
                     parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'В начало ↩')
def func(message):
    help(message)


@bot.message_handler(commands=['study'])
def study_eng(message):
    markup_reply = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    item_rules = types.KeyboardButton(text='Правила английского')
    item_words = types.KeyboardButton(text='Новые слова')
    ret_btn = types.KeyboardButton('В начало ↩')
    markup_reply.add(item_rules, item_words, ret_btn)
    bot.send_message(message.chat.id, 'Давай начнём!', reply_markup=markup_reply)


@bot.message_handler(func=lambda message: message.text == 'Правила английского')
def eng_rules(message):
    markup_reply = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    item_tenses = types.KeyboardButton('Памятка по временам')
    item_gramm = types.KeyboardButton('Важные конструкции')
    ret_back = types.KeyboardButton('Назад ↩')
    markup_reply.row(item_tenses, item_gramm)
    markup_reply.add(ret_back)
    bot.send_message(message.chat.id, 'Что вы хотите изучить?', reply_markup=markup_reply)


@bot.message_handler(func=lambda message: message.text == 'Назад ↩')
def func(message):
    study_eng(message)


@bot.message_handler(func=lambda message: message.text == 'Памятка по временам')
def tenses(message):
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item_tenses1 = types.KeyboardButton('Present')
    item_tenses2 = types.KeyboardButton('Past')
    item_tenses3 = types.KeyboardButton('Future')
    ret_back = types.KeyboardButton('Вернуться назад ↩')
    markup_reply.row(item_tenses1, item_tenses2, item_tenses3)
    markup_reply.row(ret_back)
    bot.send_message(message.chat.id, 'Выберите группу времён', reply_markup=markup_reply)


@bot.message_handler(func=lambda message: message.text == 'Present')
def present(message):
    with open('863d0921cde74032d3660204f46c9b46.jpg', 'rb') as file:
        bot.send_photo(message.chat.id, file)
        bot.send_message(message.chat.id, '<b>Present Simple</b> - действие постоянно, настоящее время'
                                          '\nМаркеры - always, often, usually, never, every day, etc.',
                         parse_mode='html')
        bot.send_message(message.chat.id, '<b>Present Continious</b> - действие в данный момент, сейчас'
                                          '\nИли, если речь о расписании (поезда, встреча сегодня)'
                                          '\nМаркеры - now, at the moment, today, etc.', parse_mode='html')
        bot.send_message(message.chat.id,
                         '<b>Present Perfect</b> - действие произошло в прошлом, но имеет значение в настоящем'
                         '\nМаркеры - already, never, ever, just, yet, etc.', parse_mode='html')
        bot.send_message(message.chat.id,
                         '<b>Present Perfect Continious</b> - действие происходило в течение времени в прошлом, '
                         'но имеет значение в настоящем '
                         '\nМаркеры - since, for', parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'Past')
def past(message):
    with open('58bc9a165abfe2c037fe198ecf035694.jpg', 'rb') as file1:
        bot.send_photo(message.chat.id, file1)
        bot.send_message(message.chat.id, "<b>Past Simple</b> - действие произошло когда-то в прошлом"
                                          "\nМаркеры - yesterday, a week ago, last night, the day before yesterday, "
                                          "etc.",
                         parse_mode='html')
        bot.send_message(message.chat.id, "<b>Past Continious</b> - действие происходило в течение времени в прошлом"
                                          "\nМаркеры - at 4 o'clock yesterday, the whole day, from 5 till 6, "
                                          "when + Past Simple, while, etc.",
                         parse_mode='html')
        bot.send_message(message.chat.id,
                         "<b>Past Perfect</b> - действие случилось до происхождение какого-то момента в прошлом"
                         "\nМаркеры - by that time, by 5 o'clock, before + Past Simple, after, etc.", parse_mode='html')
        bot.send_message(message.chat.id,
                         "<b>Past Perfect Continious</b> - действие случалось какое-то время до происхождение "
                         "какого-то момента в прошлом"
                         "\nМаркеры - since, for a month, a long time, etc.", parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'Future')
def future(message):
    with open('6b295b7916a8165c928ffb69ef00be0c.jpg', 'rb') as file2:
        bot.send_photo(message.chat.id, file2)
        bot.send_message(message.chat.id, '<b>Future Simple</b> - действие произойдёт в будущем '
                                          '\nМаркеры - tomorrow, in the future, soon, next weekend, etc.',
                         parse_mode='html')
        bot.send_message(message.chat.id,
                         '<b>Future Continious</b> - действие будет происходить в течение какого-то времени'
                         '\nМаркеры - all the morning, from 4 till 7, for a week, etc.', parse_mode='html')
        bot.send_message(message.chat.id, "<b>Future Perfect</b> - действие завершится к определённому моменту"
                                          "\nМаркеры - by the time, by 5 o'clock, before, untill/till, etc."
                                          "\n<i>*Часто после Future Perfect идёт <b>Present simple</b> "
                                          "как момент, к которому завершится действие.</i>",
                         parse_mode='html')
        bot.send_message(message.chat.id,
                         "<b>Future Perfect Continious</b> - действие будет длиться какое-то время и "
                         "завершится до момента в будущем"
                         "\nМаркеры - for three years, by the end, etc."
                         "\n<i>*Часто после Future Perfect идёт <b>Present simple</b> как момент, к которому "
                         "завершится действие.</i>",
                         parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'Вернуться назад ↩')
def func(message):
    eng_rules(message)


@bot.message_handler(func=lambda message: message.text == 'Важные конструкции')
def gramm(message):
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    ret_back = types.KeyboardButton('Вернуться назад ↩')
    passvoice_btn = types.KeyboardButton('Passive voice (Пассив. залог)')
    there_btn = types.KeyboardButton('There is/There are')
    art_btn = types.KeyboardButton('Articles')
    part_btn = types.KeyboardButton('Предлоги')
    repsp_btn = types.KeyboardButton('Reported speech (Косв. речь)')
    complx_btn = types.KeyboardButton('Complex object (Сложн. дополн.)')
    stsrav_btn = types.KeyboardButton('Степени сравн. прилагат.')
    plur_btn = types.KeyboardButton('Plural (Множ-е число)')
    ger_btn = types.KeyboardButton('Gerund (Герундий)')
    begointo_btn = types.KeyboardButton('Be going to')
    usedto_btn = types.KeyboardButton('Used to')
    markup_reply.row(passvoice_btn, repsp_btn, there_btn)
    markup_reply.row(complx_btn, stsrav_btn)
    markup_reply.row(ret_back)
    markup_reply.row(part_btn, ger_btn, plur_btn)
    markup_reply.row(art_btn, begointo_btn, usedto_btn)
    bot.send_message(message.chat.id, 'В данном разделе вы можете изучать небольшую теорию по важным конструкциям в'
                                      'английском языке, которые <i>наиболее часто</i> используются.'
                                      '\nВы можете пролистать вниз, если видны не все кнопки',
                     reply_markup=markup_reply, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'Passive voice (Пассив. залог)')
def passive_voice(message):
    f = open('passive_voice.png', 'rb')
    f1 = open('passive_voice2.png', 'rb')
    bot.send_message(message.chat.id, 'В английском языке существует два залога — активный (active voice) и пассивный'
                                      ' или страдательный (passive voice). В активном залоге действие выполняет '
                                      'подлежащее. В пассивном залоге действие происходит над подлежащим.')
    bot.send_photo(message.chat.id, f)
    bot.send_photo(message.chat.id, f1)
    bot.send_message(message.chat.id, "Образование отрицательной формы - частица 'not'. Ставится после вспомогательного"
                                      " глагола. Если их несколько, то после первого "
                                      "\n(I left my camera on the bench and it was not stolen! — Я забыл камеру на "
                                      "лавочке, и ее не украли!)")
    bot.send_message(message.chat.id, "Образование вопроса - вспомогательный глагол на первом месте. "
                                      "Если есть необходимость указать, кем выполняется действие, в конце предложения "
                                      "ставим предлог by + того, кто выполняет действие. "
                                      "(The book was written by an unknown author. — Книга была написана неизвестным "
                                      "автором.)")
    bot.send_message(message.chat.id, "Случаи использования: "
                                      "\n1. Когда тот, кто выполняет действие, неизвестен, неважен или очевиден. "
                                      "Действие важнее того, кто его совершает."
                                      "\n2. Когда описываем действие в новостях, заголовках, рекламных объявлениях "
                                      "(The local shop was robbed this morning. — Местный магазин ограбили этим утром.)"
                                      "\n3. Когда описываем общие факты, идеи, мнения. "
                                      "(Quentin Tarantino is known all around the world. — Квентина Тарантино знают "
                                      "по всему миру.)"
                                      "\n4. Когда хотим сделать высказывание более вежливым или формальным. "
                                      "(The electricity hasn’t been paid for since January. — За электричество не "
                                      "платят с января.)")
    bot.send_message(message.chat.id, "Иные формы passive voice:"
                                      "\n1. ing-форм (Nobody likes being treated badly. — "
                                      "Никому не нравится, когда с ним обращаются плохо.)"
                                      "\n2. Modals (This rule must be taken into consideration. — "
                                      "Это правило должно быть принято во внимание.)"
                                      "\n3. Impersonal construction (It is believed that they are from a "
                                      "very rich family. — Считается, что они из очень богатой семьи.)"
                                      "\nPersonal construction (They were expected to come on Friday. — "
                                      "Ожидалось, что они приедут в пятницу.)"
                                      "\n4. Have something done (предоставление каких-либо услуг)."
                                      "\nПодлежащее + have + дополнение + глагол в 3-ей форме "
                                      "(I had my nails done yesterday. — Мне сделали маникюр вчера.)")
    bot.send_message(message.chat.id, '<i>(Взято частично с englex.ru)</i>', parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'There is/There are')
def there_isare(message):
    f = open('thereisare11.png', 'rb')
    f1 = open('thereisare22.png', 'rb')
    bot.send_message(message.chat.id, "There is и there are используют, когда хотят сказать, что что-то существует "
                                      "(не существует) или находится (не находится) в конкретном месте.")
    bot.send_message(message.chat.id, "There is - наличие в определенном месте какого-то одного предмета (лица). "
                                      "Также используется с неопределенными подлежащими (неопределенный артикль "
                                      "(«a», «an»), когда артикля нет, или используются слова «some», «any», «no»), "
                                      "и с неопределенными местоимениями как «somebody», «nothing» "
                                      "(There’s something that makes me feel worried. – Меня что-то тревожит).")
    bot.send_message(message.chat.id,
                     "There are - на наличие в определенном месте нескольких (многих) предметов (лиц).")
    bot.send_photo(message.chat.id, f)
    bot.send_message(message.chat.id, "Оборот there is/are можно использовать во временах Perfect. "
                                      "В конструкциях типа there has been речь идет о действии, которое совершилось до "
                                      "момента речи, а результат при этом актуален на данный момент. ")
    bot.send_photo(message.chat.id, f1)
    bot.send_message(message.chat.id, "<i>(Взято частично с englishdom.com, skysmart.ru)</i>", parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'Reported speech (Косв. речь)')
def rep_speech(message):
    f = open('rp1.png', 'rb')
    f1 = open('rp21.png', 'rb')
    f2 = open('rp22.png', 'rb')
    bot.send_message(message.chat.id, "Прямая речь (Direct Speech) — это способ, при котором высказывание другого "
                                      "человека передается слово в слово (в кавычках), тогда как косвенная "
                                      "(Reported Speech) — это пересказ чужих слов с изменением стиля изложения и "
                                      "заменой слов.")
    bot.send_photo(message.chat.id, f1)
    bot.send_photo(message.chat.id, f2)
    bot.send_message(message.chat.id, "Past Simple не меняется, когда стоит после временных союзов, например: when, "
                                      "as, while, before, after, since и т. д.")
    bot.send_message(message.chat.id, "Порядок слов в косвенном вопросе такой же, как и в утвердительном предложении. "
                                      "Прямой общий вопрос подразумевает ответ «да» или «нет», поэтому в косвенном "
                                      "вопросе используются такие слова, как if и whether, которые переводятся на "
                                      "русский язык как «ли» (I asked my friend if she had finished reading my "
                                      "book. — Я спросила свою подругу, дочитала ли она мою книгу).")
    bot.send_message(message.chat.id, "Если вопрос в прямой речи начинается с вопросительного слова "
                                      "(where, what, when и т. д.), то косвенный вопрос также следует "
                                      "начинать с вопросительного слова, не используя вспомогательные "
                                      "глаголы do/does, did и сохраняя прямой порядок слов (He asked me "
                                      "where I lived. — Он спросил, где я живу).")
    bot.send_message(message.chat.id, "Приказ или просьба в косвенной речи всегда выражаются инфинитивом "
                                      "(My mom told me to switch on the light. — Мама сказала мне включить свет).")
    bot.send_photo(message.chat.id, f)
    bot.send_message(message.chat.id, "Личные местоимения I, we меняются на местоимения he, she, they, а местоимение "
                                      "you в зависимости от контекста может меняться на I, we или же на he, she, they."
                                      "\nЕсли глагол в главном предложении стоит в прошедшем времени (said, told), то "
                                      "при преобразовании прямой речи в косвенную указательные местоимения и наречия "
                                      "заменяются.")
    bot.send_message(message.chat.id, "<i>(Взято частично с englex.ru)</i>", parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'Articles')
def articles(message):
    f = open('art1.png', 'rb')
    f1 = open('art2.png', 'rb')
    f2 = open('art3.png', 'rb')
    f3 = open('art4.png', 'rb')
    f4 = open('art51.png', 'rb')
    f5 = open('art52.png', 'rb')
    bot.send_photo(message.chat.id, f)
    bot.send_photo(message.chat.id, f1)
    bot.send_photo(message.chat.id, f2)
    bot.send_photo(message.chat.id, f3)
    bot.send_photo(message.chat.id, f4)
    bot.send_photo(message.chat.id, f5)
    bot.send_message(message.chat.id, "<i>(Взято частично с skyeng.ru)</i>", parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'Предлоги')
def preps(message):
    f = open('prep_time.png', 'rb')
    f1 = open('prep_place.png', 'rb')
    f2 = open('prep_drct.png', 'rb')
    f3 = open('prep_rsn.png', 'rb')
    bot.send_photo(message.chat.id, f, "Предлоги времени")
    bot.send_photo(message.chat.id, f1, "Предлоги места")
    bot.send_photo(message.chat.id, f2, "Предлоги направления")
    bot.send_photo(message.chat.id, f3, "Предлоги причины")
    bot.send_message(message.chat.id, "Правила постановки предлога в предложении:"
                                      "\n1. Перед существительным или местоимением. Put the glass on the table. — "
                                      "Положи стакан на стол. Give the book to Tom. — Передай эту книгу Тому."
                                      "\n2. В конце вопросительных предложений. Where do you live in? — "
                                      "Где ты живешь? Who are you waiting for? — Кого ты ждешь?"
                                      "\n3. В конце придаточного предложения или пассивной конструкции. "
                                      "Apartment repair is what they wanted to begin with. — "
                                      "Они хотели бы начать с ремонта квартиры. You know who he is worried about. — "
                                      "Ты знаешь, о ком он беспокоится.")
    bot.send_message(message.chat.id, "<i>(Взято частично с skysmart.ru)</i>", parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'Plural (Множ-е число)')
def plural(message):
    f1 = open('pl1.png', 'rb')
    f2 = open('pl2.png', 'rb')
    f3 = open('pl3.png', 'rb')
    f4 = open('pl4.png', 'rb')
    f5 = open('pl41.png', 'rb')
    f6 = open('pl5.png', 'rb')
    f7 = open('pl6.png', 'rb')
    f8 = open('pl7.png', 'rb')
    f9 = open('pl8.png', 'rb')
    bot.send_photo(message.chat.id, f1)
    bot.send_photo(message.chat.id, f2)
    bot.send_photo(message.chat.id, f3)
    bot.send_photo(message.chat.id, f4)
    bot.send_photo(message.chat.id, f5)
    bot.send_photo(message.chat.id, f6)
    bot.send_photo(message.chat.id, f7)
    bot.send_photo(message.chat.id, f8)
    bot.send_photo(message.chat.id, f9)
    bot.send_message(message.chat.id, "<i>(Взято частично с skysmart.ru)</i>", parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'Степени сравн. прилагат.')
def st_sr(message):
    f1 = open('Снимок экрана 2023-02-23 175938.png', 'rb')
    f2 = open('foto-51_51-e1640768483277.jpg', 'rb')
    bot.send_photo(message.chat.id, f1)
    bot.send_photo(message.chat.id, f2)


@bot.message_handler(func=lambda message: message.text == 'Complex object (Сложн. дополн.)')
def complx(message):
    f1 = open('complex-object.jpg', 'rb')
    f2 = open('comp2.png', 'rb')
    bot.send_photo(message.chat.id, f1)
    bot.send_photo(message.chat.id, f2)


@bot.message_handler(func=lambda message: message.text == 'Used to')
def used_to(message):
    f1 = open('AT0gBgN10ik.jpg', 'rb')
    bot.send_photo(message.chat.id, f1)


@bot.message_handler(func=lambda message: message.text == 'Be going to')
def used_to(message):
    f1 = open('bgt1.png', 'rb')
    f2 = open('bgt2.png', 'rb')
    f3 = open('bgt3.png', 'rb')
    f4 = open('bgt4.png', 'rb')
    bot.send_message(message.chat.id, "Эту конструкцию мы используем в следующих случаях: "
                                      "\n1. Когда заранее планируем что-либо сделать. (она собирается испечь торт; "
                                      "он собирается помыть машину) "
                                      "\n2. Когда говорим о том, что что-то произойдет с большой вероятностью и "
                                      "для этого есть все признаки. (собирается дождь, посмотри на эти облака)")
    bot.send_message(message.chat.id, "They are going to swim in the pool. Они собираются поплавать в бассейне."
                                      "\n "
                                      "\nShe is going to find a job. Она собирается найти работу. "
                                      "\n"
                                      "\nWe are going to buy a car. Мы собираемся купить машину ")
    bot.send_photo(message.chat.id, f1)
    bot.send_photo(message.chat.id, f2)
    bot.send_photo(message.chat.id, f3)
    bot.send_message(message.chat.id, "Эта конструкция может использоваться в прошедшем времени. "
                                      "Её можно использовать, когда мы говорим, что собирались что-то сделать, "
                                      "но так и не сделали "
                                      "\n(She was going to go to the party, but her father did not let her go. "
                                      "Она собиралась идти на вечеринку, но ее отец не пустил ее).")
    bot.send_photo(message.chat.id, f4)


@bot.message_handler(func=lambda message: message.text == 'Gerund (Герундий)')
def gerund(message):
    f1 = open('ger1.png', 'rb')
    f2 = open('ger2.png', 'rb')
    bot.send_photo(message.chat.id, f1)
    bot.send_message(message.chat.id, "<b>Когда используется:</b> "
                                      "\n1. Говорим о том, что нравится / не нравится:"
                                      "\nto fancy, to feel like — хотеть"
                                      "\nto enjoy — наслаждаться"
                                      "\nto (not) mind — (не) возражать"
                                      "\nto dislike — не любить"
                                      "\ncan’t stand — не выносить", parse_mode='html')
    bot.send_message(message.chat.id, "\n2. Когда выражаем мнение, предлагаем идеи:"
                                      "\nto admit — признавать"
                                      "\nto deny — отрицать"
                                      "\nto consider — обдумывать"
                                      "\nto imagine — представлять"
                                      "\nto suggest — предлагать")
    bot.send_message(message.chat.id, "\n3. Говорим о действии, которое начинается, продолжается или заканчивается:"
                                      "\nto commence — начинать"
                                      "\nto keep (on) — продолжать"
                                      "\nto give up — сдаваться, бросать, прекращать"
                                      "\nto finish — заканчиватьto imagine — представлять")
    bot.send_message(message.chat.id, "\n4. Речь идет о занятиях спортом, хобби или какими-либо активностями в"
                                      " выражениях с глаголом go:"
                                      "\nto go dancing — ходить на танцы"
                                      "\nto go swimming — ходить на плавание"
                                      "\nto go fishing — ходить на рыбалку"
                                      "\nto go skating — ходить кататься на коньках")
    bot.send_message(message.chat.id, "\n5. Герундий употребляют после конструкции to be + прилагательное + предлог:"
                                      "\nto be afraid of smth — бояться чего-либо"
                                      "\nto be fond of smth — любить что-либо, увлекаться чем-либо"
                                      "\nto be good/bad at smth — хорошо/плохо уметь что-либо, быть способным/"
                                      "неспособным к чему-либо"
                                      "\nto be interested in smth — интересоваться чем-либо"
                                      "\nto be tired of smth — уставать от чего-либо")
    bot.send_message(message.chat.id, "\n6. После:"
                                      "\nto accuse of — обвинять в"
                                      "\nto blame for — винить за"
                                      "\nto carry on — продолжать"
                                      "\nto complain of — жаловаться на"
                                      "\nto congratulate on — поздравлять с"
                                      "\nto depend on — зависеть от"
                                      "\nto dream of — мечтать о"
                                      "\nto hear of — слышать о"
                                      "\nto insist on — настаивать на"
                                      "\nto keep from — удерживаться от"
                                      "\nto look forward to — предвкушать, с нетерпением ждать"
                                      "\nto praise for — хвалить за"
                                      "\nto prevent from — предотвращать от"
                                      "\nto succeed in — преуспевать в"
                                      "\nto suspect of — подозревать в"
                                      "\nto take up — начинать делать"
                                      "\nto thank for — благодарить за"
                                      "\nto think of — думать о")
    bot.send_photo(message.chat.id, f2)
    bot.send_message(message.chat.id, "<i>(Взято частично с englex.ru)</i>", parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'Новые слова')
def new_words(message):
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item_categ1 = types.KeyboardButton('Слова')
    item_categ2 = types.KeyboardButton('Фразы')
    ret_back = types.KeyboardButton(text='Назад ↩')
    markup_reply.row(item_categ1, item_categ2)
    markup_reply.row(ret_back)
    bot.send_message(message.chat.id, 'В этом разделе можно изучать слова или фразы. '
                                      '\nВыбирай, и <i><b>каждые несколько часов</b></i> будешь узнавать что-то '
                                      '<i><b>новое</b></i>.'
                                      '\n<b>Не забудь включить уведомления!</b>',
                     reply_markup=markup_reply, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'Слова')
def byt_words(message):
    bot.send_message(message.chat.id, random.choice(pred))
    bot.send_message(message.chat.id, random.choice(pred))
    for i in range(1000):
        time.sleep(60 * 60 * 5)
        bot.send_message(message.chat.id, random.choice(pred))


@bot.message_handler(func=lambda message: message.text == 'Фразы')
def phrases(message):
    f = open('if-you-want-food-you-ask-for-it-like-a-man.mp4', 'rb')
    f1 = open("no-i'll-be-out-in-a-minute.mp4", 'rb')
    f2 = open("calm-down-doctor-now-is-not-the-time-for-fear.mp4", 'rb')
    f3 = open("i'll-call-back-tomorrow.mp4", 'rb')
    f4 = open("if-this-man-should-fall-who-will-lift-the-flag-and-carry-on.mp4", 'rb')
    f5 = open("come-back-next-week.mp4", 'rb')
    f6 = open("i-need-you-to-come-over-as-soon-as-you-get-this-it's-important.mp4", 'rb')
    f7 = open("if-we-can-come-up-with-a-new-trick-change-the-name-of-the-act-the-name-stays.mp4", 'rb')
    f8 = open("find-out-who-he-is.mp4", 'rb')
    f9 = open("you-just-fill-in-the-details.mp4", 'rb')
    f10 = open("no-but-it-took-me-a-while-to-figure-out-why-i-felt-you-know-so-different.mp4", 'rb')
    f11 = open("don't-give-up-on-me-now-dean.mp4", 'rb')
    f12 = open("don't-give-in-to-hate.mp4", 'rb')
    f13 = open("you-never-could-get-along-with-anyone-in-school.mp4", 'rb')
    f14 = open("well-then-you-got-to-get-up-earlier-what's-that.mp4", 'rb')
    f15 = open("get-off-the-road.mp4", 'rb')
    f16 = open("kid-that's-the-wizard-get-on-it.mp4", 'rb')
    f17 = open("get-out-of-here.mp4", 'rb')
    f18 = open("we-just-gonna-get-through-this-somehow-okay.mp4", 'rb')
    f19 = open("it'll-be-okay-i-have-to-go-away.mp4", 'rb')
    f20 = open("go-ahead-sit-down.mp4", 'rb')
    f21 = open("go-on-take-it.mp4", 'rb')
    f22 = open("i-know-why-you're-afraid-to-go-out-at-night.mp4", 'rb')
    f23 = open("just-hang-on-a-minute.mp4", 'rb')
    f24 = open("i-always-learn-something-when-i-hang-out-with-the-elderly.mp4", 'rb')
    f25 = open("you-might-be-let-down.mp4", 'rb')
    f26 = open("i'm-going-to-look-after-you.mp4", 'rb')
    f27 = open("i'll-go-look-for-some-food-take-the-shotgun.mp4", 'rb')
    f28 = open("i-look-forward-to-our-partnership.mp4", 'rb')
    f29 = open("look-i-don't-have-anyone-eise-to-put-on-this-and-you-know-it.mp4", 'rb')
    video = [f, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22,
             f23, f24, f25, f26, f27, f28, f29]
    video_trscp = {
        f: 'Текст видео: If you want food, you <b>ask for it</b> like a man (Если тебе нужна еда, ты попросишь ее как '
           'мужчина)',
        f1: "Текст видео: No i'll <b>be out</b> in a minute (Нет, я выйду через минуту)",
        f2: "Текст видео: <b>Calm down</b> doctor now is not the time for fear (Успокойтесь, доктор, сейчас не время "
            "для страха)",
        f3: "Текст видео: I'll <b>call back</b> tomorrow (Я позвоню завтра)",
        f4: 'Текст видео: If this man should fall, who will lift the flag and <b>carry on</b>? (Если этот человек '
            'падет, кто поднимет флаг и продолжит?)',
        f5: 'Текст видео: <b>Come back</b> next week (Возвращайся на следующей неделе)',
        f6: "Текст видео: I need you to <b>come over</b> as soon as you get this, it's important (Мне нужно, "
            "чтобы ты пришел, как только получишь это, это важно)",
        f7: 'Текст видео: If we can <b>come up</b> with a new trick, change the name of the act (Если мы сможем '
            'придумать новый трюк, измените название номера)',
        f8: 'Текст видео: <b>Find out</b> who he is (Выясни, кто он такой)',
        f9: 'Текст видео: You just <b>fill in</b> the details (Просто заполните детали)',
        f10: 'Текст видео: No, but it took me a while to <b>figure out</b> why i felt, you know, so different (Нет, '
             'но мне потребовалось некоторое время, чтобы понять, почему я чувствовал себя, знаешь ли, таким другим)',
        f11: "Текст видео: Don't <b>give up</b> on me now, Dean (Не отказывайся от меня сейчас, Дин)",
        f12: "Текст видео: Don't <b>give in</b> to hate (Не позволь гневу овладеть тобой)",
        f13: 'Текст видео: You never could <b>get along</b> with anyone in school (У тебя никогда не получалось '
             'поладить с кем-то в школе)',
        f14: "Текст видео: Well then you got to <b>get up</b> earlier. What's that? (Что ж, тогда тебе придется "
             "вставать "
             "пораньше. Что это такое?)",
        f15: 'Текст видео: <b>Get off</b> the road! (Убирайся с дороги!)',
        f16: "Текст видео: Kid, that's the wizard. <b>Get on</b> it (Малыш, это волшебник. Займись им)",
        f17: 'Текст видео: <b>Get out of</b> here! (Проваливай отсюда!)',
        f18: 'Текст видео: We just gonna <b>get through</b> this somehow. Okay? (Мы как-нибудь справимся с этим. '
             'Ладно?)',
        f19: "Текст видео: It'll be okay. I have to <b>go away</b> (Всё будет хорошо. Мне нужно уйти)",
        f20: 'Текст видео: <b>Go ahead</b>, sit down (Давай, садись)',
        f21: 'Текст видео: <b>Go on</b>, take it (Давай, возьми это)',
        f22: "Текст видео: I know why you're afraid to <b>go out</b> at night (Я знаю, почему ты боишься выходить по "
             "ночам)",
        f23: 'Текст видео: Just <b>hang on</b> a minute (Подождите минуту)',
        f24: 'Текст видео: I always learn something when i <b>hang out</b> with the elderly (Я всегда узнаю новое, '
             'когда тусуюсь со стариками)',
        f25: 'Текст видео: You might be <b>let down</b> (Должно быть, ты расстроен)',
        f26: "Текст видео: I'm going to <b>look after</b> you (Я буду заботиться о тебе)",
        f27: "Текст видео: I'll go <b>look for</b> some food. Take the shotgun (Я пойду поищу еды. Возьми оружие)",
        f28: 'Текст видео: I <b>look forward to</b> our patnership (Я с нетерпением жду нашего партнерства)',
        f29: "Текст видео: Look, i don't have anyone else to <b>put on</b> this and you know it (Послушай, мне больше "
             "некого втянуть в это, и ты это знаешь)"}
    phrases_dict = {f: '<b>ask for</b> – просить, спрашивать, требовать',
                    f1: '<b>be out</b> – отсутствовать (не быть дома, на месте)',
                    f2: '<b>calm down</b> – успокоиться',
                    f3: '<b>call back</b> — перезванивать',
                    f4: '<b>carry on</b> — продолжать что-то делать',
                    f5: '<b>come back</b> – возвращаться',
                    f6: '<b>come over</b> – прийти, зайти к кому-то (обычно домой).',
                    f7: '<b>come up with</b> — придумать что-то, предложить что-то',
                    f8: '<b>find out</b> — узнавать что-то',
                    f9: '<b>fill in</b> – заполнять (форму, анкету, бланк)',
                    f10: '<b>figure out</b> – понять, выяснить, найти ответ или решение',
                    f11: '<b>give up</b> – сдаваться (падать духом)',
                    f12: '<b>give in</b> – уступать, сдаться, признавать',
                    f13: '<b>get along</b> – ладить, быть в хороших отношениях',
                    f14: '<b>get up</b> – вставать',
                    f15: '<b>get off</b> – сойти, выйти из (общественный транспорт и другое)',
                    f16: '<b>get on</b> – войти, сесть на общественный транспорт',
                    f17: '<b>get out of</b> – выйти из, выбраться',
                    f18: '<b>get through</b> – выжить, пройти через что-то',
                    f19: '<b>go away</b> – уходить, уезжать',
                    f20: '<b>go ahead</b>— продолжать, начинать, призыв к действию – «давай, вперед»',
                    f21: '<b>go on</b>— продолжать, призыв к действию',
                    f22: '<b>go out</b>— выйти в общество, проводить время вне дома, пойти развлекаться',
                    f23: '<b>hang on</b>— подождать',
                    f24: '<b>hang out</b>— тусоваться, проводить время, «зависать» где-то/с кем-то',
                    f25: '<b>let down</b>— расстроить, разочаровать кого-то',
                    f26: '<b>look after</b> — присматривать за чем-то/кем-то',
                    f27: '<b>look for</b> — искать что-то/кого-то',
                    f28: '<b>look forward to</b> — ждать чего-либо с нетерпением',
                    f29: '<b>put on</b> — надеть что-либо, втянуть во что-то'}
    a = random.choice(video)
    bot.send_message(message.chat.id, phrases_dict[a], parse_mode='html')
    bot.send_video(message.chat.id, a)
    bot.send_message(message.chat.id, video_trscp[a], parse_mode='html')
    for i in range(1000):
        time.sleep(60*60*5)
        a = random.choice(video)
        bot.send_message(message.chat.id, phrases_dict[a], parse_mode='html')
        bot.send_video(message.chat.id, a)
        bot.send_message(message.chat.id, video_trscp[a], parse_mode='html')


bot.polling(none_stop=True, interval=0)
