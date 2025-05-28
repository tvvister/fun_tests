from asyncio import run
from deque_vs_aioqueue import handle_asyncio_queue, handle_deque


if __name__ == "__main__":
    run(handle_asyncio_queue())
    handle_deque(1000000)
