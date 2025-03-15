import asyncio
import datetime
from telethon import TelegramClient, functions
from pytz import timezone

# اطلاعات ورود (از my.telegram.org بگیرید)
API_ID = 28867710  # مقدار خود را جایگزین کنید
API_HASH = "de07b25a33ab51e759b9eb8041a52cfc"

# نام اصلی شما
BASE_NAME = "𝗡𝗲𝘅𝗦𝗮𝘃𝗶𝗼𝗿"

# استایل ثابت برای اعداد
FANCY_NUMBERS = {"0": "⓪", "1": "①", "2": "②", "3": "③", "4": "④", 
                 "5": "⑤", "6": "⑥", "7": "⑦", "8": "⑧", "9": "⑨"}

# تابع تبدیل اعداد به استایل ثابت
def fancy_numbers(number_str):
    return "".join(FANCY_NUMBERS.get(d, d) for d in number_str)

async def update_name():
    async with TelegramClient("session", API_ID, API_HASH) as client:
        while True:
            # گرفتن زمان ایران
            iran_time = datetime.datetime.now(timezone("Asia/Tehran"))
            formatted_time = fancy_numbers(iran_time.strftime("%H:%M"))

            # ساختن نام جدید
            new_name = f"↬{BASE_NAME} {formatted_time}"

            # تغییر نام در تلگرام
            try:
                await client(functions.account.UpdateProfileRequest(first_name=new_name))
                print(f"✅ نام تغییر کرد به: {new_name}")
            except Exception as e:
                print(f"⚠️ خطا: {e}")

            # صبر برای یک دقیقه
            await asyncio.sleep(60)

# اجرای تابع
asyncio.run(update_name())
