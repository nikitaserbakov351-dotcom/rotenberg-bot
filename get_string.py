from telethon import TelegramClient
from telethon.sessions import StringSession
import asyncio

# Твои данные
API_ID = 34855836
API_HASH = "505884cacfad99610d616c2bc1e200d4"
SESSION_FILE = "rotenberg_session"  # Твой файл сессии


async def main():
    print("🔍 Подключаюсь к существующей сессии...")

    # Используем файловую сессию
    client = TelegramClient(SESSION_FILE, API_ID, API_HASH)

    try:
        await client.connect()

        # Проверяем авторизацию
        if not await client.is_user_authorized():
            print("❌ Сессия не авторизована. Сначала запусти main.py для авторизации.")
            return

        # Получаем информацию об аккаунте
        me = await client.get_me()
        print(f"✅ Подключен как: {me.first_name} (@{me.username})")

        # Получаем строковую сессию
        string_session = client.session.save()

        print("\n" + "=" * 70)
        print("✅ СТРОКОВАЯ СЕССИЯ ДЛЯ RAILWAY:")
        print("=" * 70)
        print(string_session)
        print("=" * 70)

        # Сохраняем в файл
        with open("RAILWAY_SESSION.txt", "w", encoding="utf-8") as f:
            f.write(string_session)
        print("\n💾 Также сохранено в RAILWAY_SESSION.txt")

    except Exception as e:
        print(f"❌ Ошибка: {e}")
    finally:
        await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())