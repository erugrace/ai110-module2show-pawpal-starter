"""PawPal — pet scheduling domain model.

Dataclass skeletons for Owner, Pet, Task, and Scheduler, based on diagrams/uml.mmd.
Method bodies are left as `raise NotImplementedError` stubs to be filled in.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta


@dataclass
class Owner:
    id: int
    name: str
    email: str
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the owner's list and assign ownership."""
        pet.owner = self
        self.pets.append(pet)

    def remove_pet(self, pet: Pet) -> None:
        if pet in self.pets:
            self.pets.remove(pet)
            pet.owner = None



@dataclass
class Pet:
    id: int
    name: str
    species: str
    breed: str
    age: int
    owner: Owner | None = None
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
       task.pet = self
       self.tasks.append(task)


@dataclass
class Task:
    id: int
    title: str
    description: str
    due_date: datetime
    frequency: str = "once"
    completed: bool = False
    pet: Pet | None = None

    def mark_complete(self):
      self.completed = True
      if self.frequency == "daily":
        self.due_date += timedelta(days=1)
        self.completed = False

    def reschedule(self, new_date: datetime) -> None:
       self.due_date = new_date


@dataclass
class Scheduler:
    owner: Owner

    def get_all_tasks(self) -> list[Task]:
        tasks = []

        for pet in self.owner.pets:
            tasks.extend(pet.tasks)

        return tasks

    def schedule_task(self, pet: Pet, task: Task) -> None:
        pet.add_task(task)

    def cancel_task(self, task: Task) -> None:
        if task.pet and task in task.pet.tasks:
            task.pet.tasks.remove(task)
            task.pet = None

    def get_tasks_for_pet(self, pet: Pet) -> list[Task]:
        return pet.tasks

    def get_upcoming_tasks(self) -> list[Task]:
        now = datetime.now()

        return [
            task
            for task in self.get_all_tasks()
            if task.due_date >= now and not task.completed
        ]
    def sort_by_time(self) -> list[Task]:
       return sorted(
           self.get_all_tasks(),
           key=lambda task: task.due_date
        )
    def get_incomplete_tasks(self) -> list[Task]:
        return [
           task
           for task in self.get_all_tasks()
           if not task.completed
        ]
    def detect_conflicts(self):

       conflicts = []

       tasks = self.get_all_tasks()

       for i in range(len(tasks)):

            for j in range(i+1, len(tasks)):

                if tasks[i].due_date == tasks[j].due_date:

                    conflicts.append(
                        f"{tasks[i].title} conflicts with {tasks[j].title}"
                    )

       return conflicts