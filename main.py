from datetime import datetime

from pawpal_system import Owner, Pet, Task, Scheduler

owner = Owner(
    id=1,
    name="Grace",
    email="grace@email.com"
)

dog = Pet(
    id=1,
    name="Buddy",
    species="Dog",
    breed="Golden Retriever",
    age=3
)

cat = Pet(
    id=2,
    name="Whiskers",
    species="Cat",
    breed="Siamese",
    age=2
)

#Assign both pets to buddy
owner.add_pet(dog)
owner.add_pet(cat)
task1 = Task(
    id=1,
    title="Clean Litter Box",
    description="Clean Whiskers litter",
    due_date=datetime(2026,7,7,10,0)
    #datetime means Year: 2026 Month: July Day: 7,Hour: 8 ,Minute: 00
)


task2 = Task(
    id=2,
    title="Morning Walk",
    description="Walk Buddy",
    due_date=datetime(2026,7,7,8,0)
)


task3 = Task(
    id=3,
    title="Feed Buddy",
    description="Breakfast",
    due_date=datetime(2026,7,7,9,0)
)
task4 = Task(
    id=4,
    title="Give Medicine",
    description="Medication",
    due_date=datetime(2026,7,7,8,0)
)




#Add tasks to the pets
dog.add_task(task1)
dog.add_task(task2)

cat.add_task(task3)
cat.add_task(task4)

#Create a Scheduler
scheduler = Scheduler(owner)
print("Today's Schedule")
print("-" * 40)

for task in scheduler.get_all_tasks():
    print(
        f"{task.due_date.strftime('%I:%M %p')} | "
        f"{task.pet.name} | "
        f"{task.title}"
    )

print("Sorted Schedule")

for task in scheduler.sort_by_time():
    print(
        task.due_date.strftime("%I:%M %p"),
        task.title
    )

task1.mark_complete()
print("Incomplete Tasks")

for task in scheduler.get_incomplete_tasks():
    print(task.title)


print("Conflicts")
print("*" * 30)
conflicts = scheduler.detect_conflicts()

for warning in conflicts:
    print(warning)