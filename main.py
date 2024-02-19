import logging
import telebot

# Replace with your actual Telegram bot token
BOT_TOKEN = "6733000714:AAG1Q6G_KxJqmQ535SyY1ftU-FoLnpXotyA"

# Replace with a list of admin chat IDs or usernames
ADMIN_CHAT_IDS = ["5002238436", "admin2_username"]

logging.basicConfig(level=logging.INFO)

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["request"])
def handle_request(message):
    """Handles the /request command from users."""

    user_id = message.chat.id
    username = message.from_user.username or message.from_user.first_name
    text = message.text.strip()

    # Extract request message after the command (if any)
    request_message = text[len("/request"):].strip() or "Empty request message."

    # Construct the message to send to admins
    admin_message = f"Request from: {username} ({user_id})\n\n{request_message}"

    # Send the message to each admin
    for admin_chat_id in ADMIN_CHAT_IDS:
        try:
            bot.send_message(admin_chat_id, admin_message, parse_mode="Markdown")
            logging.info(f"Successfully sent request to admin: {admin_chat_id}")
        except Exception as e:
            logging.error(f"Failed to send request to admin {admin_chat_id}: {e}")

    # Send a confirmation message to the user
    bot.reply_to(message, "Your request has been sent to the admins.")

if __name__ == "main":
    bot.polling()
