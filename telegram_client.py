import asyncio
import logging
import random
import sys
import os  # ДОБАВЬТЕ ЭТУ СТРОКУ!
from typing import Optional
from datetime import datetime

from telethon import TelegramClient, events
from telethon.tl.functions.messages import SendReactionRequest
from telethon.tl.types import ReactionEmoji, PeerUser
from telethon.errors import FloodWaitError
from telethon.sessions import StringSession  # ДОБАВЬТЕ ЭТУ СТРОКУ!

from brain import RotenbergBrain

logger = logging.getLogger(__name__)


class TelegramClientHandler:
    """Обработчик Telegram-клиента"""

    def __init__(self, config, brain: RotenbergBrain):
        self.config = config
        self.brain = brain
        self.client: Optional[TelegramClient] = None
        self.is_running = True
        self.me = None

    async def start(self):
        """Запуск клиента"""
        try:
            print("🔧 Инициализация Telegram клиента...")

            # СОЗДАЁМ СТРОКОВУЮ СЕССИЮ
            string_session = StringSession(self.config.SESSION_NAME)

            self.client = TelegramClient(
                session=string_session,  # ИСПОЛЬЗУЕМ СТРОКОВУЮ СЕССИЮ!
                api_id=self.config.API_ID,
                api_hash=self.config.API_HASH,
                device_model="RotenbergBot",
                system_version="Linux",
                app_version="2.0.0",
                lang_code="ru",
                system_lang_code="ru"
            )

            print("✅ Клиент создан")

            # Настройка обработчиков
            self.setup_handlers()

            # Подключение
            print("📡 Подключаюсь к Telegram...")
            await self.client.connect()

            # Проверка авторизации (ВАЖНОЕ ИЗМЕНЕНИЕ!)
            if not await self.client.is_user_authorized():
                print("❌ ОШИБКА: Сессия недействительна или устарела!")
                print("ℹ️  Получите новую сессию:")
                print("   1. Запустите get_string.py на своем компьютере")
                print("   2. Скопируйте новую строку сессии")
                print("   3. Обновите переменную SESSION_NAME в Railway")
                raise ValueError("Недействительная сессия")

            # Получаем информацию о себе
            self.me = await self.client.get_me()
            print(f"\n✅ АВТОРИЗОВАН КАК: {self.me.first_name} (@{self.me.username})")
            print("=" * 40)

            # Запускаем фоновые задачи
            asyncio.create_task(self._keep_alive())

            # Информационное сообщение
            print("\n🚀 БОТ ЗАПУЩЕН И ГОТОВ К РАБОТЕ!")
            print("👉 Напишите вашему аккаунту в Telegram")
            print("💬 Бот будет отвечать в стиле Романа Ротенберга")
            print("⏹️  Для остановки нажмите Ctrl+C")
            print("=" * 40 + "\n")

            # Бесконечный цикл ожидания
            await self._run_forever()

        except Exception as e:
            logger.error(f"❌ Ошибка запуска: {e}")
            raise

    def setup_handlers(self):
        """Настройка обработчиков событий"""
        @self.client.on(events.NewMessage(incoming=True))
        async def message_handler(event):
            await self._handle_message(event)

    # УДАЛИТЕ МЕТОД _perform_login ВОВСЕ! Он больше не нужен.

    async def _handle_message(self, event):
        """Обработка входящих сообщений"""
        try:
            # Пропускаем служебные сообщения
            if not event.message or event.message.out:
                return

            # Получаем информацию об отправителе
            sender = await event.get_sender()
            if not sender:
                return

            # Логируем
            msg_preview = event.message.text[:50] + "..." if len(event.message.text) > 50 else event.message.text
            print(f"📩 Сообщение от {sender.first_name}: {msg_preview}")

            # Имитируем печатание
            typing_delay = random.uniform(0.5, 2.0)
            await asyncio.sleep(typing_delay)

            # Генерируем ответ
            response = self.brain.get_response(
                user_message=event.message.text,
                user_name=sender.first_name
            )

            # Отправляем ответ
            await event.reply(response)

            # Ставим реакцию (50% шанс)
            if random.random() < 0.5:
                await self._send_reaction(event.message)

            # Отмечаем как прочитанное
            await event.message.mark_read()

        except FloodWaitError as e:
            print(f"⏳ Слишком много запросов. Жду {e.seconds} секунд")
            await asyncio.sleep(e.seconds)
        except Exception as e:
            logger.error(f"Ошибка обработки: {e}")

    async def _send_reaction(self, message):
        """Отправляет реакцию на сообщение"""
        try:
            reactions = [
                ReactionEmoji(emoticon='👍'),
                ReactionEmoji(emoticon='❤️'),
                ReactionEmoji(emoticon='👏'),
            ]

            await self.client(SendReactionRequest(
                peer=message.peer_id,
                msg_id=message.id,
                reaction=[random.choice(reactions)]
            ))
        except:
            pass  # Игнорируем ошибки реакций

    async def _keep_alive(self):
        """Поддержание соединения"""
        while self.is_running:
            try:
                await asyncio.sleep(300)  # Каждые 5 минут
                if self.client and self.client.is_connected():
                    await self.client.get_me()
            except:
                await asyncio.sleep(30)

    async def _run_forever(self):
        """Основной цикл работы"""
        try:
            while self.is_running:
                await asyncio.sleep(1)
        except asyncio.CancelledError:
            pass

    async def stop(self):
        """Корректная остановка"""
        self.is_running = False
        if self.client:
            await self.client.disconnect()
        logger.info("🛑 Бот остановлен")
