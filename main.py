import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

TOKEN = os.getenv("TOKEN")

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return
    
    text = update.message.text

    if "مستجد" in text:
        await update.message.reply_text(
            "أهلاً بك 👋\n\n📚 دليل المستجدين:\n- القوانين\n- التسجيل\n- الجداول\n\nإذا تحتاج شيء اسأل 👍"
        )

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT, reply))
    print("Bot is running...")
    app.run_polling()
  
