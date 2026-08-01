from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

# ==========================
BOT_TOKEN = "6448421534:AAHSOnlOuUMg4wNpvCsbFws_TRR9H4VCfDQ"

# الجروب اللي هياخد منه الرسائل
SOURCE_GROUP = -1003737762174

# الجروب اللي هيبعتله الرسائل
DEST_GROUP = -1003917198393
# ==========================


async def forward(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("وصل Update")

    if not update.message:
        print("دي مش رسالة")
        return

    print("Chat ID:", update.effective_chat.id)

    if update.effective_chat.id != SOURCE_GROUP:
        print("الرسالة من جروب تاني")
        return

    try:
        await context.bot.copy_message(
            chat_id=DEST_GROUP,
            from_chat_id=SOURCE_GROUP,
            message_id=update.message.message_id
        )
        print("Copied Successfully")
    except Exception as e:
        print("Error:", e)


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(
        MessageHandler(filters.ALL & ~filters.StatusUpdate.ALL, forward)
    )

    print("Bot Started...")
    app.run_polling()


if __name__ == "__main__":
    main()
