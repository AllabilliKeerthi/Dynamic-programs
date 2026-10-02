from app.algorithms import (
    backtracking_timetable,
    best_selection,
    greedy_schedule,
    knapsack,
    merge_sort,
)


def test_merge_sort() -> None:
    data = [
        5,
        2,
        8,
        1,
        3,
    ]

    assert merge_sort(data) == [
        1,
        2,
        3,
        5,
        8,
    ]


def test_knapsack() -> None:
    values = [
        10,
        20,
        30,
    ]

    weights = [
        1,
        2,
        3,
    ]

    assert (
        knapsack(
            values,
            weights,
            3,
        )
        == 30
    )


def test_greedy_schedule() -> None:
    tasks = [
        ("Python", 2),
        ("AI", 3),
        ("Statistics", 1),
    ]

    result = greedy_schedule(
        tasks,
        4,
    )

    assert result == [
        "AI",
        "Statistics",
    ]


def test_backtracking_timetable() -> None:
    tasks = [
        ("Python", 2),
        ("AI", 3),
        ("Statistics", 2),
    ]

    result = backtracking_timetable(
        tasks,
        5,
    )

    assert len(result) == 5


def test_best_selection() -> None:
    values = [
        10,
        20,
        30,
    ]

    weights = [
        1,
        2,
        3,
    ]

    result = best_selection(
        values,
        weights,
        3,
    )

    assert result == 30