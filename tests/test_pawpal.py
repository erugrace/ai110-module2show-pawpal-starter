from datetime import datetime, timedelta

from pawpal_system import Owner, Pet, Task, Scheduler



def test_mark_task_complete():

    task = Task(
        id=1,
        title="Feed Dog",
        description="Give dog food",
        due_date=datetime(2026, 7, 7, 8, 0)
    )

    task.mark_complete()

    assert task.completed == True



def test_pet_add_task():

    pet = Pet(
        id=1,
        name="Buddy",
        species="Dog",
        breed="Golden Retriever",
        age=3
    )

    task = Task(
        id=1,
        title="Walk",
        description="Morning walk",
        due_date=datetime(2026, 7, 7, 10, 0)
    )

    pet.add_task(task)

    assert len(pet.tasks) == 1

    assert task.pet == pet



def test_owner_add_pet():

    owner = Owner(
        id=1,
        name="Grace",
        email="grace@email.com"
    )

    pet = Pet(
        id=1,
        name="Buddy",
        species="Dog",
        breed="Golden Retriever",
        age=3
    )

    owner.add_pet(pet)

    assert len(owner.pets) == 1

    assert pet.owner == owner



def test_scheduler_sort_by_time():

    owner = Owner(
        id=1,
        name="Grace",
        email="grace@email.com"
    )


    pet = Pet(
        id=1,
        name="Buddy",
        species="Dog",
        breed="Golden Retriever",
        age=3
    )


    owner.add_pet(pet)


    late_task = Task(
        id=1,
        title="Walk",
        description="Walk dog",
        due_date=datetime(2026, 7, 7, 10, 0)
    )


    early_task = Task(
        id=2,
        title="Feed",
        description="Feed dog",
        due_date=datetime(2026, 7, 7, 8, 0)
    )


    pet.add_task(late_task)
    pet.add_task(early_task)


    scheduler = Scheduler(owner)


    sorted_tasks = scheduler.sort_by_time()


    assert sorted_tasks[0].title == "Feed"



def test_conflict_detection():

    owner = Owner(
        id=1,
        name="Grace",
        email="grace@email.com"
    )


    pet = Pet(
        id=1,
        name="Buddy",
        species="Dog",
        breed="Golden Retriever",
        age=3
    )


    owner.add_pet(pet)


    task1 = Task(
        id=1,
        title="Feed",
        description="Feed dog",
        due_date=datetime(2026, 7, 7, 8, 0)
    )


    task2 = Task(
        id=2,
        title="Medicine",
        description="Give medicine",
        due_date=datetime(2026, 7, 7, 8, 0)
    )


    pet.add_task(task1)
    pet.add_task(task2)


    scheduler = Scheduler(owner)


    conflicts = scheduler.detect_conflicts()


    assert len(conflicts) == 1



def test_daily_task_recurring():

    task = Task(
        id=1,
        title="Feed Dog",
        description="Feed every morning",
        due_date=datetime(2026, 7, 7, 8, 0),
        frequency="daily"
    )


    task.mark_complete()


    assert task.completed == False

    assert task.due_date == datetime(2026, 7, 8, 8, 0)

def test_owner_remove_pet():

    owner = Owner(
        id=1,
        name="Grace",
        email="grace@email.com"
    )


    pet = Pet(
        id=1,
        name="Buddy",
        species="Dog",
        breed="Golden Retriever",
        age=3
    )


    owner.add_pet(pet)

    owner.remove_pet(pet)


    assert len(owner.pets) == 0

    assert pet.owner == None

def test_cancel_task():

    owner = Owner(
        id=1,
        name="Grace",
        email="grace@email.com"
    )


    pet = Pet(
        id=1,
        name="Buddy",
        species="Dog",
        breed="Golden Retriever",
        age=3
    )


    owner.add_pet(pet)


    task = Task(
        id=1,
        title="Walk",
        description="Walk dog",
        due_date=datetime(2026,7,7,10,0)
    )


    pet.add_task(task)


    scheduler = Scheduler(owner)


    scheduler.cancel_task(task)


    assert len(pet.tasks) == 0

    assert task.pet == None
def test_get_upcoming_tasks():

    owner = Owner(
        id=1,
        name="Grace",
        email="grace@email.com"
    )


    pet = Pet(
        id=1,
        name="Buddy",
        species="Dog",
        breed="Golden Retriever",
        age=3
    )


    owner.add_pet(pet)


    task = Task(
        id=1,
        title="Vet Appointment",
        description="Annual checkup",
        due_date=datetime.now() + timedelta(days=5)
    )


    pet.add_task(task)


    scheduler = Scheduler(owner)


    upcoming = scheduler.get_upcoming_tasks()


    assert len(upcoming) == 1