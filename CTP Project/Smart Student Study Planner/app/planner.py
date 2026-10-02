from app.algorithms import (
    backtracking_timetable,
    best_selection,
    knapsack,
)
from app.models import Student, StudyTask


class StudyPlanner:

    def __init__(
        self,
        student: Student,
    ) -> None:

        self.student = student


    # =====================================================
    # SORT TASKS
    # =====================================================

    def sort_tasks(self) -> list[StudyTask]:

        return sorted(
            self.student.tasks,
            key=lambda task: task.deadline,
        )


    # =====================================================
    # GENERATE PLAN
    # =====================================================

    def generate_plan(self) -> None:

        print(
            "\n===== STUDY PLAN ====="
        )

        tasks = self.sort_tasks()

        for task in tasks:

            print(
                f"{task.subject}: "
                f"{task.name} - "
                f"{task.hours} hour(s)"
            )

        task_data = [
            (
                task.name,
                task.hours,
            )
            for task in tasks
        ]

        timetable = backtracking_timetable(
            task_data,
            self.student.available_hours,
        )

        print(
            "\nTimetable:"
        )

        for index, task_name in enumerate(
            timetable,
            start=1,
        ):

            print(
                f"Slot {index}: "
                f"{task_name}"
            )


    # =====================================================
    # OPTIMIZE TOPICS
    # =====================================================

    def optimize_topics(self) -> None:

        values = [
            task.importance
            for task in self.student.tasks
        ]

        weights = [
            task.hours
            for task in self.student.tasks
        ]

        result = knapsack(
            values,
            weights,
            self.student.available_hours,
        )

        print(
            "\nMaximum study value:",
            result,
        )

        result2 = best_selection(
            values,
            weights,
            self.student.available_hours,
        )

        print(
            "Branch & Bound value:",
            result2,
        )