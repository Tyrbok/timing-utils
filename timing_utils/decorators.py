import time
from functools import wraps
from typing import Callable, Any, Optional


def _default_logger(message: str) -> None:
    """Default logger function that uses print."""
    print(message)


# Global logger configuration
_global_logger: Optional[Callable[[str], Any]] = None


def set_timing_logger(logger: Optional[Callable[[str], Any]] = None) -> None:
    """
    Set a global logger for all timing decorators.

    Args:
        logger: A callable that will be used for logging. If None, the default print logger will be used.
    """
    global _global_logger
    _global_logger = logger


def async_timeit(func=None, *, logger: Optional[Callable[[str], Any]] = None):
    """
    A decorator that logs the execution time of an asynchronous function.

    Args:
        func: The function to be decorated.
        logger: A callable that will be used for logging. If None, the global logger will be used,
               and if no global logger is set, print will be used.
    """
    # Use the provided logger, or the global logger, or the default logger
    actual_logger = logger or _global_logger or _default_logger

    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = await func(*args, **kwargs)
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            actual_logger(f"Function '{func.__name__}' executed in {elapsed_time:.4f} seconds.")
            return result
        return wrapper

    if func is None:
        return decorator
    return decorator(func)


def timeit(func=None, *, logger: Optional[Callable[[str], Any]] = None):
    """
    A decorator that logs the execution time of a function.

    Args:
        func: The function to be decorated.
        logger: A callable that will be used for logging. If None, the global logger will be used,
               and if no global logger is set, print will be used.
    """
    # Use the provided logger, or the global logger, or the default logger
    actual_logger = logger or _global_logger or _default_logger

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            actual_logger(f"Function '{func.__name__}' executed in {elapsed_time:.4f} seconds.")
            return result
        return wrapper

    if func is None:
        return decorator
    return decorator(func)
