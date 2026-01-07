import os
from dotenv import load_dotenv

# Пытаемся загрузить из .env (для локального запуска)
try:
    load_dotenv()
except:
    pass

class Config:
    """Настройки бота"""
    # Берем переменные из окружения (Railway) или из .env
    API_ID = int(os.environ.get('API_ID') or os.getenv('API_ID', 0))
    API_HASH = os.environ.get('API_HASH') or os.getenv('API_HASH', '')
    SESSION_NAME = os.environ.get('SESSION_NAME') or os.getenv('SESSION_NAME', 'rotenberg_session')
    
    # Настройки ответов
    TYPING_DELAY_MIN = 0.5
    TYPING_DELAY_MAX = 4.5
    
    @classmethod
    def validate(cls):
        """Проверка настроек"""
        print(f"🔍 Проверяю переменные:")
        print(f"   API_ID: {'✅' if cls.API_ID else '❌'} ({cls.API_ID})")
        print(f"   API_HASH: {'✅' if cls.API_HASH else '❌'} ({cls.API_HASH[:10]}...)")
        print(f"   SESSION_NAME: {'✅' if cls.SESSION_NAME else '❌'} ({cls.SESSION_NAME[:20]}...)")
        
        if not cls.API_ID or cls.API_ID == 0:
            raise ValueError("❌ API_ID не найден")
        if not cls.API_HASH:
            raise ValueError("❌ API_HASH не найден")
        if not cls.SESSION_NAME or cls.SESSION_NAME == 'rotenberg_session':
            raise ValueError("❌ SESSION_NAME не найден или использует значение по умолчанию")
        
        print("✅ Конфигурация загружена успешно")
