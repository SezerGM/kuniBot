import aiogram
from aiogram import Bot, Dispatcher, executor, types
import sqlite3
import config
from config import TOKEN
from db import Database


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
db = Database('database/bot_db.db')

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="О чем весь разговор?", callback_data="secondM"))
    if (not db.user_exists((message.from_user.id))):
        db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, "Добро пожаловать странник🥸👋🏻\n\n Назови себя!")
    else:
        await message.answer("Добро пожаловать странник🥸👋🏻\n"
                            "Я вовсе не удивлён что ты тут, ведь куда бы дороги не вели, они всегда приводят к нам) \n \n"
                            "Так что… располагайся! И готовься стать тем, о ком будут слагать легенды!", reply_markup=keyboard ,parse_mode="Markdown")


@dp.callback_query_handler(text="secondM")
async def SecondM_command(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Оплатить обучение", callback_data="payment"))
    keyboard.add(types.InlineKeyboardButton(text="Удиви ещё!", callback_data="thirdM"))

    await call.message.answer("Ты наш очередной последователь тайного искусства - *KUNI*😝\n\n*Благодаря нашей поддержке*:\n -Ты станешь лучшим любовником!\n -Повысишь личную уверенность!\n -Раскроешь таланты и получишь незабываемые навыки!\n\nЗа *EXTRA обучение*, проводящееся в рамках удобного\nинтерактива, раскрытого в 3 модулях ты со своей сладкой\nполовинкой💘 достигнешь пика удовольствия!💗",reply_markup=keyboard,parse_mode="Markdown")

@dp.callback_query_handler(text="thirdM")
async def thirdM_command(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Оплатить обучение", callback_data="payment"))
    keyboard.add(types.InlineKeyboardButton(text="Мне мало! Хочу ещё!!", callback_data="fourthM"))

    await call.message.answer("Естественно у нас припасены секреты 🤐 о которых никто не говорит!\n\nВедь помимо раскрытия *ЛУЧШИХ ТЕХНИК* с предоставлением *ФИРМЕННЫХ ЛАЙФХАКОВ*🫂\n\nМы раскрываем свой продукт через проработку *ПСИХОЛОГИЧЕСКИХ*, *ФИЗИОЛОГИЧЕСКИХ* и конечно же *ТЕХНИЧЕСКИХ*🥴 АСПЕКТОВ!\n\n*УЖЕ ПОСЛЕ ПЕРВОЙ БАЗЫ* вы сможете сразить любую, ещё и показав *СЕРТИФИКАТ МАСТЕРА*🫡",reply_markup=keyboard,parse_mode="Markdown")

@dp.callback_query_handler(text="fourthM")
async def fourthM_command(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Оплатить обучение", callback_data="payment"))

    await call.message.answer("О чём ещё думать! Ты что!!!?? Тугодум?! Небось ещё и в постели такая же шняга🥱\n\n Так что смотри! Ты можешь потратить жизнь *штрудируя* тонны литературы, а можешь прийти к нам на обучение и сделать *ЛУЧШИЙ ПОДАРОК ВТОРОЙ ПОЛОВИНКЕ!*\n\n",parse_mode="Markdown")
    await call.message.answer("Ответ без сомнений прост!\n\nВкладываю копейки в наше обучение ты получаешь то, что НЕ СОБЕРЁТ НИ ОДИН ПОИСКОВИК,👎🏻 а уж тем более НЕ ПОДСКАЖЕТ ЗАЦ🔞НЗУРИРОВАННАЯ НЕЙРОННАЯ СЕТЬ. \nБеги оплачивай и приступай к обучению...🏃🏼 ",reply_markup=keyboard,parse_mode="Markdown")

@dp.callback_query_handler(text="payment")
async def payment_command(call: types.CallbackQuery):
    await bot.send_invoice(call.message.chat.id, 'Купить обучение', 'Покупка курса по Куни', 'invoce',config.PAYMENT_TOKEN, 'RUB', [types.LabeledPrice('Купить обучение', 969 * 100)])

@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

if __name__ == '__main__':
    executor.start_polling(dp)