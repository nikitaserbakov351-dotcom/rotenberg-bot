import os

class Config:
    """Настройки бота"""
    
    # Получаем переменные ИЗ RAILWAY
    API_ID = os.environ.get('API_ID', '')
    API_HASH = os.environ.get('API_HASH', '')
    SESSION_NAME = os.environ.get('SESSION_NAME', '')
    
    # Настройки ответов
    TYPING_DELAY_MIN = 0.5
    TYPING_DELAY_MAX = 4.5
    
    @classmethod
    def validate(cls):
        """Проверка настроек"""
        print(f"🔍 DEBUG: API_ID = '{cls.API_ID}'")
        print(f"🔍 DEBUG: API_HASH = '{cls.API_HASH[:10]}...'")
        print(f"🔍 DEBUG: SESSION_NAME = '{cls.SESSION_NAME[:20]}...'")
        
        # Проверяем API_ID
        if not cls.API_ID or cls.API_ID.strip() == '':
            raise ValueError("❌ API_ID не найден в Railway Variables. Добавьте переменную API_ID с вашими цифрами")
        
        # Проверяем API_HASH
        if not cls.API_HASH or cls.API_HASH.strip() == '':
            raise ValueError("❌ API_HASH не найден в Railway Variables. Добавьте переменную API_HASH")
        
        # Проверяем SESSION_NAME
        if not cls.SESSION_NAME or cls.SESSION_NAME.strip() == '':
            raise ValueError("❌ SESSION_NAME не найден в Railway Variables. Добавьте переменную SESSION_NAME")
        
        print("✅ Конфигурация загружена успешно")
