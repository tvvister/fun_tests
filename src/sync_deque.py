from collections import deque
from concurrent.futures import ThreadPoolExecutor
from typing import Deque

from constants import TASK_COUNT


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
        # executer.submit(consume, q)
        # executer.submit(consume, q)
