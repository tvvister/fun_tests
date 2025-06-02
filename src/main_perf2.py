import timeit


NUMBER = 50


def main_with_deque():
    print(
        'handle_deque',
        timeit.timeit(
            'handle_deque()',
            setup='from sync_deque import handle_deque',
            number=NUMBER,
        ),
    )


def main_with_simple_queue():
    print(
        'handle_simple_queue',
        timeit.timeit(
            'handle_simple_queue()',
            setup='from sync_queue import handle_simple_queue',
            number=NUMBER,
        ),
    )


def main_with_asyncio_queue():
    setup_code = """
from async_impl import handle_asyncio_queue
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
    main_with_simple_queue()
