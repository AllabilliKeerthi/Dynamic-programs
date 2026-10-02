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