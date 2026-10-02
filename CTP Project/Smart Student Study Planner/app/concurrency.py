import asyncio
import time
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool

# =========================================================
# THREADING
# =========================================================

def process_subject(
    subject: str,
) -> str:

    time.sleep(1)

    return f"Processed {subject}"


def run_threads() -> None:

    subjects = [
        "Python",
        "Statistics",
        "AI",
        "Machine Learning",
    ]

    with ThreadPoolExecutor(
        max_workers=4
    ) as executor:

        results = executor.map(
            process_subject,
            subjects,
        )

    for result in results:

        print(result)


# =========================================================
# MULTIPROCESSING
# =========================================================

def calculate_square(
    number: int,
) -> int:

    return number * number


def run_multiprocessing() -> None:

    numbers = [
        10,
        20,
        30,
        40,
    ]

    with Pool() as pool:

        results = pool.map(
            calculate_square,
            numbers,
        )

    print(
        "Multiprocessing:",
        results,
    )


# =========================================================
# ASYNCIO
# =========================================================

async def fetch_resource(
    name: str,
) -> str:

    await asyncio.sleep(1)

    return (
        f"Resource downloaded: {name}"
    )


async def run_async() -> None:

    resources = [
        fetch_resource(
            "Python Notes"
        ),
        fetch_resource(
            "AI Notes"
        ),
        fetch_resource(
            "Statistics Notes"
        ),
    ]

    results = await asyncio.gather(
        *resources
    )

    for result in results:

        print(result)