# fun_tests
Yet another repo—just for running fun tests on curious cases involving async, threading, and multiprocessing within Python's programming infrastructure.

# Producer-Consumer Performance Comparison in Python

## The first check

### The Idea

I recently became interested in evaluating the performance of a common programming construct: the producer-consumer model in Python. Specifically, I wanted to compare synchronous (using `deque` with threads) and asynchronous (using `asyncio.Queue`) implementations.

## Implementation Details

The comparison focuses on two approaches:

1. **Synchronous Version**:
   - Uses `collections.deque` as the queue
   - Implements multitasking using two threads (one producer, one consumer)
   - Satisfies the multitasking requirement through threading

https://github.com/tvvister/fun_tests/blob/d30f8994df96587a537451956cc59de8f72bcf54/sync.py#L8-L22


2. **Asynchronous Version**:
   - Uses `asyncio.Queue` as the queue
   - Leverages Python's native async/await syntax
   - Uses asyncio's built-in multitasking capabilities

https://github.com/tvvister/fun_tests/blob/d30f8994df96587a537451956cc59de8f72bcf54/async_impl.py#L6-L19

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


## Next checks

Let’s Welcome a New Contender: **SimpleQueue** from the **queue** Module!

### Quick Intro to SimpleQueue

**queue.SimpleQueue** is Python’s no-frills, thread-safe FIFO queue built for one job: bulletproof communication between threads.


- Purpose:
   A simple, thread-safe FIFO queue designed for inter-thread communication.

- Thread Safety: Fully thread-safe (all operations are atomic).


Only supports FIFO operations (no appendleft or popleft).

### Features:

- No size limit (unless manually implemented).
- Does not support indexing or peeking (only get() and put()).
- Designed for multithreading (unlike deque).

Use Case: When you need a simple, thread-safe queue for communication between threads

## 3... 2... 1... uv run   !!!
```bash
uv run --python 3.12 main_perf2.py
```
Results:
```
handle_deque 5.6982688790303655
handle_asyncio_queue 23.970929217000958
handle_simple_queue 6.759707813966088
```
The Verdict:

**deque** still wears the speed crown