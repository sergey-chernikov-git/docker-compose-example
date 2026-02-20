import json
from abc import ABC, abstractmethod
from typing import override, overload

import redis.asyncio as redis

from config import Config


class ACache(ABC):
    @abstractmethod
    async def add(self, key: str, value: object):
        raise NotImplemented()

    @abstractmethod
    async def get(self, key):
        raise NotImplemented()

    @abstractmethod
    async def update(self, key, value):
        raise NotImplemented()

    @abstractmethod
    async def ping(self) -> bool:
        raise NotImplemented()


class RedisCache(ACache):

    def __init__(self, host: str = Config.RI_APP_HOST, port: int = Config.RI_APP_PORT):
        self._redis = redis.Redis(
            host=host,
            port=port,
            decode_responses=True,
            socket_timeout=3
        )

    async def add(self, key: str, value: object):
        if isinstance(value, dict):
            await self._redis.set(f"{Config.RI_APP_PREFIX}-{key}", json.dumps(value))
        elif isinstance(value, str):
            await self._redis.set(f"{Config.RI_APP_PREFIX}-{key}", value)
        else:
            raise NotImplementedError(f"Method add({type(key)}, {type(value)}) is not implemented")

    async def get(self, key):
        return await self._redis.get(f"{Config.RI_APP_PREFIX}-{key}")

    async def update(self, key, value):
        await self.add(key, value)

    async def ping(self) -> bool:
        return await self._redis.ping()


redis_cache = RedisCache()
