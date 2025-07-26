# timing-utils

Simple utilities to time the execution of synchronous and asynchronous Python functions.

## Installation

### Basic Installation

```bash
pip install timing-utils
```

### With Loguru Support

If you want to use loguru with timing-utils:

```bash
pip install timing-utils[loguru]
```

## Usage

### Basic Usage

```python
from timing_utils import timeit, async_timeit

@timeit
def fast_func():
    return sum(range(10000))

@async_timeit
async def slow_async_func():
    import asyncio
    await asyncio.sleep(1)

# Example of running the async function (in an async environment):
# await slow_async_func()
```

### Custom Logger

You can provide a custom logger function to the decorators:

```python
from timing_utils import timeit, async_timeit
import logging

# Configure your own logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Use with a custom logger
@timeit(logger=logger.debug)
def fast_func():
    return sum(range(10000))

# Or with loguru
from loguru import logger

@async_timeit(logger=logger.debug)
async def slow_async_func():
    import asyncio
    await asyncio.sleep(1)
```

If no logger is provided, a simple print function will be used by default.

### Global Logger Configuration

You can set a global logger for all timing decorators, which will be used when no specific logger is provided:

```python
from timing_utils import timeit, async_timeit, set_timing_logger
import logging

# Configure your own logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Set the global logger
set_timing_logger(logger.debug)

# These decorators will use the global logger
@timeit
def fast_func():
    return sum(range(10000))

@async_timeit
async def slow_async_func():
    import asyncio
    await asyncio.sleep(1)

# You can still override the global logger for specific functions
@timeit(logger=print)
def another_func():
    return 42
```

The priority for logger selection is:
1. Logger provided directly to the decorator
2. Global logger set with `set_timing_logger`
3. Default print logger

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes and add tests if needed
4. Run tests locally: `make test`
5. Submit a pull request

Please follow the existing coding style and include relevant documentation if applicable.

## License

This project is licensed under the [MIT License](LICENSE).
