# fun_tests
Yet another repo—just for running fun tests on curious cases involving async, threading, and multiprocessing within Python's programming infrastructure.

# Producer-Consumer Performance Comparison in Python

## The Idea

I recently became interested in evaluating the performance of a common programming construct: the producer-consumer model in Python. Specifically, I wanted to compare synchronous (using `deque` with threads) and asynchronous (using `asyncio.Queue`) implementations.

## Implementation Details

The comparison focuses on two approaches:

1. **Synchronous Version**:
   - Uses `collections.deque` as the queue
   - Implements multitasking using two threads (one producer, one consumer)
   - Satisfies the multitasking requirement through threading

2. **Asynchronous Version**:
   - Uses `asyncio.Queue` as the queue
   - Leverages Python's native async/await syntax
   - Uses asyncio's built-in multitasking capabilities

## Initial Hypothesis

Before testing, I hypothesized that the asyncio version would outperform the threaded version because:
1. It operates in a single thread, avoiding GIL contention
2. It's a newer implementation that's presumably more optimized

## Performance Results

## How to Run

```bash
uv run --python 3.12 main_perf.py
```

Testing on Python 3.12 yielded surprising results:
```
handle_deque 6.472979425000176
handle_asyncio_queue 19.628546229999984
```

The synchronous `deque` implementation was approximately **3x faster** than the asynchronous `asyncio.Queue` implementation.

