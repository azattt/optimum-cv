import decimal
import logging
import time
from typing import Any, TypedDict, cast

import asyncpg

from aiogram.types import KeyboardButton

print("loading", __file__)

UserRecord = TypedDict(
    "UserRecord", {"tg_id": int, "username": str, "first_visit": float, "is_banned": bool}
)
UserID_MessageID = TypedDict("UserID_MessageID", {"tg_id": int, "msg_id": int})
MessageRecord = TypedDict(
    "MessageRecord",
    {
        "id": int,
        "time_sent": int,
        "message_json": str,
        "users_sent_to": list[UserID_MessageID],
        "is_deleted": bool,
    },
)


class DB:
    def __init__(self, user: str, password: str, database: str, host: str):
        self._initalized = False
        self._conn: asyncpg.connection.Connection | None = None
        self._user = user
        self._password = password
        self._database = database
        self._host = host
        self._conn_pool: asyncpg.pool.Pool
        self.logger = logging.getLogger(f"db:{user}:{database}")

    @property
    def conn_pool(self):
        if not self._initalized:
            raise RuntimeError("DB not initialized (await async__init__ function)")
        return self._conn_pool

    async def async__init__(self):
        self._conn_pool = await asyncpg.pool.create_pool(
            user=self._user, password=self._password, database=self._database, host=self._host
        )
        self._initalized = True

    async def fetch(
        self, query: str, *args, timeout: float | None = None, record_class=None
    ) -> list:
        """Proxy function for benchmarking"""
        async with self.conn_pool.acquire() as conn:
            t0 = time.perf_counter()
            result = await conn.fetch(query, *args, timeout=timeout, record_class=record_class)
            self.logger.debug("db.fetch: %f sec. Query: %s", time.perf_counter() - t0, query)
            return result

    async def fetchrow(
        self, query: str, *args, timeout: float | None = None, record_class=None
    ) -> dict | None:
        """Proxy function for benchmarking"""
        async with self.conn_pool.acquire() as conn:
            t0 = time.perf_counter()
            result = await conn.fetchrow(query, *args, timeout=timeout, record_class=record_class)
            self.logger.debug("db.fetchrow: %f sec. Query: %s", time.perf_counter() - t0, query)
            return result

    async def fetchval(
        self, query: str, *args, column: int = 0, timeout: float | None = None
    ) -> Any:
        """Proxy function for benchmarking"""
        async with self.conn_pool.acquire() as conn:
            t0 = time.perf_counter()
            result = await conn.fetchval(query, *args, column=column, timeout=timeout)
            self.logger.debug("db.fetchval: %f sec. Query: %s", time.perf_counter() - t0, query)
            return result

    async def execute(self, query: str, *args, timeout: float | None = None) -> str:
        """Proxy function for benchmarking"""
        async with self.conn_pool.acquire() as conn:
            t0 = time.perf_counter()
            result = await conn.execute(query, *args, timeout=timeout)
            self.logger.debug("db.execute: %f sec. Query: %s", time.perf_counter() - t0, query)
            return result

    async def close(self):
        t0 = time.perf_counter()
        await self.conn_pool.close()
        self.logger.debug("db.close: %f sec", time.perf_counter() - t0)

    async def get_calculator_categories(self) -> list[list[KeyboardButton]]:
        buttons: list[list[KeyboardButton]] = []
        rows = await self.fetch("select * from calculator_categories_rows;")
        buttons_text = await self.fetch("select * from calculator_categories;")
        button_index = 0
        for y, num_col in enumerate(rows):
            buttons.append([] * num_col["num_in_row"])
            for _ in range(num_col["num_in_row"]):
                buttons[y].append(KeyboardButton(text=buttons_text[button_index]["button"]))
                button_index += 1
        for i in range(button_index, len(buttons_text)):
            buttons.append([KeyboardButton(text=buttons_text[i]["button"])])
        return buttons

    async def get_calculator_categories_text(self) -> list[str]:
        result = await self.fetch("select * from calculator_categories;")
        return [i["button"] for i in result]

    async def get_exchange_rate(self) -> decimal.Decimal:
        result = await self.fetch("select * from exchange_rate;")
        return result[-1]["rate"]

    async def set_exchange_rate(self, rate: decimal.Decimal) -> None:
        await self.execute("insert into exchange_rate values ($1);", rate)

    async def get_commision(self, category_name: str) -> int:
        result = await self.fetchrow(
            "select * from calculator_categories where button=$1;", category_name
        )
        if not result:
            raise RuntimeError("Category not found")
        return result["commision"]

    async def is_admin(self, tg_id: int) -> bool:
        result = await self.fetch("select * from admins where tg_id=$1", tg_id)
        return bool(result)

    async def create_user(self, tg_id: int, username: str | None, first_visit: float) -> None:
        await self.execute(
            "insert into users values ($1, $2, $3, $4)", tg_id, username, first_visit, False
        )

    async def get_user(self, tg_id: int) -> UserRecord | None:
        result = cast(UserRecord, await self.fetchrow("select * from users where tg_id=$1;", tg_id))
        return result

    async def get_users(self, offset: int = 0, limit: int = 0) -> list[UserRecord]:
        if offset and limit:
            result = await self.fetch("select * from users offset $1 limit $2;", offset, limit)
        elif offset:
            result = await self.fetch("select * from users offset $1;", offset)
        elif limit:
            result = await self.fetch("select * from users limit $1;", limit)
        else:
            result = await self.fetch("select * from users")
        return result

    async def count_users(self) -> int:
        result = await self.fetchval("select count(*) from users;")
        return result

    async def set_user_ban_status(self, tg_id: int, is_banned: bool):
        await self.execute("update users set is_banned = $2 where tg_id = $1", tg_id, is_banned)

    async def save_message(self, time_sent: float, message_json: str) -> int:
        msg_id = await self.fetchval(
            "insert into messages values (DEFAULT, $1, $2, DEFAULT, DEFAULT) returning id",
            time_sent,
            message_json,
        )
        return msg_id

    async def edit_message_users_sent_to(self, msg_id: int, user_ids: list[tuple[int, int]]):
        await self.execute("update messages set users_sent_to=$1 where id=$2", user_ids, msg_id)

    async def set_message_deleted(self, msg_id: int, is_deleted: bool):
        await self.execute("update messages set is_deleted=$1 where id=$2", is_deleted, msg_id)

    async def get_messages(self, offset=0, limit=None) -> list[MessageRecord]:
        result = await self.fetch("select * from messages offset $1 limit $2", offset, limit)
        return result

    async def get_message_by_id(self, msg_id: int) -> MessageRecord:
        result = cast(
            MessageRecord | None, await self.fetchrow("select * from messages where id=$1", msg_id)
        )
        if not result:
            raise RuntimeError("Message not found")
        return result
