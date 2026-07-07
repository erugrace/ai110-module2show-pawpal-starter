"""PawPal — pet scheduling domain model.

Dataclass skeletons for Owner, Pet, Task, and Scheduler, based on diagrams/uml.mmd.
Method bodies are left as `raise NotImplementedError` stubs to be filled in.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Owner:
    id: int
    name: str
    email: str
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        raise NotImplementedError

    def remove_pet(self, pet: Pet) -> None:
        raise NotImplementedError


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
        raise NotImplementedError


@dataclass
class Task:
    id: int
    title: str
    description: str
    due_date: datetime
    completed: bool = False
    pet: Pet | None = None

    def mark_complete(self) -> None:
        raise NotImplementedError

    def reschedule(self, new_date: datetime) -> None:
        raise NotImplementedError


@dataclass
class Scheduler:
    tasks: list[Task] = field(default_factory=list)

    def schedule_task(self, task: Task) -> None:
        raise NotImplementedError

    def cancel_task(self, task: Task) -> None:
        raise NotImplementedError

    def get_tasks_for_pet(self, pet: Pet) -> list[Task]:
        raise NotImplementedError

    def get_upcoming_tasks(self) -> list[Task]:
        raise NotImplementedError
