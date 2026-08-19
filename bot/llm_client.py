import logging
from openai import AsyncOpenAI, APIError, APITimeoutError, APIConnectionError
from bot.config import config

logger = logging.getLogger(__name__)


class LLMService:
    def __init__(self):
        self.client = AsyncOpenAI(
            base_url=config.LLM_BASE_URL,
            api_key=config.LLM_API_KEY,
            timeout=config.LLM_TIMEOUT,
        )
        self.model = config.LLM_MODEL

    async def generate_reply(self, prompt: str) -> str:
        """
        Отправляет одиночный prompt в LLM (Stateless-режим, без истории).
        """
        try:
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "Ты полезный и лаконичный AI-ассистент. Отвечай прямо на поставленный вопрос."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
            )
            return response.choices[0].message.content or "Модель вернула пустой ответ."

        except APITimeoutError:
            logger.error("Превышен таймаут ожидания ответа от LLM.")
            return "Время ожидания ответа от нейросети истекло. Попробуйте еще раз позже."
        except APIConnectionError as e:
            logger.error(f"Ошибка подключения к LLM API ({config.LLM_BASE_URL}): {e}")
            return "Ошибка подключения к сервису LLM. Проверьте, запущен ли сервер модели."
        except APIError as e:
            logger.error(f"Ошибка LLM API: {e}")
            return f"Ошибка провайдера LLM: {e.message}"
        except Exception as e:
            logger.exception(f"Непредвиденная ошибка при запросе к LLM: {e}")
            return "⚠️ Произошла внутренняя ошибка при обработке запроса."


llm_service = LLMService()
