from asyncio import run

from async_impl import handle_asyncio_queue
from sync_deque import handle_deque
from sync_queue import handle_simple_queue


if __name__ == "__main__":
    run(handle_asyncio_queue(10))
    handle_deque(10)
    handle_simple_queue(10)
