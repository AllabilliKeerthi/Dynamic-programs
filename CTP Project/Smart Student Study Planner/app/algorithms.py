from typing import TypeVar

T = TypeVar("T", int, float, str)


# =========================================================
# 1. MERGE SORT
# =========================================================

def merge_sort(items: list[T]) -> list[T]:
    """
    Sort items using Merge Sort.
    """

    if len(items) <= 1:
        return items

    mid = len(items) // 2

    left = merge_sort(items[:mid])

    right = merge_sort(items[mid:])

    return merge(left, right)


def merge(
    left: list[T],
    right: list[T],
) -> list[T]:
    """
    Merge two sorted lists.
    """

    result: list[T] = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:

            result.append(left[i])

            i += 1

        else:

            result.append(right[j])

            j += 1

    result.extend(left[i:])

    result.extend(right[j:])

    return result


# =========================================================
# 2. GREEDY ALGORITHM
# =========================================================

def greedy_schedule(
    tasks: list[tuple[str, int]],
    available_hours: int,
) -> list[str]:
    """
    Select tasks using a Greedy approach.

    Tasks requiring fewer hours are considered first.
    """

    tasks = sorted(
        tasks,
        key=lambda x: x[1],
        reverse=True,
    )

    selected: list[str] = []

    used = 0

    for name, hours in tasks:

        if used + hours <= available_hours:

            selected.append(name)

            used += hours

    return selected


# =========================================================
# 3. KNAPSACK
# =========================================================

def knapsack(
    values: list[int],
    weights: list[int],
    capacity: int,
) -> int:
    """
    0/1 Knapsack algorithm.

    Values represent task importance.
    Weights represent required study hours.
    Capacity represents available study hours.
    """

    n = len(values)

    dp = [
        [0] * (capacity + 1)
        for _ in range(n + 1)
    ]

    for i in range(1, n + 1):

        for w in range(capacity + 1):

            if weights[i - 1] <= w:

                dp[i][w] = max(
                    dp[i - 1][w],
                    values[i - 1]
                    + dp[
                        i - 1
                    ][
                        w - weights[i - 1]
                    ],
                )

            else:

                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# =========================================================
# 4. BACKTRACKING
# =========================================================

def backtracking_timetable(
    tasks: list[tuple[str, int]],
    available_hours: int,
) -> list[str]:
    """
    Create a timetable using Backtracking.

    Each task uses its actual study hours.

    The algorithm searches for a combination
    of tasks that fits within the available
    study hours.
    """

    best_schedule: list[tuple[str, int]] = []

    best_hours = 0

    def search(
        index: int,
        current_schedule: list[tuple[str, int]],
        current_hours: int,
    ) -> None:

        nonlocal best_schedule
        nonlocal best_hours

        # Do not exceed available hours
        if current_hours > available_hours:

            return

        # Save the best schedule found
        if current_hours > best_hours:

            best_hours = current_hours

            best_schedule = (
                current_schedule.copy()
            )

        # All tasks checked
        if index == len(tasks):

            return

        task_name, task_hours = tasks[index]

        # -------------------------------------------------
        # Include current task
        # -------------------------------------------------

        if (
            current_hours + task_hours
            <= available_hours
        ):

            current_schedule.append(
                (
                    task_name,
                    task_hours,
                )
            )

            search(
                index + 1,
                current_schedule,
                current_hours + task_hours,
            )

            current_schedule.pop()

        # -------------------------------------------------
        # Exclude current task
        # -------------------------------------------------

        search(
            index + 1,
            current_schedule,
            current_hours,
        )

    search(
        0,
        [],
        0,
    )

    # Convert selected tasks into hourly slots
    timetable: list[str] = []

    for task_name, task_hours in best_schedule:

        for _ in range(task_hours):

            timetable.append(task_name)

    return timetable


# =========================================================
# 5. BRANCH & BOUND
# =========================================================

def best_selection(
    values: list[int],
    weights: list[int],
    capacity: int,
) -> int:
    """
    Branch and Bound style search.

    Finds the maximum value that can fit
    within the available capacity.
    """

    best = 0

    def search(
        index: int,
        current_value: int,
        current_weight: int,
    ) -> None:

        nonlocal best

        # Capacity exceeded
        if current_weight > capacity:

            return

        # All items processed
        if index == len(values):

            best = max(
                best,
                current_value,
            )

            return

        # Calculate remaining possible value
        remaining_value = current_value

        for i in range(
            index,
            len(values),
        ):

            remaining_value += values[i]

        # Prune this branch
        if remaining_value <= best:

            return

        # Include current item
        search(
            index + 1,
            current_value + values[index],
            current_weight + weights[index],
        )

        # Exclude current item
        search(
            index + 1,
            current_value,
            current_weight,
        )

    search(
        0,
        0,
        0,
    )

    return best