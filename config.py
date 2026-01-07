import os

class Config:
    """Настройки бота"""
    
    # ПРЯМОЕ ПОЛУЧЕНИЕ ПЕРЕМЕННЫХ
    API_ID = os.getenv('API_ID', '').strip()
    API_HASH = os.getenv('API_HASH', '').strip()
    SESSION_NAME = os.getenv('SESSION_NAME', '').strip()
    
    # Настройки ответов
    TYPING_DELAY_MIN = 0.5
    TYPING_DELAY_MAX = 4.5
    
    @classmethod
    def validate(cls):
        """Проверка настроек"""
        print("=" * 50)
        print("🔍 ПРОВЕРКА ПЕРЕМЕННЫХ ОКРУЖЕНИЯ:")
        print(f"API_ID (длина): {len(cls.API_ID)} символов")
        print(f"API_HASH (начало): {cls.API_HASH[:15]}")
        print(f"SESSION_NAME (начало): {cls.SESSION_NAME[:30]}")
        print("=" * 50)
        
        # Проверяем API_ID
        if not cls.API_ID:
            print("❌ ОШИБКА: API_ID ПУСТОЙ!")
            print("✅ РЕШЕНИЕ: В Railway Variables добавьте API_ID=ваши_цифры")
            raise ValueError("API_ID пустой")
        
        # Пробуем преобразовать в число
        try:
            api_id_int = int(cls.API_ID)
            print(f"✅ API_ID корректный: {api_id_int}")
        except:
            print(f"❌ API_ID не число: '{cls.API_ID}'")
            raise ValueError("API_ID должен быть числом")
        
        # Проверяем API_HASH
        if not cls.API_HASH:
            print("❌ ОШИБКА: API_HASH ПУСТОЙ!")
            raise ValueError("API_HASH пустой")
        
        # Проверяем SESSION_NAME
        if not cls.SESSION_NAME:
            print("❌ ОШИБКА: SESSION_NAME ПУСТОЙ!")
            raise ValueError("SESSION_NAME пустой")
        
        print("✅ ВСЕ ПЕРЕМЕННЫЕ НАЙДЕНЫ!")
        print("=" * 50)
