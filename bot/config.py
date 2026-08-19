from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Telegram Bot API
    TELEGRAM_BOT_TOKEN: str

    # LLM Provider Configuration
    # Для локальной Ollama: http://localhost:11434/v1 (или http://ollama:11434/v1 в docker)
    # Для OpenRouter: https://openrouter.ai/api/v1
    # Для OpenAI: https://api.openai.com/v1
    LLM_BASE_URL: str = "http://localhost:11434/v1"
    LLM_API_KEY: str = "ollama"  # Для локальной Ollama ключ может быть любым
    LLM_MODEL: str = "qwen2.5:1.5b"  # или tinyllama, gpt-4o-mini и т.д.
    
    # Таймаут на генерацию (в секундах)
    LLM_TIMEOUT: float = 60.0

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


config = Settings()
