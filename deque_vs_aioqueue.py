



from asyncio import Queue, gather
from collections import deque
from concurrent.futures import ThreadPoolExecutor
from time import sleep
from typing import Deque


TASK_COUNT = 1000_000


def consume(q: Deque[int | None]):
    res = 0
    while True:
        if q:
            el = q.popleft()
            if el is not None:
                res += el
            else:
                break
        else:
            sleep(0.05)


def send(q: Deque[int | None]):
    for el in range(TASK_COUNT):
        q.append(el)
    q.append(None)


def handle_deque():
    q: Deque[int | None] = deque()
    with ThreadPoolExecutor(max_workers=2) as executer:
        executer.submit(send, q)
        executer.submit(consume, q)


async def consume_async(q: Queue[int | None]):
    res = 0
    while True:
        el = await q.get()
        if el is not None:
            res += el
        else:
            break


async def send_async(q: Queue[int | None]):
    for el in range(TASK_COUNT):
        q.put_nowait(el)
        # await q.put(el)
    await q.put(None)


async def handle_asyncio_queue():
    q:  Queue[int | None] = Queue()
    await gather(
        consume_async(q),
        send_async(q),
    )
