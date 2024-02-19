from fastapi import FastAPI, Request, Response
from telegram.ext import Application
from telegram import Update
from contextlib import asynccontextmanager
from http import HTTPStatus
import uvicorn

from app.telegram_bot import add_handlers
from app.core.config import settings
from app.services.auth import auth_update


telegram_bot = (
        Application.builder()
        .token(settings.TELEGRAM_API_KEY)
        .build()
)

add_handlers(telegram_bot)



@asynccontextmanager
async def lifespan(_: FastAPI):
    await telegram_bot.bot.setWebhook(settings.WEBHOOK_URL)
    async with telegram_bot as bot:
        await bot.start()
        yield
        await telegram_bot.bot.deleteWebhook(settings.WEBHOOK_URL)
        await bot.stop()


app = FastAPI(lifespan=lifespan)


# webhook setup
@app.post("/")
async def process_update(request: Request):
    req = await request.json()
    update = Update.de_json(req, telegram_bot.bot)
    is_allowed = await auth_update(update)
    if is_allowed:
        await telegram_bot.process_update(update)
        return Response(status_code=HTTPStatus.OK)
    else:
        await update.message.reply_text('You are not allowed to use Jane, please talk to Albert about it!')
        print(f'User with id {update.effective_user.id} and name {update.effective_user.full_name} tried to access Jane')
        return Response(status_code=HTTPStatus.OK)



@app.get("/")
async def root():
    return {"message": "Telegram Communication Service is running"}


if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=3000, reload=True)
