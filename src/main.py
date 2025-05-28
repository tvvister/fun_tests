from asyncio import run

from async_impl import handle_asyncio_queue
from sync import handle_deque


if __name__ == "__main__":
    run(handle_asyncio_queue())
    handle_deque(1000000)
