from app.models import Student, StudyTask
from app.planner import StudyPlanner


def test_planner_sort_tasks() -> None:
    student = Student("Test Student", 4)

    student.add_task(
        StudyTask(
            "Machine Learning",
            "AI",
            9,
            10,
            2,
            3,
        )
    )

    student.add_task(
        StudyTask(
            "Python",
            "Programming",
            7,
            8,
            2,
            1,
        )
    )

    planner = StudyPlanner(student)

    tasks = planner.sort_tasks()

    assert tasks[0].name == "Python"
    assert tasks[1].name == "Machine Learning"


def test_planner_generate_plan(capsys) -> None:
    student = Student("Test Student", 4)

    student.add_task(
        StudyTask(
            "Python Algorithms",
            "Programming",
            8,
            9,
            2,
            1,
        )
    )

    student.add_task(
        StudyTask(
            "Machine Learning",
            "AI",
            9,
            10,
            2,
            2,
        )
    )

    planner = StudyPlanner(student)

    planner.generate_plan()

    output = capsys.readouterr().out

    assert "===== STUDY PLAN =====" in output
    assert "Programming: Python Algorithms - 2 hour(s)" in output
    assert "AI: Machine Learning - 2 hour(s)" in output
    assert "Timetable:" in output


def test_planner_optimize_topics(capsys) -> None:
    student = Student("Test Student", 4)

    student.add_task(
        StudyTask(
            "Python",
            "Programming",
            7,
            8,
            2,
            1,
        )
    )

    student.add_task(
        StudyTask(
            "Machine Learning",
            "AI",
            9,
            10,
            2,
            2,
        )
    )

    planner = StudyPlanner(student)

    planner.optimize_topics()

    output = capsys.readouterr().out

    assert "Maximum study value:" in output
    assert "Branch & Bound value:" in output