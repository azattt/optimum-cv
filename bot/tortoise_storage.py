import json
import logging
from typing import Any

from aiogram.fsm.storage.base import (
    BaseStorage,
    StateType,
    StorageKey,
)
from aiogram.fsm.state import State

from models import User

print("loading", __file__)

class TortoiseStorage(BaseStorage):
    """Single bot, single chat storage for Tortoise"""
    def __init__(self):
        self.logger = logging.getLogger("TortoiseStorage")

    async def set_state(self, key: StorageKey, state: StateType = None) -> None:
        """
        Set state for specified key

        :param key: storage key
        :param state: new state
        """
        db_key = key.user_id
        if isinstance(state, State):
            new_state = state.state 
        else:
            new_state = state

        if new_state is None:
            new_state = ""

        self.logger.debug("Setting %s state to %s", db_key, new_state)

        (await User.get(tg_id=db_key)).state = new_state

    async def get_state(self, key: StorageKey) -> str | None:
        """
        Get key state

        :param key: storage key
        :return: current state
        """
        db_key = key.user_id
        self.logger.debug("Getting state for %s", db_key)
        result = await User.get(tg_id=db_key)
        if not result:
            return None
        
        return result.state



    async def set_data(self, key: StorageKey, data: dict[str, Any]) -> None:
        """
        Write data (replace)

        :param key: storage key
        :param data: new data
        """
        db_key = key.user_id
        self.logger.debug("Setting data for %s", db_key)
        (await User.get(tg_id=db_key)).data = data


    async def get_data(self, key: StorageKey) -> dict[str, Any]:
        """
        Get current data for key

        :param key: storage key
        :return: current data
        """
        db_key = key.user_id
        self.logger.debug("Getting data for %s", db_key)
        result = await User.get(tg_id=db_key)
        if not result:
            raise RuntimeError("no data")
        
        data = result.data
        if not data:
            return {}
        if isinstance(data, list):
            raise NotImplementedError("User state data returned list instead of dict")
        return data

    async def close(self) -> None:
        """
        Close storage (database connection, file or etc.)
        """
        self.logger.debug("Closing storage (no need to close, ORM will do that for us)")
    
        
    