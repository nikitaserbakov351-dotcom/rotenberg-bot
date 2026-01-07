import os
from dotenv import load_dotenv

# Пытаемся загрузить .env, если он есть
load_dotenv()

class Config:
    """Настройки бота"""
    
    # Получаем переменные из окружения
    API_ID = os.environ.get('API_ID')
    API_HASH = os.environ.get('API_HASH')
    SESSION_NAME = os.environ.get('SESSION_NAME')
    
    # Если переменные не найдены, попробуем из .env
    if not API_ID:
        API_ID = os.getenv('API_ID')
    if not API_HASH:
        API_HASH = os.getenv('API_HASH')
    if not SESSION_NAME:
        SESSION_NAME = os.getenv('SESSION_NAME')
    
    # Настройки ответов
    TYPING_DELAY_MIN = 0.5
    TYPING_DELAY_MAX = 4.5
    
    @classmethod
    def validate(cls):
        """Проверка настроек"""
        # Проверяем API_ID
        if not cls.API_ID:
            raise ValueError("❌ API_ID не найден. Добавьте в Railway Variables: API_ID=ваши_цифры")
        
        # Пытаемся преобразовать в число
        try:
            cls.API_ID = int(cls.API_ID)
        except (ValueError, TypeError):
            raise ValueError(f"❌ API_ID должен быть числом. У вас: {cls.API_ID}")
        
        # Проверяем API_HASH
        if not cls.API_HASH:
            raise ValueError("❌ API_HASH не найден. Добавьте в Railway Variables: API_HASH=ваш_хэш")
        
        # Проверяем SESSION_NAME
        if not cls.SESSION_NAME:
            raise ValueError("❌ SESSION_NAME не найден. Добавьте в Railway Variables: SESSION_NAME=ваша_сессия")
        
        print("✅ Конфигурация загружена успешно")
