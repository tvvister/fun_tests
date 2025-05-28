from asyncio import Queue, gather, sleep
from collections import deque
from concurrent.futures import ThreadPoolExecutor
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


def send(q: Deque[int | None], task_count: int):
    for el in range(task_count):
        q.append(el)
    q.append(None)


def handle_deque(task_count: int = TASK_COUNT):
    q: Deque[int | None] = deque()
    with ThreadPoolExecutor(max_workers=2) as executer:
        executer.submit(send, q, task_count)
        executer.submit(consume, q)


async def consume_async(q: Queue[int | None]):
    res = 0
    while True:
        el = await q.get()
        if el is not None:
            res += el
        else:
            break


async def send_async(q: Queue[int | None], task_count: int):
    for el in range(task_count):
        q.put_nowait(el)
    await q.put(None)


async def handle_asyncio_queue(task_count: int = TASK_COUNT):
    q:  Queue[int | None] = Queue()
    await gather(
        consume_async(q),
        send_async(q, task_count),
    )
