from dataclasses import dataclass


@dataclass
class StudyTask:
    name: str
    subject: str
    difficulty: int
    importance: int
    hours: int
    deadline: int


class Person:
    def __init__(self, name: str) -> None:
        self.name = name


class Student(Person):
    def __init__(
        self,
        name: str,
        available_hours: int,
    ) -> None:
        super().__init__(name)

        self.available_hours = available_hours

        self.tasks: list[StudyTask] = []

    def add_task(
        self,
        task: StudyTask,
    ) -> None:
        self.tasks.append(task)