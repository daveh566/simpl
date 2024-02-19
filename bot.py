import logging
import telegram

# Replace with your actual Telegram bot token
BOT_TOKEN = "6733000714:AAG1Q6G_KxJqmQ535SyY1ftU-FoLnpXotyA"

# Replace with a list of admin chat IDs
ADMIN_CHAT_IDS = [5002238436, 987654321]

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def handle_request(update, context):
    chat_id = update.effective_chat.id
    user_id = update.message.from_user.id
    username = update.message.from_user.username

    message_text = update.message.text.split(" ", 1)[1] if len(update.message.text.split()) > 1 else ""

    message = f"Request from: @{username} (ID: {user_id})\n"
    message += f"Chat ID: {chat_id}\n"
    message += f"Message: {message_text}"

    for admin_chat_id in ADMIN_CHAT_IDS:
        try:
            context.bot.send_message(chat_id=admin_chat_id, text=message)
        except telegram.error.TelegramError as e:
            logging.error(f"Failed to send message to admin {admin_chat_id}: {e}")

    update.message.reply_text("Your request has been sent to the admins.")


def main():
    updater = telegram.Updater(token=BOT_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(telegram.CommandHandler("request", handle_request))

    updater.start_polling()
    updater.idle()


if name == 'main':
    main()￼Enter
