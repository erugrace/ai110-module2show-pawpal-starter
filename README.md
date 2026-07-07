# PawPal+

A pet scheduling application that helps owners organize and manage pet care tasks.

PawPal+ is a pet management application that allows users to create pet profiles, 
assign tasks, schedule care activities, and manage recurring responsibilities.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

## Features

- Create pet profiles
- Assign tasks to pets
- Mark tasks as complete
- Automatically reschedule recurring daily tasks
- Sort tasks by due date
- Detect scheduling conflicts
- View upcoming incomplete tasks

## Technologies

- Python
- Dataclasses
- Pytest
- Streamlit
- Git/GitHub

## Running the Project

Clone the repository:

git clone <repository-url>


Install dependencies:

pip install -r requirements.txt


Run tests:

python -m pytest


Run the application:

streamlit run app.py

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

```
# e.g.:
# Daily plan for Biscuit (Golden Retriever):
#   08:00 — Morning walk (30 min) [priority: high]
#   09:00 — Feeding (10 min) [priority: high]
#   ...
```

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:

```
# Paste your pytest output here
```

## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.

## Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `Scheduler.sort_by_time()` | Sorts tasks based on their due time so the schedule is displayed chronologically. |
| Filtering | `Scheduler.get_incomplete_tasks()` | Filters out completed tasks and returns only pending tasks that still need attention. |
| Conflict handling | `Scheduler.detect_conflicts()` | Checks for tasks scheduled at the same time and returns warning messages when duplicate time slots are detected. |
| Recurring tasks | `Task.mark_complete()` / `Scheduler.reschedule_recurring_task()` | Automatically creates the next occurrence of a completed daily task so recurring activities continue in the schedule. |

## 📸 Demo Walkthrough

## 📸 Demo Walkthrough

The PawPal+ application allows users to manage pets and organize their care schedules. The following steps demonstrate the main workflow of the application:

1. The user opens the PawPal+ application and views the pet scheduling interface.

2. The user creates an owner profile and adds pets with information such as name, species, breed, and age.

3. The user assigns tasks to each pet, including task details such as title, description, due date, and frequency.

4. The scheduler collects tasks from all pets and displays upcoming tasks based on their due dates.

5. The user can mark completed tasks as finished. For recurring daily tasks, the system automatically moves the task to the next scheduled day.

6. The scheduler organizes tasks by time and identifies scheduling conflicts when multiple tasks are assigned at the same time.

7. The user can review incomplete and upcoming tasks to better manage their pets' care routines.

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
