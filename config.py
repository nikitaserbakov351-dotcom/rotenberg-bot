import os

class Config:
    """Настройки бота"""
    
    # Получаем переменные из окружения
    API_ID = os.getenv('API_ID', '').strip()
    API_HASH = os.getenv('API_HASH', '').strip()
    SESSION_NAME = os.getenv('SESSION_NAME', '').strip()
    
    # Настройки ответов
    TYPING_DELAY_MIN = 0.5
    TYPING_DELAY_MAX = 4.5
    
    @classmethod
    def validate(cls):
        """Проверка настроек"""
        print("=" * 60)
        print("🔍 ПРОВЕРКА ПЕРЕМЕННЫХ:")
        print(f"API_ID: {cls.API_ID}")
        print(f"API_HASH (первые 20): {cls.API_HASH[:20]}")
        print(f"SESSION_NAME длина: {len(cls.SESSION_NAME)} символов")
        
        # Проверяем длину SESSION_NAME
        if len(cls.SESSION_NAME) < 200:
            print(f"⚠️  ВНИМАНИЕ: SESSION_NAME слишком короткий! Нужно ~300 символов")
        
        if ' ' in cls.SESSION_NAME:
            print("⚠️  ВНИМАНИЕ: В SESSION_NAME есть ПРОБЕЛЫ! Удалите их!")
        
        print("=" * 60)
        
        # Проверяем наличие
        if not cls.API_ID:
            raise ValueError("❌ API_ID не найден")
        
        if not cls.API_HASH:
            raise ValueError("❌ API_HASH не найден")
        
        if not cls.SESSION_NAME:
            raise ValueError("❌ SESSION_NAME не найден")
        
        # Проверяем API_ID на число
        try:
            api_id_int = int(cls.API_ID)
            print(f"✅ API_ID корректный: {api_id_int}")
        except:
            raise ValueError(f"❌ API_ID должен быть числом: '{cls.API_ID}'")
        
        # Проверяем API_HASH (должен быть 32 символа)
        if len(cls.API_HASH) != 32:
            print(f"⚠️  API_HASH должен быть 32 символа, у вас: {len(cls.API_HASH)}")
        
        print("✅ ВСЕ ПЕРЕМЕННЫЕ НАЙДЕНЫ")
        return True
