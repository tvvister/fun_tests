from asyncio import Queue, gather

from constants import TASK_COUNT


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
