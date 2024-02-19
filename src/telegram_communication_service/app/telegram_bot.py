from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Hello {update.effective_user.first_name}')


async def echo_msg(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


def add_handlers(bot: Application):
    bot.add_handler(CommandHandler("hello", hello))
    bot.add_handler(MessageHandler(filters.ALL, callback=echo_msg))


