import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import uuid

# Включение логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Словарь для хранения описаний
descriptions = {}

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Введите текст описания для вашей платежной страницы:')

def handle_description(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    description = update.message.text
    
    # Генерация уникального ID и сохранение описания
    unique_id = str(uuid.uuid4())
    descriptions[unique_id] = description
    
    # Отправка ссылки пользователю
    link = f"https://understood-lopsided-attention.glitch.me/{unique_id}"  # Замените на ваш URL сервера
    update.message.reply_text(f'Ваша уникальная ссылка на страницу платежа:n{link}')

def main() -> None:
    updater = Updater("7942218008:AAGGgSSYs8biWj1cNEWFEjcmyIoxjPRYOY0")  # Замените на токен вашего бота

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_description))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()