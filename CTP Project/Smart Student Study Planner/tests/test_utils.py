from pathlib import Path

from app.utils import (
    FileManager,
    calculate_total_hours,
    execution_time,
    filter_difficult_tasks,
    task_generator,
)


def test_execution_time(capsys) -> None:
    @execution_time
    def add_numbers(a: int, b: int) -> int:
        return a + b

    result = add_numbers(10, 20)

    output = capsys.readouterr().out

    assert result == 30
    assert "add_numbers took" in output
    assert "seconds" in output


def test_task_generator() -> None:
    tasks = [
        "Python",
        "Machine Learning",
        "Statistics",
    ]

    result = list(task_generator(tasks))

    assert result == tasks


def test_calculate_total_hours() -> None:
    hours = [2, 3, 4, 1]

    result = calculate_total_hours(hours)

    assert result == 10


def test_filter_difficult_tasks() -> None:
    difficulties = [3, 5, 7, 8, 9, 6]

    result = filter_difficult_tasks(difficulties)

    assert result == [7, 8, 9]


def test_file_manager(tmp_path: Path) -> None:
    file_path = tmp_path / "study_plan.txt"

    with FileManager(str(file_path)) as file:
        file.write("Python - 2 hours")

    assert file_path.exists()
    assert file_path.read_text(encoding="utf-8") == "Python - 2 hours"