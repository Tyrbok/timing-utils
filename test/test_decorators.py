import asyncio
import pytest
from timing_utils import timeit, async_timeit, run_async_task


@timeit
def sample_sync_func():
    return sum(range(100))


@async_timeit
async def sample_async_func():
    await asyncio.sleep(0.1)
    return 42


def test_timeit_decorator():
    result = sample_sync_func()
    assert result == sum(range(100))


@pytest.mark.asyncio
async def test_async_timeit_decorator():
    result = await sample_async_func()
    assert result == 42


def test_run_async_task_executes_async_func(caplog):
    @async_timeit
    async def short_task():
        await asyncio.sleep(0.05)

    run_async_task(short_task)

    # Give the task a moment to finish if running in background
    asyncio.run(asyncio.sleep(0.1))