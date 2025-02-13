import logging
from asgiref.sync import sync_to_async
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, filters, ConversationHandler, CallbackContext
from TelegramBot.models import TGUser


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

NAME, LAST_NAME, POSITION, SAP_NUMBER, CONFIRM = range(5)


async def start(update: Update, context: CallbackContext) -> int:
    user_id = update.message.from_user.id
    if await sync_to_async(TGUser.objects.filter(user_id=user_id).exists)():
        await update.message.reply_text('Приветствую. Используй /help для помощи!')
        return ConversationHandler.END
    else:
        await update.message.reply_text('''
Приветствую\. Я Digital\-бот \- твой маленький друг помогающий в доставке\.
Давай познакомимся с тобой\. я задам тебе несколько вопросов\.
```Регистрация:
Имя\:
```''', 'MarkdownV2')

        return NAME

# Функция для получения имени
async def get_name(update: Update, context: CallbackContext) -> int:
    context.user_data['first_name'] = update.message.text
    await update.message.reply_text('''
```Регистрация:
Фамилия\:
```''', 'MarkdownV2')
    return LAST_NAME

# Функция для получения фамилии
async def get_last_name(update: Update, context: CallbackContext) -> int:
    context.user_data['last_name'] = update.message.text
    reply_keyboard = [['Продавец-кассир', 'Сборщик заказов', 'Администратор магазина', 'Директор магазина', 'Гость']]
    await update.message.reply_text('''
```Регистрация:
Ваша должность\:
```''', 'MarkdownV2', reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return POSITION

# Функция для получения должности
async def get_position(update: Update, context: CallbackContext) -> int:
    context.user_data['position'] = update.message.text
    await update.message.reply_text('''
```Регистрация:
ТОРГ(SAP) магазина\:
Если вы ГОСТЬ то введите\: 0 
```''', 'MarkdownV2')
    return SAP_NUMBER

# Функция для получения SAP номера
async def get_sap_number(update: Update, context: CallbackContext) -> int:
    context.user_data['sap_number'] = update.message.text
    user_data = context.user_data
    confirmation_message = (
        f"Подтвердите ваши данные: \n"
        f"Имя: {user_data['first_name']} \n"
        f"Фамилия: {user_data['last_name']} \n"
        f"Должность: {user_data['position']} \n"
        f"ТОРГ номер: {user_data['sap_number']} \n"
        f"Подтвердите (да/нет):"
    )
    await update.message.reply_text(confirmation_message)
    return CONFIRM

# Функция для подтверждения данных
async def confirm(update: Update, context: CallbackContext) -> int:
    if update.message.text.lower() == 'да':
        user_data = context.user_data
        await sync_to_async(TGUser.objects.create)(
            user_id=update.message.from_user.id,
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            position=user_data['position'],
            sap_number=user_data['sap_number']
        )
        await update.message.reply_text('Ваши данные сохранены. Спасибо!')
    else:
        await update.message.reply_text('Пожалуйста, начните заново. /start')
    return ConversationHandler.END

# Функция для отмены разговора
async def cancel(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text('Отменено. /start для начала заново.')
    return ConversationHandler.END

def registration_handler():
    return ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
            LAST_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_last_name)],
            POSITION: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_position)],
            SAP_NUMBER: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_sap_number)],
            CONFIRM: [MessageHandler(filters.TEXT & ~filters.COMMAND, confirm)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
