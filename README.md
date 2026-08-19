# Telegram-бот с интеграцией LLM

Асинхронный Telegram-бот на **Python (aiogram 3)** с подключением к языковым моделям через OpenAI-совместимый API (**Ollama**, **OpenAI**, **OpenRouter**, **PolzaAI**).

## 🚀 Особенности

- **Stateless-архитектура:** Бот работает по схеме `User Message → LLM → Bot Reply` без сохранения истории, что экономит токены и снижает нагрузку на память.
- **Универсальный LLM-клиент:** Быстрое переключение между локальными моделями (Ollama) и облачными API (OpenAI / OpenRouter) простой сменой переменных в `.env`.
- **Отказоустойчивость:** Обработка таймаутов, недоступности LLM API и длинных ответов (>4096 символов).
- **Docker Ready:** Полностью готов к запуску локально или на сервере через `docker-compose`.

## 🛠️ Стек технологий

- **Язык:** Python 3.11+
- **Фреймворк бота:** `aiogram 3.x`
- **Клиент LLM:** `openai-python` (AsyncOpenAI)
- **Конфигурация:** `pydantic-settings`
- **Контейнеризация:** Docker, Docker Compose
- **LLM бэкенд:** Ollama (`tinyllama`, `qwen2.5:1.5b`) / OpenRouter

---

## ⚡ Быстрый старт

### 1. Локальный запуск (с локальной Ollama)

1. Установите и запустите [Ollama](https://ollama.com/):
   ```bash
   ollama run tinyllama
