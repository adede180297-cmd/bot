import random
from datetime import datetime, timedelta, timezone

# ================== GIỜ VIỆT NAM ==================
VN_TIME = timezone(timedelta(hours=7))

def now_vn():
    return datetime.now(VN_TIME)

# ================== NGÀY CỐ ĐỊNH ==================
target_date_tet = datetime(2026, 2, 17, tzinfo=VN_TIME)
target_date_noel = datetime(2025, 12, 25, tzinfo=VN_TIME)

# ================== LẤY TÊN USER ==================
def get_name(update):
    u = update.message.from_user
    return u.first_name or "Bạn"

# ================== RANDOM CÂU TRẢ LỜI ==================
def pick(arr, name):
    msg = random.choice(arr)
    return msg.replace("{name}", name)

# ================== 10 CÂU HÀI HƯỚC ==================
MOOD_FUNNY = [
    "Hôm nay bot vui dữ lắm 😆",
    "Bot đang trong mood đỉnh cao 😎",
    "Năng lượng bot đang 200% 🔥",
    "Bot tỉnh như sáo luôn 🤣",
    "Bot đang rất chi là phấn khởi 😝",
    "Hôm nay bot đẹp trai lạ thường 😏",
    "Bot đang rung chuyển cảm xúc 🌪️",
    "Bot vui quá muốn nhảy hiphop 💃",
    "Tâm trạng bot như mặt trời giữa trưa 🌞",
    "Bot đang tung tăng như con cá 🐟"
]

TET_FUNNY = [
    "Tết đến nơi rồi đóoooo 🎉",
    "Chuẩn bị dọn nhà chưa {name}? 🤣",
    "Bao lì xì đâu, bot đòi nè 😆",
    "Tết này nhớ cười nhiều nha {name} 😄",
    "Không khí Tết đang áp sát 🚀",
    "Tết mà vui là phải ăn nhiều 😋",
    "{name} nhớ sắm đồ mới nha 👗",
    "Tết tới nơi rồi mà tiền chưa tới 😭",
    "Không khí Tết thơm mùi bánh chưng 😍",
    "Xuân sắp gõ cửa mạnh lắm rồi 🌸"
]

NOEL_FUNNY = [
    "Noel tới nơi rồi đóooo 🎄",
    "Bạn trang trí cây thông chưa? 🎅",
    "Santa đang chuẩn bị quà cho {name} 😆",
    "Không khí Noel lạnh mà tim thì ấm ❤️",
    "Chuẩn bị đi chơi Noel chưa nè ❄️",
    "Tuyết không có nhưng Noel vẫn chill ☃️",
    "Noel mà độc thân thì nhắn bot chơi nè 😭",
    "Ông già Noel đang đến kìa 🎁",
    "Noel tới là có gấu liền nha (bot nói vậy thôi 😝)",
    "Đi chơi Noel nhớ mặc ấm nha {name} 💙"
]

XUONGCA_FUNNY = [
    "Sắp được về rồi, cố lennn 😭",
    "Nghĩ đến cái giường mà muốn xỉu 😴",
    "Tự do sắp vẫy gọi bạn 📢",
    "Ráng xíu nữa thôi là được bung 😎",
    "Chuẩn bị cúp máy làm đẹp trai lại 😆",
    "Đồng hồ điểm về nhà là hạnh phúc 🔥",
    "Bạn sắp thoát kiếp lao động 😭",
    "Thêm chút nữa thôi là tự do 🕊️",
    "Nghĩ đến bữa ăn tối mà ham quá 🤤",
    "{name}, sẵn sàng chạy khỏi chỗ làm chưa? 🤣"
]

LUONG_FUNNY = [
    "Sắp hết nghèo rồi đó 😭",
    "Ví tiền sắp sống lại 🔥",
    "Chuẩn bị ăn sang nha {name} 😎",
    "Thiếu nợ ai thì trốn đi 😭",
    "Lương sắp về, vui dữ dội 😆",
    "Ví bạn sắp mập lên rồi 🐷",
    "Tiền vô rồi lại đi liền 😭",
    "Mua gì nhớ rủ bot 😝",
    "Sắp có tiền mua trà sữa rồi nè 🧋",
    "Chuẩn bị giàu 5 phút đầu tháng 🤣"
]

ANCOM_FUNNY = [
    "Đi ăn cơm lẹ đi {name} 😆",
    "Đói bụng là buồn lắm đó 😭",
    "Đi ăn cho có sức làm tiếp 💪",
    "Trưa rồi, bụng biểu tình chưa? 🍚",
    "Ăn cơm đi rồi bot thương 😭",
    "Nhịn đói là không vui đâu nha 😢",
    "Đi ăn đi rồi quay lại tám tiếp 🤣",
    "Tới giờ nạp năng lượng rồi ⚡",
    "Ăn cơm xong nhớ rửa chén nha 😝",
    "Đi ăn lẹ đi, để bụng đói tội nghiệp 😭"
]
