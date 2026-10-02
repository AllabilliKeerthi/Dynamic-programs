import asyncio

from app.concurrency import (
    run_async,
    run_multiprocessing,
    run_threads,
)
from app.models import Student, StudyTask
from app.planner import StudyPlanner
from app.utils import (
    calculate_total_hours,
    filter_difficult_tasks,
    task_generator,
)


def main() -> None:

    # -----------------------------------------------------
    # CREATE STUDENT
    # -----------------------------------------------------

    student = Student(
        "Likhitha",
        6,
    )


    # -----------------------------------------------------
    # ADD STUDY TASKS
    # -----------------------------------------------------

    student.add_task(
        StudyTask(
            "Python Algorithms",
            "Programming",
            8,
            10,
            2,
            1,
        )
    )

    student.add_task(
        StudyTask(
            "Probability",
            "Statistics",
            7,
            9,
            2,
            2,
        )
    )

    student.add_task(
        StudyTask(
            "Machine Learning",
            "AI",
            9,
            10,
            3,
            3,
        )
    )


    # -----------------------------------------------------
    # STUDY PLANNER
    # -----------------------------------------------------

    planner = StudyPlanner(
        student
    )

    planner.generate_plan()

    planner.optimize_topics()


    # -----------------------------------------------------
    # GENERATOR
    # -----------------------------------------------------

    print(
        "\n===== GENERATOR ====="
    )

    for task in task_generator(
        [
            "Python",
            "AI",
            "Statistics",
        ]
    ):

        print(task)


    # -----------------------------------------------------
    # REDUCE
    # -----------------------------------------------------

    print(
        "\nTotal hours:",
        calculate_total_hours(
            [2, 2, 3]
        ),
    )


    # -----------------------------------------------------
    # FILTER
    # -----------------------------------------------------

    print(
        "Difficult topics:",
        filter_difficult_tasks(
            [5, 8, 9, 4, 7]
        ),
    )


    # -----------------------------------------------------
    # THREADING
    # -----------------------------------------------------

    print(
        "\n===== THREADING ====="
    )

    run_threads()


    # -----------------------------------------------------
    # MULTIPROCESSING
    # -----------------------------------------------------

    print(
        "\n===== MULTIPROCESSING ====="
    )

    run_multiprocessing()


    # -----------------------------------------------------
    # ASYNCIO
    # -----------------------------------------------------

    print(
        "\n===== ASYNCIO ====="
    )

    asyncio.run(
        run_async()
    )


if __name__ == "__main__":

    main()