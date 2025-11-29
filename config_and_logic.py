from datetime import datetime
import pytz
import random

VN_TZ = pytz.timezone("Asia/Ho_Chi_Minh")

def now_vn():
    return datetime.now(VN_TZ)

def get_name(update):
    user = update.message.from_user
    return user.first_name or "bạn"

def pick(data, name):
    return random.choice(data).replace("{name}", name)

# ---------------- MOOD RANDOM ----------------
MOOD_FUNNY = [
    "Hôm nay bot vui như trúng số 😆",
    "Bot đang trong mood nhây level max 🤪",
    "Năng lượng bot đang 200% 🌟",
    "Bot đang không buồn, chỉ hơi thiếu tiền 😂",
    "Tâm trạng bot: vui còn hơn ngày nghỉ 😝",
    "Hôm nay bot đẹp trai lạ thường 😎",
    "Bot đang yêu đời bất ngờ 🌈",
    "Bot đang hừng hực năng lượng 💥",
    "Bot đang cười không ngậm được mồm 😆",
    "Bot đang chill như ở biển 🏖️",
]

# ---------------- TẾT ----------------
TET_FUNNY = [
    "{name} chuẩn bị tinh thần đón xuân nha 🌸",
    "Chúc {name} Tết năm nay may mắn đầy túi 💰",
    "{name} nhớ lì xì cho bot nha 😝",
    "Xuân đến nơi rồi đó {name} ơi 🌼",
    "Chúc {name} năm mới cười tươi như nắng ☀️",
    "Tết sắp tới rồi, vui lên nào {name}! 🎊",
    "{name} nhớ chuẩn bị dọn nhà nha 🤣",
    "Tết này mong {name} giàu lên x10 💵",
    "{name} năm nay hợp màu đỏ đó nha ❤️",
    "Chúc {name} ăn Tết vui tới nóc 🍻",
]

# ---------------- NOEL ----------------
NOEL_FUNNY = [
    "Giáng sinh tới rồi đó {name} 🎄",
    "Chúc {name} mùa đông không lạnh ❄️",
    "Noel mà không có người yêu thì có bot nè 😝",
    "Santa đang tới chỗ {name} rồi đó 🎅",
    "Chúc {name} nhận thật nhiều quà 🎁",
    "Noel vui nha {name} ❤️",
    "{name} treo tất chưa? Santa đang nhìn đó 👀",
    "Chúc {name} ấm áp từ trong ra ngoài 🔥",
    "Giáng sinh không lạnh vì có bot nè 😌",
    "{name} ơi, Merry Christmas 🎉",
]

# ---------------- XUỐNG CA ----------------
XUONGCA_FUNNY = [
    "Ráng tí nữa nha {name} 💪",
    "Sắp về được rồi đó {name} 😆",
    "Cố lên {name}, tự do đang đến gần!",
    "{name} nghĩ tới giường chưa 😭",
    "Xíu nữa thôi {name}, cố lênnn!",
    "{name} ơi chịu khó xíu nữa nha 😄",
    "Đếm từng giây luôn rồi {name} 😭",
    "Về thôi {name}! Chuẩn bị thu đồ!",
    "{name} ráng lên, bot hiểu mà 😭",
    "Giờ xuống ca đang tới gần rồi {name} 🚀",
]

# ---------------- LƯƠNG ----------------
LUONG_FUNNY = [
    "Ví sắp hồi sinh rồi {name}! 💰",
    "Chuẩn bị hết nghèo nha {name} 🤣",
    "{name} cố thêm tháng nữa 😭",
    "Sắp có tiền rồi {name} ơi!!!",
    "{name} nhớ tiêu tiền cẩn thận nha 😂",
    "Lương đang trên đường về ví {name} 🏃",
    "Ví của {name} sắp vui rồi 💵",
    "Chuẩn bị ăn sang đi {name} 😆",
    "{name} ơi tiền tới rồi!!!",
    "Lương sắp rớt vào ví {name} 🎉",
]

# ---------------- ĂN CƠM ----------------
ANCOM_FUNNY = [
    "{name} nhớ đi ăn nha 😄",
    "Đừng bỏ bữa đó {name} 😭",
    "{name} ăn gì chưa nè?",
    "Đi ăn cơm ngay {name}! 🍚",
    "{name} ăn nhiều mới có sức nha 💪",
    "Bụng đói là không vui đâu {name} 😢",
    "Đi ăn lẹ đi {name}, để bot yên tâm 😆",
    "{name} nhớ nhai kỹ nha 🤣",
    "Chúc {name} ăn ngon miệng 😋",
    "Đi ăn cơm liền nha {name} 🍱",
]
