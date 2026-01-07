from telethon.sessions import StringSession
from telethon import TelegramClient

# Твои данные из .env
API_ID = 34855836
API_HASH = "505884cacfad99610d616c2bc1e200d4"
SESSION_FILE = "rotenberg_session"

print("🔍 Ищу существующую сессию...")

try:
    # Подключаемся к уже существующей сессии
    with TelegramClient(SESSION_FILE, API_ID, API_HASH) as client:
        # Преобразуем файловую сессию в строковую
        string_session = client.session.save()

        print("\n" + "=" * 70)
        print("✅ СТРОКОВАЯ СЕССИЯ УСПЕШНО ПОЛУЧЕНА!")
        print("=" * 70)
        print("\n📋 СКОПИРУЙТЕ ВСЮ СТРОКУ НИЖЕ:")
        print("=" * 70)
        print(string_session)
        print("=" * 70)

        # Также сохраняем в файл для безопасности
        with open("SESSION_STRING.txt", "w", encoding="utf-8") as f:
            f.write(string_session)
        print("\n💾 Сессия также сохранена в файл: SESSION_STRING.txt")

except Exception as e:
    print(f"\n❌ ОШИБКА: {e}")
    print("\nВозможные причины:")
    print("1. Файл rotenberg_session не найден в текущей папке")
    print("2. Сессия устарела или повреждена")
    print("\nРешение:")
    print("Запустите бота через main.py, чтобы создать новую сессию")