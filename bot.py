from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler
from datetime import datetime, timedelta
from random import choice
import asyncio

from config_and_logic import (
    pick, get_name,
    target_date_tet, target_date_noel,
    TET_FUNNY, NOEL_FUNNY, XUONGCA_FUNNY,
    LUONG_FUNNY, ANCOM_FUNNY, MOOD_FUNNY
)

TOKEN = "YOUR_TOKEN_HERE"

# ========================= BOT HANDLERS =========================

def mood():
    return choice(MOOD_FUNNY)

async def countdown_tet(update, context):
    name = get_name(update)
    now = datetime.now()
    diff = target_date_tet - now
    days = diff.days
    h = diff.seconds // 3600
    m = (diff.seconds % 3600) // 60
    s = diff.seconds % 60

    msg = (
        "🧨 Đếm ngược đến Tết 2026 nèee! 🧨\n\n"
        f"{mood()}\n"
        f"{name}, {pick(TET_FUNNY, name)}\n\n"
        f"⏳ Còn: {days} ngày {h} giờ {m} phút {s} giây\n"
        "🌕 Tết rơi vào ngày: 17/02/2026\n"
        "✨ Chúc bạn một năm mới vui tới nóc!"
    )

    await update.message.reply_text(msg)

async def countdown_noel(update, context):
    name = get_name(update)
    now = datetime.now()
    diff = target_date_noel - now
    days = diff.days
    h = diff.seconds // 3600
    m = (diff.seconds % 3600) // 60

    msg = (
        "🎄 Đếm ngược Noel 2025 nèee! 🎄\n\n"
        f"{mood()}\n"
        f"{name}, {pick(NOEL_FUNNY, name)}\n\n"
        f"⏳ Còn: {days} ngày {h} giờ {m} phút\n"
        "📅 Noel vào ngày: 25/12/2025\n"
        "✨ Chúc bạn mùa lễ tràn ngập niềm vui!"
    )

    await update.message.reply_text(msg)

# Add các handler khác của bạn vào đây…

# ========================= FLASK SERVER =========================

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(), application.bot)
    asyncio.run(application.process_update(update))
    return "OK"

# ========================= RUN BOT =========================

application = Application.builder().token(TOKEN).build()

application.add_handler(CommandHandler("countdown", countdown_tet))
application.add_handler(CommandHandler("noel", countdown_noel))
# … thêm các lệnh khác

if __name__ == "__main__":
    # Set webhook cho Telegram
    import requests
    SERVER_URL = "https://YOUR_RENDER_URL"  # đổi link Render của bạn

    requests.get(
        f"https://api.telegram.org/bot{TOKEN}/setWebhook?url={SERVER_URL}/{TOKEN}"
    )

    app.run(host="0.0.0.0", port=10000)
