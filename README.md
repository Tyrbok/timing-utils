# timing-utils

Simple utilities to time the execution of synchronous and asynchronous Python functions.

## Installation

```bash
pip install timing-utils
```

## Usage

```python
from timing_utils import timeit, async_timeit, run_async_task

@timeit
def fast_func():
    return sum(range(10000))

@async_timeit
async def slow_async_func():
    import asyncio
    await asyncio.sleep(1)

run_async_task(slow_async_func)
```
