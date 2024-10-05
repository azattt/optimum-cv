import logging
from typing import Callable, Dict, Awaitable, Any, cast

from aiogram import BaseMiddleware
from aiogram.types import Update, TelegramObject, Message, CallbackQuery

from models import User

class BanMiddleware(BaseMiddleware):
    def __init__(self):
        self.logger = logging.getLogger("BanMiddleware")
    
    async def __call__(self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]):
        if isinstance(event, Update):
            if event.message:
                if event.message.from_user is None:
                    raise RuntimeError()
                user, _ = await User.get_or_create({"is_banned": False, "username": event.message.from_user.username}, tg_id=event.message.from_user.id)
            elif event.callback_query:
                user, _ = await User.get_or_create({"is_banned": False, "username": event.callback_query.from_user.username}, tg_id=event.callback_query.from_user.id)
            if user.is_banned:
                return
            await handler(cast(Update, event), data)
        else:
            raise RuntimeError("Unknown event", event)