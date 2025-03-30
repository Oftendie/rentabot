Создай файл в корне проекта:

bash
Копировать
Редактировать
touch README.md
Открой и вставь:

markdown
Копировать
Редактировать
# 📊 Rentabot — Telegram-бот для расчёта рентабельности

Этот Telegram-бот помогает рассчитать сумму на основе "Цены входа" и "Ренты" (в процентах) по следующей формуле:

Цена / (1 - (Рента / 100))

markdown
Копировать
Редактировать

## 🚀 Как использовать

1. Напиши боту команду `/start`
2. Введи цену входа (например: `150000`)
3. Введи ренту в процентах (например: `18.5`)
4. Бот покажет расчёт и предложит кнопку "Рассчитать ещё"

## 📦 Установка

### 1. Клонируй репозиторий:

```bash
git clone https://github.com/Oftendie/rentabot.git
cd rentabot
2. Создай виртуальное окружение:
bash

python3 -m venv .venv
source .venv/bin/activate
3. Установи зависимости:
bash

pip install python-telegram-bot
4. Укажи свой Telegram-токен в bot.py:
python

TOKEN = "ТВОЙ_ТОКЕН_ЗДЕСЬ"
(или подключи .env, если хочешь безопасно хранить ключи 🔐)

5. Запусти бота:
bash

python bot.py
🛠 Стек технологий
Python 3

python-telegram-bot

💡 Пример расчёта
Ввод:

Цена входа: 150000

Рента: 18.5

Вывод:

makefile

Расчёт:
150000 / (1 - 0.185) = 184049.08
🧾 Лицензия
Проект распространяется под лицензией MIT.

yaml

