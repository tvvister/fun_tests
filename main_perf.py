import timeit


NUMBER = 50


def main_with_deque():
    print(
        'handle_deque',
        timeit.timeit(
            'handle_deque()',
            setup='from deque_vs_aioqueue import handle_deque',
            number=NUMBER,
        ),
    )


def main_with_asyncio_queue():
    setup_code = """
from deque_vs_aioqueue import handle_asyncio_queue
from asyncio import run
    """
    print(
        'handle_asyncio_queue',
        timeit.timeit(
            'run(handle_asyncio_queue())',
            setup=setup_code,
            number=NUMBER,
        ),
    )


if __name__ == "__main__":
    main_with_deque()
    main_with_asyncio_queue()
