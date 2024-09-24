from typing import Callable, Dict, Awaitable, Any, cast

from aiogram import BaseMiddleware
from aiogram.types import Update, TelegramObject

class BanMiddleware(BaseMiddleware):
    def __init__(self):
        pass
    
    async def __call__(self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]):
        await handler(cast(Update, event), data)