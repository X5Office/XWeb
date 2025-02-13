from telegram import Update
from telegram.ext import ContextTypes
from asgiref.sync import sync_to_async
from TelegramBot.models import TGUser

async def cdm_shift(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = await sync_to_async(TGUser.objects.get)(user_id=update.effective_user.id)
    if user.is_store_admin:
        args = context.args
        if len(args) < 1:
            await update.message.reply_text(
                text='''Режим смены
В данном режиме вы будете получать оповещения о всех запросах маркировки соотрудниками вашего магазина\. Вы так же будете получать причину\, по которой пользователь запросил данный код\.
Для входа в режим смены \(её открытия\) используйте эту команду с аргументом start\, для отключения stop
            ''',
                parse_mode='MarkdownV2'
            )
            return
        mode = args[0]

        if mode == 'start':
            user.admin_mode = True
            await sync_to_async(user.save)()
            await update.message.reply_text(
                text='Смена успешно открыта\! Теперь вы будете получать уведомления о действиях сотрудников\!',
                parse_mode='MarkdownV2'
            )
            return
        elif mode == 'stop':
            user.admin_mode = False
            await sync_to_async(user.save)()
            await update.message.reply_text(
                text='Смена закрыта\. Уведомления отключены\!',
                parse_mode='MarkdownV2'
            )
            return
        else:
            await update.message.reply_text(
                text='''ПРОИЗОШЛА ОШИБКА
Режим смены
В данном режиме вы будете получать оповещения о всех запросах маркировки соотрудниками вашего магазина\. Вы так же будете получать причину\, по которой пользователь запросил данный код\.
Для входа в режим смены \(её открытия\) используйте эту команду с аргументом start\, для отключения stop
                        ''',
                parse_mode='MarkdownV2'
            )
            return
