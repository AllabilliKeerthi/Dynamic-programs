import random
import time
from collections.abc import Callable
from typing import Any

from app.algorithms import (
    backtracking_timetable,
    best_selection,
    greedy_schedule,
    knapsack,
    merge_sort,
)


def measure_time(
    function: Callable[..., Any],
    *args: Any,
) -> tuple[Any, float]:
    start = time.perf_counter()

    result = function(*args)

    end = time.perf_counter()

    return result, end - start


def print_bar_chart(
    times: dict[str, float],
) -> None:
    print("\n" + "=" * 60)
    print("             PERFORMANCE CHART")
    print("=" * 60)

    maximum = max(times.values())

    for name, execution_time in times.items():

        if maximum > 0:
            bar_length = int(
                (execution_time / maximum) * 40
            )
        else:
            bar_length = 0

        bar = "█" * bar_length

        print(
            f"{name:<22} | "
            f"{bar:<40} "
            f"{execution_time:.6f}s"
        )

    print("=" * 60)


def main() -> None:
    print("=" * 60)
    print("           PERFORMANCE EVALUATION")
    print("=" * 60)

    # -----------------------------------------------------
    # 1. MERGE SORT
    # -----------------------------------------------------

    data = [
        random.randint(1, 10000)
        for _ in range(1000)
    ]

    _, merge_time = measure_time(
        merge_sort,
        data,
    )

    print("\n1. Merge Sort")
    print("Input size:", len(data))
    print(
        f"Execution time: "
        f"{merge_time:.6f} seconds"
    )

    # -----------------------------------------------------
    # 2. GREEDY SCHEDULING
    # -----------------------------------------------------

    greedy_tasks = [
        (
            f"Task {i}",
            random.randint(1, 10),
        )
        for i in range(1000)
    ]

    _, greedy_time = measure_time(
        greedy_schedule,
        greedy_tasks,
        500,
    )

    print("\n2. Greedy Scheduling")
    print(
        "Number of tasks:",
        len(greedy_tasks),
    )
    print(
        f"Execution time: "
        f"{greedy_time:.6f} seconds"
    )

    # -----------------------------------------------------
    # 3. DYNAMIC PROGRAMMING
    # -----------------------------------------------------

    values = [
        random.randint(1, 100)
        for _ in range(50)
    ]

    weights = [
        random.randint(1, 20)
        for _ in range(50)
    ]

    capacity = 100

    _, knapsack_time = measure_time(
        knapsack,
        values,
        weights,
        capacity,
    )

    print("\n3. Dynamic Programming - Knapsack")
    print(
        "Number of items:",
        len(values),
    )
    print("Capacity:", capacity)
    print(
        f"Execution time: "
        f"{knapsack_time:.6f} seconds"
    )

    # -----------------------------------------------------
    # 4. BACKTRACKING
    # -----------------------------------------------------

    backtracking_tasks = [
        (
            f"Task {i}",
            random.randint(1, 5),
        )
        for i in range(16)
    ]

    _, backtracking_time = measure_time(
        backtracking_timetable,
        backtracking_tasks,
        30,
    )

    print("\n4. Backtracking")
    print(
        "Number of tasks:",
        len(backtracking_tasks),
    )
    print(
        f"Execution time: "
        f"{backtracking_time:.6f} seconds"
    )

    # -----------------------------------------------------
    # 5. BRANCH AND BOUND
    # -----------------------------------------------------

    bb_values = [
        random.randint(1, 100)
        for _ in range(16)
    ]

    bb_weights = [
        random.randint(1, 10)
        for _ in range(16)
    ]

    bb_capacity = 40

    _, branch_bound_time = measure_time(
        best_selection,
        bb_values,
        bb_weights,
        bb_capacity,
    )

    print("\n5. Branch & Bound")
    print(
        "Number of items:",
        len(bb_values),
    )
    print("Capacity:", bb_capacity)
    print(
        f"Execution time: "
        f"{branch_bound_time:.6f} seconds"
    )

    # -----------------------------------------------------
    # PERFORMANCE SUMMARY
    # -----------------------------------------------------

    times = {
        "Merge Sort": merge_time,
        "Greedy": greedy_time,
        "Dynamic Programming": knapsack_time,
        "Backtracking": backtracking_time,
        "Branch & Bound": branch_bound_time,
    }

    print("\n" + "=" * 60)
    print("              PERFORMANCE SUMMARY")
    print("=" * 60)

    for name, execution_time in times.items():
        print(
            f"{name:<25} "
            f"{execution_time:.6f} seconds"
        )

    # -----------------------------------------------------
    # ASCII PERFORMANCE CHART
    # -----------------------------------------------------

    print_bar_chart(times)


if __name__ == "__main__":
    main()