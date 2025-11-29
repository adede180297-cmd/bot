from telegram.ext import Application, CommandHandler
from config_and_logic import *

TOKEN = "YOUR_TOKEN_HERE"   # <-- NHỚ THAY TOKEN

async def countdown_tet(update, context):
    name = get_name(update)
    now = now_vn()
    diff = target_date_tet - now

    days = diff.days
    h = diff.seconds // 3600
    m = (diff.seconds % 3600) // 60
    s = diff.seconds % 60

    msg = (
        "🧨 Đếm ngược Tết 2026 🧨\n\n"
        f"{pick(MOOD_FUNNY, name)}\n"
        f"{pick(TET_FUNNY, name)}\n\n"
        f"⏳ Còn: {days} ngày {h} giờ {m} phút {s} giây"
    )

    await update.message.reply_text(msg)


async def countdown_noel(update, context):
    name = get_name(update)
    now = now_vn()
    diff = target_date_noel - now

    days = diff.days
    h = diff.seconds // 3600
    m = (diff.seconds % 3600) // 60

    msg = (
        "🎄 Đếm ngược Noel 2025 🎄\n\n"
        f"{pick(MOOD_FUNNY, name)}\n"
        f"{pick(NOEL_FUNNY, name)}\n\n"
        f"⏳ Còn: {days} ngày {h} giờ {m} phút"
    )

    await update.message.reply_text(msg)


async def countdown_xuongca(update, context):
    name = get_name(update)
    now = now_vn()

    end = now.replace(hour=20, minute=0, second=0, microsecond=0)
    if now > end:
        end += timedelta(days=1)

    diff = end - now
    h = diff.seconds // 3600
    m = (diff.seconds % 3600) // 60
    s = diff.seconds % 60

    msg = (
        "🕗 Đếm ngược xuống ca 🕗\n\n"
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
        payday = payday.replace(month=payday.month % 12 + 1)
        if payday.month == 1:
            payday = payday.replace(year=payday.year + 1)

    diff = payday - now
    days = diff.days
    h = diff.seconds // 3600
    m = (diff.seconds % 3600) // 60

    msg = (
        "💰 Đếm ngược ngày nhận lương 💰\n\n"
        f"{pick(MOOD_FUNNY, name)}\n"
        f"{pick(LUONG_FUNNY, name)}\n\n"
        f"⏳ Còn: {days} ngày {h} giờ {m} phút"
    )

    await update.message.reply_text(msg)


async def ancom(update, context):
    name = get_name(update)
    msg = (
        "🍚 Tới giờ ăn cơm rồi! 🍚\n\n"
        f"{pick(MOOD_FUNNY, name)}\n"
        f"{pick(ANCOM_FUNNY, name)}"
    )
    await update.message.reply_text(msg)


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("countdown", countdown_tet))
    app.add_handler(CommandHandler("noel", countdown_noel))
    app.add_handler(CommandHandler("xuongca", countdown_xuongca))
    app.add_handler(CommandHandler("luong", countdown_luong))
    app.add_handler(CommandHandler("ancom", ancom))

    print("Bot đang chạy…")
    app.run_polling()


if __name__ == "__main__":
    main()
