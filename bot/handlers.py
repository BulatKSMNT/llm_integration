from aiogram import Router, types
from aiogram.enums import ChatAction
from aiogram.filters import CommandStart, Command
from bot.llm_client import llm_service

router = Router()


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    welcome_text = (
        "Привет! Я бот с интеграцией языковой модели (LLM).\n\n"
        "Я работаю в **stateless-режиме** (без сохранения контекста диалога): "
        "каждое сообщение обрабатывается как отдельный независимый запрос.\n\n"
        "Просто отправь мне любой текстовый вопрос!"
    )
    await message.answer(welcome_text, parse_mode="Markdown")


@router.message(Command("help"))
async def cmd_help(message: types.Message):
    help_text = (
        "**Справка:**\n"
        "- Отправьте текстовое сообщение, чтобы получить ответ от LLM.\n"
        "- Память диалога отключена для снижения расхода токенов и ускорения работы.\n"
        "- Поддерживает локальные (Ollama) и облачные (OpenAI / OpenRouter) модели."
    )
    await message.answer(help_text, parse_mode="Markdown")


@router.message()
async def handle_message(message: types.Message):
    if not message.text:
        await message.answer("Пожалуйста, отправьте текстовое сообщение.")
        return

    # статус "печатает..." в чате Telegram
    await message.bot.send_chat_action(
        chat_id=message.chat.id, 
        action=ChatAction.TYPING
    )

    # Генерация ответа от LLM
    reply = await llm_service.generate_reply(message.text)
    
    if len(reply) > 4000:
        for chunk in range(0, len(reply), 4000):
            await message.answer(reply[chunk:chunk + 4000])
    else:
        await message.answer(reply)
