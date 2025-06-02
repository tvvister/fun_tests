from queue import SimpleQueue
from concurrent.futures import ThreadPoolExecutor

from constants import TASK_COUNT


def consume(q: SimpleQueue[int | None]):
    res = 0
    while True:
        if q:
            el = q.get()
            if el is not None:
                res += el
            else:
                break


def send(q: SimpleQueue[int | None], task_count: int):
    for el in range(task_count):
        q.put_nowait(el)
    q.put_nowait(None)


def handle_simple_queue(task_count: int = TASK_COUNT):
    q: SimpleQueue[int | None] = SimpleQueue()
    with ThreadPoolExecutor(max_workers=2) as executer:
        executer.submit(send, q, task_count)
        executer.submit(consume, q)
        # executer.submit(consume, q)
        # executer.submit(consume, q)
