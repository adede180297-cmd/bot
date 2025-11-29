from telegram.ext import Application, CommandHandler
from datetime import datetime, timedelta
from config_and_logic import (
    now_vn, get_name, pick,
    MOOD_FUNNY, TET_FUNNY, NOEL_FUNNY,
    XUONGCA_FUNNY, LUONG_FUNNY, ANCOM_FUNNY
)

TOKEN = "8324202114:AAGJM7kfxiKvY5qTqz751elPHz_Prf0otZ8"

# ================== HANDLERS ==================

async def countdown_tet(update, context):
    name = get_name(update)
    now = now_vn()
    target = datetime(2026, 2, 17, 0, 0, 0, tzinfo=now.tzinfo)
    diff = target - now

    days = diff.days
    h = diff.seconds // 3600
    m = diff.seconds % 3600 // 60
    s = diff.seconds % 60

    msg = (
        "🧨 Đếm ngược Tết 2026 nèee! 🧨\n\n"
        f"{pick(MOOD_FUNNY, name)}\n"
        f"{pick(TET_FUNNY, name)}\n\n"
        f"⏳ Còn: {days} ngày {h} giờ {m} phút {s} giây\n"
    )

    await update.message.reply_text(msg)


async def countdown_noel(update, context):
    name = get_name(update)
    now = now_vn()
    target = datetime(2025, 12, 25, 0, 0, 0, tzinfo=now.tzinfo)
    diff = target - now

    days = diff.days
    h = diff.seconds // 3600
    m = diff.seconds % 3600 // 60

    msg = (
        "🎄 Đếm ngược Noel 2025 nè! 🎄\n\n"
        f"{pick(MOOD_FUNNY, name)}\n"
        f"{pick(NOEL_FUNNY, name)}\n\n"
        f"⏳ Còn: {days} ngày {h} giờ {m} phút\n"
    )

    await update.message.reply_text(msg)


async def countdown_xuongca(update, context):
    name = get_name(update)
    now = now_vn()
    end = now.replace(hour=20, minute=0, second=0)

    if now > end:
        end += timedelta(days=1)

    diff = end - now
    h = diff.seconds // 3600
    m = diff.seconds % 3600 // 60
    s = diff.seconds % 60

    msg = (
        "🕗 Đếm ngược đến giờ xuống ca (20:00) 🕗\n\n"
        f"{pick(MOOD_FUNNY, name)}\n"
        f"{pick(XUONGCA_FUNNY, name)}\n\n"
        f"⏳ Còn: {h} giờ {m} phút {s} giây"
    )

    await update.message.reply_text(msg)


async def countdown_luong(update, context):
    name = get_name(update)
    now = now_vn()
    payday = now.replace(day=16, hour=0, minute=0)

    if now > payday:
        if payday.month == 12:
            payday = payday.replace(year=payday.year + 1, month=1)
        else:
            payday = payday.replace(month=payday.month + 1)

    diff = payday - now
    days = diff.days
    h = diff.seconds // 3600
    m = diff.seconds % 3600 // 60
    s = diff.seconds % 60

    msg = (
        "💰 Đếm ngược ngày nhận lương 💰\n\n"
        f"{pick(MOOD_FUNNY, name)}\n"
        f"{pick(LUONG_FUNNY, name)}\n\n"
        f"⏳ Còn: {days} ngày {h} giờ {m} phút {s} giây\n"
        f"Lương về ngày: {payday.strftime('%d/%m/%Y')}"
    )

    await update.message.reply_text(msg)


async def ancom(update, context):
    name = get_name(update)

    msg = (
        "🍚 Tới giờ ăn cơm rồi nè 🍚\n\n"
        f"{pick(MOOD_FUNNY, name)}\n"
        f"{pick(ANCOM_FUNNY, name)}"
    )

    await update.message.reply_text(msg)


# ================== RUN BOT ==================

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("countdown", countdown_tet))
    app.add_handler(CommandHandler("noel", countdown_noel))
    app.add_handler(CommandHandler("xuongca", countdown_xuongca))
    app.add_handler(CommandHandler("luong", countdown_luong))
    app.add_handler(CommandHandler("ancom", ancom))

    print("Bot đang chạy 24/24 trên Render...")
    app.run_polling()


if __name__ == "__main__":
    main()

