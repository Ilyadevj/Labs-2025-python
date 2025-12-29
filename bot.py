from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler

NAME, AGE = range(2)

async def start(update: Update, context):
    await update.message.reply_text("Привет! Как тебя зовут?")
    return NAME

async def get_name(update: Update, context):
    user_name = update.message.text
    context.user_data['name'] = user_name
    await update.message.reply_text(f"Привет, {user_name}! Сколько тебе лет?")
    return AGE

async def get_age(update: Update, context):
    user_age = update.message.text
    
    if not user_age.isdigit():
        await update.message.reply_text("Пожалуйста, введите число!")
        return AGE
    
    context.user_data['age'] = user_age
    name = context.user_data['name']
    
    await update.message.reply_text(f"Отлично! Твои данные:\nИмя: {name}\nВозраст: {user_age}")
    
    with open('users.txt', 'a') as f:
        f.write(f"{name}: {user_age}\n")
    
    await update.message.reply_text("Данные сохранены! Напиши /start чтобы начать заново")
    return ConversationHandler.END

async def cancel(update: Update, context):
    await update.message.reply_text("Диалог прерван")
    return ConversationHandler.END

def main():
    TOKEN = "8530282914:AAGL_N6PdjHhDUvsAlhDh9HMMrUxUfwPawc"
    
    app = Application.builder().token(TOKEN).build()
    
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
            AGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_age)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    
    app.add_handler(conv_handler)
    app.run_polling()

if __name__ == '__main__':
    main()