from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    CallbackQueryHandler, ContextTypes, filters
)

user_state = {}

# Универсальная функция старта (работает и через /start, и через кнопку)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = (
        update.message.from_user.id if update.message
        else update.callback_query.from_user.id
    )
    user_state[user_id] = {}

    if update.message:
        await update.message.reply_text("Привет! Введите цену входа:")
    elif update.callback_query:
        await update.callback_query.answer()
        await update.callback_query.message.reply_text("Привет! Введите цену входа:")

# Обработка текстовых сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    text = update.message.text

    if user_id not in user_state:
        await update.message.reply_text("Напишите /start, чтобы начать.")
        return

    state = user_state[user_id]

    if "price" not in state:
        try:
            price = float(text.replace(",", "."))
            state["price"] = price
            await update.message.reply_text("Теперь введите ренту в процентах (например, 18.5):")
        except ValueError:
            await update.message.reply_text("Пожалуйста, введите корректную цену.")
    elif "rent" not in state:
        try:
            rent = float(text.replace(",", "."))
            if rent >= 100:
                await update.message.reply_text("Рента должна быть меньше 100%. Попробуйте снова.")
                return
            state["rent"] = rent

            result = state["price"] / (1.0 - (rent / 100.0))
            await update.message.reply_text(
                f"Расчёт:\n{state['price']} / (1 - {rent / 100}) = {round(result, 2)}"
            )

            # Кнопка "Рассчитать ещё"
            keyboard = [[InlineKeyboardButton("Рассчитать ещё", callback_data="restart")]]
            await update.message.reply_text("Хотите рассчитать ещё?", reply_markup=InlineKeyboardMarkup(keyboard))

            user_state.pop(user_id)
        except ValueError:
            await update.message.reply_text("Пожалуйста, введите ренту числом (например, 18.5).")
    else:
        await update.message.reply_text("Что-то пошло не так. Напишите /start чтобы начать заново.")

# Обработка нажатия кнопки "Рассчитать ещё"
async def restart_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start(update, context)

if __name__ == '__main__':
    TOKEN = "8133544064:AAH-N8DDF9D13QZUi9Y_STrRm9eHPsG2RZw"

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(restart_callback, pattern="^restart$"))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен...")
    app.run_polling()