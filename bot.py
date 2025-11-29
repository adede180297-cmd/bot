from telegram.ext import Application, CommandHandler
from datetime import datetime, timedelta
from random import choice

# ================== TOKEN ==================
TOKEN = "8324202114:AAGJM7kfxiKvY5qTqz751elPHz_Prf0otZ8"


# ================== NGÀY CỐ ĐỊNH ==================
target_date_tet = datetime(2026, 2, 17)
target_date_noel = datetime(2025, 12, 25)

# ================== TÊN USER ==================
def get_name(update):
    u = update.message.from_user
    return u.first_name or "Bạn"

# ================== CHỌN RANDOM ==================
def pick(data, name):
    msg = choice(data)
    return msg.replace("{name}", name)

# ================== MOOD VUI ==================
MOOD_FUNNY = [
    "Hôm nay bot vui dữ lắm luôn á 😆",
    "Bot đang trong mood vui cực mạnh nè 😝",
    "Năng lượng của bot hôm nay: 999% 🌈",
    "Tâm trạng bot đang sáng như ánh mặt trời ☀️",
    "Bot vui quá, muốn chúc bạn thiệt nhiều thứ luôn 😄"
]

# ================== CÂU TẾT ==================
TET_FUNNY = [
    "Chuẩn bị không khí đón xuân nha 🌸",
    "Hy vọng năm mới của bạn thật rực rỡ ✨",
    "Tết này nhớ cười thiệt tươi nha 😄",
    "Xuân đang tới gần từng chút nè 🌼",
    "Chúc bạn sớm cảm nhận được không khí Tết 💛",
]

# ================== CÂU NOEL ==================
NOEL_FUNNY = [
    "Không khí Giáng Sinh đang rất dễ thương nha 🎄",
    "Chúc bạn có mùa Noel thật ấm áp ❤️",
    "Hy vọng bạn nhận được nhiều lời chúc đáng yêu ❄️",
    "Bạn treo đèn Giáng Sinh chưa? ✨",
    "Santa đang chuẩn bị quà đó 😆",
]

# ================== CÂU XUỐNG CA ==================
XUONGCA_FUNNY = [
    "Ráng lên một chút nữa nha 💪",
    "Bạn sắp hết giờ rồi đó 😄",
    "Cố thêm tí nữa, tự do đang tới gần 😆",
    "Nghĩ đến cái giường là có động lực liền 😭",
    "Chúc bạn xuống ca thật nhẹ nhàng ✨",
]

# ================== CÂU LƯƠNG ==================
LUONG_FUNNY = [
    "Ráng chịu đựng nha 😭✌️",
    "Tháng này cố thêm xíu nha 😄",
    "Sắp hết nghèo rồi 😆",
    "Ví bạn sắp được hồi sinh ✨",
    "Hi vọng tháng này không âm 😭",
]

# ================== CÂU ĂN CƠM ==================
ANCOM_FUNNY = [
    "nhớ ăn cơm cho khỏe nha 😄",
    "đừng làm việc mà quên ăn đó nha 🍚",
    "ăn cơm đúng bữa để có sức nha 💪",
    "hôm nay ăn gì ngon chưa? 😆",
    "bụng đói là không vui đâu nha 😭",
]


def mood():
    return choice(MOOD_FUNNY)


# ======================================================
# ==================== LỆNH TẾT =========================
# ======================================================
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


# ======================================================
# ==================== LỆNH NOEL ========================
# ======================================================
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


# ======================================================
# ==================== LỆNH XUỐNG CA ====================
# ======================================================
async def countdown_xuongca(update, context):
    name = get_name(update)
    now = datetime.now()

    end = now.replace(hour=20, minute=0, second=0, microsecond=0)
    if now > end:
        end += timedelta(days=1)

    diff = end - now
    h = diff.seconds // 3600
    m = (diff.seconds % 3600) // 60
    s = diff.seconds % 60

    msg = (
        "🕗 Đếm ngược đến giờ xuống ca (20:00) nèee! 🕗\n\n"
        f"{mood()}\n"
        f"{name}, {pick(XUONGCA_FUNNY, name)}\n\n"
        f"⏳ Còn: {h} giờ {m} phút {s} giây\n"
        "🏠 Chuẩn bị được về rồi đó!\n"
        "✨ Chúc bạn xuống ca thật nhẹ nhàng!"
    )

    await update.message.reply_text(msg)


# ======================================================
# ==================== LỆNH LƯƠNG =======================
# ======================================================
async def countdown_luong(update, context):
    name = get_name(update)
    now = datetime.now()

    payday = now.replace(day=16, hour=0, minute=0)
    if now > payday:
        payday = payday.replace(month=payday.month % 12 + 1)
        if payday.month == 1:
            payday = payday.replace(year=payday.year + 1)

    diff = payday - now
    days = diff.days
    h = diff.seconds // 3600
    m = (diff.seconds % 3600) // 60
    s = diff.seconds % 60

    msg = (
        "💰 Đếm ngược ngày nhận lương nèee! 💰\n\n"
        f"{mood()}\n"
        f"{name}, {pick(LUONG_FUNNY, name)}\n\n"
        f"⏳ Còn: {days} ngày {h} giờ {m} phút {s} giây\n"
        f"📅 Lương về ngày: {payday.strftime('%d/%m/%Y')}\n"
        "✨ Hy vọng tháng này ví bạn không còn buồn nữa!"
    )

    await update.message.reply_text(msg)


# ======================================================
# ==================== LỆNH ĂN CƠM ======================
# ======================================================
async def ancom(update, context):
    name = get_name(update)
    funny = pick(ANCOM_FUNNY, name)

    msg = (
        "🍚 Tới giờ ăn cơm rồi nèeeee! 🍚\n\n"
        f"{mood()}\n"
        f"{name}, {funny}\n"
        "Nhớ đi ăn liền nha, để bụng đói buồn lắm 😭\n"
        "✨ Chúc bạn ăn ngon miệng!"
    )

    await update.message.reply_text(msg)


# ======================================================
# ======================== MAIN =========================
# ======================================================
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
