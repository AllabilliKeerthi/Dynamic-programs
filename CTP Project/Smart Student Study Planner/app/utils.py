import time
from collections.abc import Callable, Generator
from functools import reduce
from types import TracebackType
from typing import Any, TextIO

# =========================================================
# EXECUTION TIME DECORATOR
# =========================================================

def execution_time(
    func: Callable[..., Any],
) -> Callable[..., Any]:

    def wrapper(
        *args: Any,
        **kwargs: Any,
    ) -> Any:

        start = time.perf_counter()

        result = func(
            *args,
            **kwargs,
        )

        end = time.perf_counter()

        print(
            f"{func.__name__} took "
            f"{end - start:.6f} seconds"
        )

        return result

    return wrapper


# =========================================================
# GENERATOR
# =========================================================

def task_generator(
    tasks: list[str],
) -> Generator[str, None, None]:

    yield from tasks


# =========================================================
# FUNCTIONAL PROGRAMMING - REDUCE
# =========================================================

def calculate_total_hours(
    hours: list[int],
) -> int:

    return reduce(
        lambda x, y: x + y,
        hours,
        0,
    )


# =========================================================
# FUNCTIONAL PROGRAMMING - FILTER
# =========================================================

def filter_difficult_tasks(
    difficulties: list[int],
) -> list[int]:

    return list(
        filter(
            lambda x: x >= 7,
            difficulties,
        )
    )


# =========================================================
# CONTEXT MANAGER
# =========================================================

class FileManager:

    def __init__(
        self,
        filename: str,
    ) -> None:

        self.filename = filename

        self.file: TextIO | None = None

    def __enter__(self) -> TextIO:

        self.file = open(
            self.filename,
            "w",
            encoding="utf-8",
        )

        return self.file

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:

        if self.file:

            self.file.close()