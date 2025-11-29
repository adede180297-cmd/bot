from datetime import datetime
import pytz
import random

# ===== NGÀY CỐ ĐỊNH =====
vn = pytz.timezone("Asia/Ho_Chi_Minh")

target_date_tet = vn.localize(datetime(2026, 2, 17))
target_date_noel = vn.localize(datetime(2025, 12, 25))


# ===== LẤY TÊN =====
def get_name(update):
    u = update.message.from_user
    return u.first_name or "Bạn"


# ===== RANDOM FORMAT =====
def pick(arr, name="Bạn"):
    msg = random.choice(arr)
    return msg.replace("{name}", name)


# ===== MOOD =====
MOOD_FUNNY = [
    "Hôm nay bot vui dữ dội luôn 😆",
    "Mood đang lên đỉnh nè 😝",
    "Bot đang hoạt động 200% công lực 🌈",
    "Tinh thần bot đang sáng như mặt trời ☀️",
    "Hôm nay bot hiền lắm 😄",
    "Tâm trạng bot đang căng đét 🤣",
    "Bot đang cười sặc nước nè 😂",
    "Năng lượng bot: vô cực 🔥",
    "Bot đang high mood nha 🤪",
    "Hôm nay bot dễ thương lắm 😳",
]


# ===== TẾT =====
TET_FUNNY = [
    "{name} chuẩn bị phong bao lì xì chưa 😆",
    "Năm nay nhớ lì xì bot nha 🤣",
    "Tết đến nơi rồi đó {name} ơi 🎉",
    "Chuẩn bị về quê ăn Tết chưa nè 🧨",
    "Tết này cố mà giảm cân nha 🤣",
    "{name} nhớ dọn nhà nhaaa 😭",
    "Năm nay nghe đồn bạn giàu lắm 😳",
    "Tết này nhớ đừng ngủ tới 2h chiều 😆",
    "Nhớ mua đồ mới nha {name} 👗",
    "Bot chúc bạn năm mới may mắn 😘"
]


# ===== NOEL =====
NOEL_FUNNY = [
    "{name} có người yêu đi chơi Noel chưa 😭",
    "Santa năm nay tới trễ nha 😆",
    "Noel này ấm không? Hay lạnh vì cô đơn ❄️",
    "Giáng sinh này nhận được quà chưa 🎁",
    "Merry x-mess {name} 🤣",
    "Đèn Noel treo chưa nè ✨",
    "Ông già Noel đang đến rồi đó 😳",
    "Chuẩn bị ăn gà rán đêm Noel chưa 🍗",
    "Noel năm nay chill không? 🎄",
    "{name} muốn bot gửi quà không 😝"
]


# ===== XUỐNG CA =====
XUONGCA_FUNNY = [
    "{name} ráng xíu nữa thôi 😭",
    "Sắp được về rồi nè 😆",
    "Tự do đang vẫy gọi bạn 🤣",
    "Cố lên {name}, sắp thoát rồi 😭",
    "Giường đang nhớ bạn 😴",
    "Đếm từng phút đúng không 😭",
    "Xíu nữa được thở rồi nè 😳",
    "Nghĩ đến lương đi cho có động lực 🤣",
    "Chuẩn bị logout cuộc đời 😆",
    "Bot cũng muốn xuống ca theo luôn 😭"
]


# ===== LƯƠNG =====
LUONG_FUNNY = [
    "{name} sắp giàu rồi đó 😭",
    "Ví sắp hồi sinh 😆",
    "Tháng này đỡ nghèo hơn xíu 🤣",
    "Lương 16 là chân ái 😳",
    "Chuẩn bị bung nóc ăn mừng 💸",
    "Sắp hết khổ rồi {name} 😭",
    "Ví đang run rẩy háo hức 💰",
    "Tới ngày nạp tiền rồi 😝",
    "Sắp trả được nợ chưa 😆",
    "Bot chúc bạn tháng này không âm 😭",
]


# ===== ĂN CƠM =====
ANCOM_FUNNY = [
    "Nhớ ăn cơm cho khỏe nha 😄",
    "Đừng nhịn đói tội nghiệp cái bụng 😭",
    "Bụng reo rồi kìa {name} 😳",
    "Đi ăn lẹ đi không xỉu 😭",
    "Hôm nay ăn gì ngon chưa 😆",
    "Ăn cơm cho có sức cày chứ 😝",
    "Đừng làm việc quên ăn đó nha 🍚",
    "Ăn cơm vô cho ấm bụng ✨",
    "Tới giờ nạp năng lượng nè 🔋",
    "Đi ăn lẹ lên bot đói ké rồi 😭",
]
