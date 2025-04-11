from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackContext,
    CallbackQueryHandler,
)

TOKEN = "7884086010:AAGrQ3Dwv7twbgw0YpeFFLz_nQRB6XsEL6E"

# ساختار دیتابیس با File IDهای ویدیوها
PAYETAKHT7 = {
    "سریال۱": {
        "قسمت 1": {
            "360": "AAMCBAADGQEB6GkRZ-2OeJ2TX4nAimwDOfdYcb7tfaYAAmkaAAK8KhFTlz9vzzmxKkYBAAdtAAM2BA",
            "480": "AAMCBAADGQEB6GkSZ-2OeI7liJY6LzvkHmmNpAt0eHEAAiwaAAKfdBFT4QMtIhzlazQBAAdtAAM2BA",
            "720": "AAMCBAADGQEB6GkTZ-2OeCaJJZOqmKoqyU8onaGmPcoAArEaAALIVRBTLF7hq_2x7PYBAAdtAAM2BA",
            "1080": "AAMCBAADGQEB6GkVZ-2OeJjPc5oY-AugoDsdB0ULT0EAArYaAALIVRBTNhe4ba5irp4BAAdtAAM2BA",
        },
        "قسمت 2": {
            "360": "AAMCBAADGQEB6GpOZ-2VDO2VYBdRP1ksj4cuvJlfvQIAAukWAAJihhlTShM2sHZddS4BAAdtAAM2BA",
            "480": "AAMCBAADGQEB6GpPZ-2VDLfNXRQ956TfYqSI95PUj_4AAtgaAAK0BxhTgqo6uKjDR-EBAAdtAAM2BA",
            "720": "AAMCBAADGQEB6GpQZ-2VDNB5_Vcn-0o9i6Yh8jCRxdQAAi4XAAJUmxlTJEudc9iEUSkBAAdtAAM2BA",
            "1080": "AAMCBAADGQEB6GpRZ-2VDF5IuWKNY8xQCaVZTrhPGNoAAt0aAAK0BxhT7XldX3aEx4gBAAdtAAM2BA",
        },
        "قسمت 3": {
            "360p": "AAMCBAADGQEB6GqSZ-2WUqDd-2oto7jV2Gm3KI0eyPgAAikWAALMeyFTridyYM57kpQBAAdtAAM2BA",
            "480p": "AAMCBAADGQEB6GqTZ-2WUncyZUGmHDWFETPQIz1D-gEAAjYcAAIMNSBTz2Nf2zNzXecBAAdtAAM2BA",
            "720p": "AAMCBAADGQEB6GqUZ-2WUgVYczaVtRKaVEYIHkQGwrUAAkIdAAIMNSBTjIZCexKITD8BAAdtAAM2BA",
            "1080p": "AAMCBAADGQEB6GqWZ-2WUl8G02w1O9FnsBx5MbGaRvoAAuAXAAIZvyBTFl4yPix7ghMBAAdtAAM2BA",
        },
        "قسمت 4": {
            "360p": "AAMCBAADGQEB6GrTZ-2XgVVisR--80d4J0rV9MFrKBQAAo4ZAAIWyjBTxUXBLETvdhsBAAdtAAM2BA",
            "480p": "AAMCBAADGQEB6GrUZ-2XgajEa8kZffJWh8O7ZemdS_kAApccAAO3MVM5MunSsjBmOwEAB20AAzYE",
            "720p": "AAMCBAADGQEB6GrVZ-2XgYprPW_6G3-GXgOGNIJzlSEAApocAAO3MVOdXymDoWId1gEAB20AAzYE",
            "1080p": "AAMCBAADGQEB6GrWZ-2XgYLDbqMHTA-9CEEB8HGtersAArMcAAO3MVNfWqtd9P1PXQEAB20AAzYE",
        },
        "قسمت 5": {
            "360p": "AAMCBAADGQEB6Gs2Z-2Ye0tOwH0zL7KFHP4tBrNklYcAAq0ZAAKooTlToLZfvByn54cBAAdtAAM2BA",
            "480p": "AAMCBAADGQEB6Gs3Z-2Ye6Kz6k3xV4cdTdUq2AYgw7oAAq4ZAAKooTlT4dXHhBbrUzMBAAdtAAM2BA",
            "720p": "AAMCBAADGQEB6Gs5Z-2Ye2SlRciuVEMGHn9ZJIH0OvcAArIZAAKooTlTnRCrQt3PSwoBAAdtAAM2BA",
            "1080p": "AAMCBAADGQEB6Gs6Z-2Ye5iRTzzK5GdjURXTU5a5YHsAAvwXAAL4GDhTEsu5w25mxDcBAAdtAAM2BA",
        },
        "قسمت 6": {
            "360p": "AAMCBAADGQEB6GttZ-2ZLPcUqI3iGHOJ5UH5UvCHL8YAAt4aAAKJAkFTyTY453J2bJ8BAAdtAAM2BA",
            "480p": "AAMCBAADGQEB6GtuZ-2ZLIeJ804gWoNaPGYXKbQAAWmsAAIxHgAC0JRIUwhaeK0_OEXHAQAHbQADNgQ",
            "720p": "AAMCBAADGQEB6GtvZ-2ZLKCPWJjtUyvsE0xEdTjSZoAAAtYYAAK0skhT8Hl2eD3YyoYBAAdtAAM2BA",
            "1080p": "AAMCBAADGQEB6GtwZ-2ZLOTM4UJdpps-Cg-aHg9aBgoAAtEaAAJY3ElTQLw-58dCjbwBAAdtAAM2BA",
        },
        "قسمت 7": {
            "360p": "AAMCBAADGQEB6GvtZ-2bC5gxyvJbuBiJYsCa_nyFhDQAAq8XAAL1wFBT012SfRBw9McBAAdtAAM2BA",
            "480p": "AAMCBAADGQEB6GvuZ-2bC-ArBfERp_5L3mjvC0-U93EAAocYAAKv2FBTLi9a59eVrJMBAAdtAAM2BA",
            "720p": "AAMCBAADGQEB6GvvZ-2bCxZbJVcC5hhxh1yGc9tqtPUAApwWAAJVEEhTq9Av3G33MdUBAAdtAAM2BA",
            "1080p": "AAMCBAADGQEB6GvwZ-2bC1GHa_zDrdcqFjjTPSAptyEAAt8ZAAJj30hTi3JTE3I9-bEBAAdtAAM2BA",
        },
        "قسمت 8": {
            "360p": "AAMCBAADGQEB6GwlZ-2b9t9QrCxGToxYhV2ffoT67k4AAvUXAAK5AVhTK8IZKAnpnckBAAdtAAM2BA",
            "480p": "AAMCBAADGQEB6GwnZ-2b9mAlwtBXpf5fZo1C3PdFt4EAAvIXAAK5AVhTk4YahLeYZpwBAAdtAAM2BA",
            "720p": "AAMCBAADGQEB6GwmZ-2b9sOHdtuPN5k4TqmlzwZj6EUAAvAXAAK5AVhTBkDosdyqjCcBAAdtAAM2BA",
            "1080p": "AAMCBAADGQEB6GwoZ-2b9mOhwmukXqlHYDdyC4GLHPIAAtkYAAKvUllTvApsSBIUILABAAdtAAM2BA",
        },
        "قسمت 9": {
            "360p": "AAMCBAADGQEB6GxJZ-2cgUel-kBktpYk-iVIhU3A6IwAApomAAIRyGBTBchT_9bEvwMBAAdtAAM2BA",
            "480p": "AAMCBAADGQEB6GxKZ-2cge_Dh6iDmr_FYyvRMxYpPhcAAqkaAAKoJGhTS2mKPx_jnYUBAAdtAAM2BA",
            "720p": "AAMCBAADGQEB6GxLZ-2cgV7k8g1E0PtXHXj4vKzVkgwAAnoYAALaNmlTJAqXYJXdz28BAAdtAAM2BA",
            "1080p": "AAMCBAADGQEB6GxMZ-2cgV80t0Kdk4zz4ndRVThA2b8AAjgYAAIzGmFTu92YdyhCJcQBAAdtAAM2BA",
        },
        "قسمت 10": {
            "360p": "AAMCBAADGQEB6IUnZ-34oKicpd6wdCwiWeUasZMG26gAAgMaAAJMSnBTv-cH2xZBC6wBAAdtAAM2BA",
            "480p": "AAMCBAADGQEB6IUoZ-34oAgs8teJfeqXbaXradTMdQkAAnkaAALaNnFTtfTNS35s5DEBAAdtAAM2BA",
            "720p": "AAMCBAADGQEB6IUpZ-34oPzwq_bPR5ypRRr-KCofOzYAAkwYAAIkeWhTeDESo7tKKcQBAAdtAAM2BA",
            "1080p": "AAMCBAADGQEB6IUqZ-34oDlh9yvIqYe6K0JLPwl5j2UAAsgbAAKoJHBT_VKu3o9aztgBAAdtAAM2BA",
        },
        # سایر قسمتها به همین شکل اضافه شوند
    }
}

def start(update: Update, context: CallbackContext):
    """منوی اصلی با دکمههای اینلاین"""
    keyboard = [
        [InlineKeyboardButton("قسمت 1", callback_data="ep_1")],
        [InlineKeyboardButton("قسمت 2", callback_data="ep_2")],
        [InlineKeyboardButton("قسمت 3", callback_data="ep_3")],
        [InlineKeyboardButton("قسمت 4", callback_data="ep_4")],
        [InlineKeyboardButton("قسمت 5", callback_data="ep_5")],
        [InlineKeyboardButton("قسمت 6", callback_data="ep_6")],
        [InlineKeyboardButton("قسمت 7", callback_data="ep_7")],
        [InlineKeyboardButton("قسمت 8", callback_data="ep_8")],
        [InlineKeyboardButton("قسمت 9", callback_data="ep_9")],
        [InlineKeyboardButton("قسمت 10", callback_data="ep_10")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("🎬 خوش آمدید! لطفا یک قسمت انتخاب کنید:", reply_markup=reply_markup)

def handle_episode(update: Update, context: CallbackContext):
    """مدیریت انتخاب قسمت"""
    query = update.callback_query
    episode_num = query.data.split("_")[1]
    episode_name = f"قسمت {episode_num}"
    
    # ذخیره قسمت انتخابی کاربر
    context.user_data["episode"] = episode_name
    
    # ایجاد کیبورد کیفیتها
    keyboard = [
        [
            InlineKeyboardButton("360p", callback_data="quality_360"),
            InlineKeyboardButton("480p", callback_data="quality_480"),
        ],
        [
            InlineKeyboardButton("720p", callback_data="quality_720"),
            InlineKeyboardButton("1080p", callback_data="quality_1080"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        f"⚙️ کیفیت مورد نظر برای {episode_name} را انتخاب کنید:", reply_markup=reply_markup
    )

def handle_quality(update: Update, context: CallbackContext):
    """مدیریت انتخاب کیفیت و ارسال ویدیو"""
    query = update.callback_query
    quality = query.data.split("_")[1]
    episode_name = context.user_data.get("episode", "قسمت نامشخص")
    
    # دریافت File ID از دیتابیس
    try:
        file_id = PAYETAKHT7["سریال۱"][episode_name][quality]
        query.message.reply_video(
            video=file_id, caption=f"🎥 {episode_name} - کیفیت {quality}p"
        )
    except KeyError:
        query.message.reply_text("⚠️ خطا در یافتن ویدیو!")

def main():
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_episode, pattern="^ep_"))
    application.add_handler(CallbackQueryHandler(handle_quality, pattern="^quality_"))
    
    application.run_polling()

if str == "__main__":
    main()