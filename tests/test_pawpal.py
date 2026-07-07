from datetime import datetime

from pawpal_system import Owner, Pet, Task

def test_mark_complete():
    task = Task(
        id=1,
        title="Feed Dog",
        description="Feed Buddy",
        due_date=datetime(2026,7,7,8,0)
    )

    task.mark_complete()

    assert task.completed is True

def test_add_task():
    pet = Pet(
        id=1,
        name="Buddy",
        species="Dog",
        breed="Golden Retriever",
        age=3
    )

    task = Task(
        id=1,
        title="Feed Dog",
        description="Breakfast",
        due_date=datetime(2026,7,7,8,0)
    )

    pet.add_task(task)

    assert len(pet.tasks) == 1