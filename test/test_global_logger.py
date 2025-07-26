import pytest
from timing_utils import timeit, async_timeit, set_timing_logger
import asyncio


# Custom logger for testing
test_log_messages = []


def custom_logger(message):
    test_log_messages.append(message)


# Test with global logger
def test_global_logger():
    # Clear any previous log messages
    test_log_messages.clear()

    # Set the global logger
    set_timing_logger(custom_logger)

    # Define a function with the default logger (should use global logger)
    @timeit
    def test_func():
        return 42

    # Call the function
    result = test_func()

    # Check the result
    assert result == 42

    # Check that the log message was captured
    assert len(test_log_messages) == 1
    assert "Function 'test_func' executed in" in test_log_messages[0]


# Test with decorator-specific logger overriding global logger
def test_override_global_logger():
    # Clear any previous log messages
    test_log_messages.clear()

    # Set the global logger
    set_timing_logger(custom_logger)

    # Define a function with a specific logger
    specific_log_messages = []

    def specific_logger(message):
        specific_log_messages.append(message)

    @timeit(logger=specific_logger)
    def test_func():
        return 42

    # Call the function
    result = test_func()

    # Check the result
    assert result == 42

    # Check that the log message was captured by the specific logger, not the global one
    assert len(test_log_messages) == 0
    assert len(specific_log_messages) == 1
    assert "Function 'test_func' executed in" in specific_log_messages[0]


# Test with async function and global logger
@pytest.mark.asyncio
async def test_async_global_logger():
    # Clear any previous log messages
    test_log_messages.clear()

    # Set the global logger
    set_timing_logger(custom_logger)

    # Define an async function with the default logger (should use global logger)
    @async_timeit
    async def test_async_func():
        await asyncio.sleep(0.1)
        return 42

    # Call the function
    result = await test_async_func()

    # Check the result
    assert result == 42

    # Check that the log message was captured
    assert len(test_log_messages) == 1
    assert "Function 'test_async_func' executed in" in test_log_messages[0]
