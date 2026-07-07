# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?
I designed the PawPal+ system around four main classes: Owner, Pet, Task, and Scheduler.

The Owner class represents the pet owner and stores all of their pets.

The Pet class represents an individual pet and stores information about that pet along with its list of care tasks.

The Task class represents a single activity, such as feeding, walking, or giving medication. Each task stores information like its description, scheduled time, frequency, and whether it has been completed.

The Scheduler class manages tasks across all pets. It is responsible for retrieving tasks, organizing schedules, sorting tasks by time, and later detecting scheduling conflicts.

**b. Design changes**

- Did your design change during implementation?
No
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

### a. Constraints and priorities

The PawPal+ scheduler considers several constraints when managing pet tasks:

- Due date and time: Tasks are organized based on when they need to be completed. Earlier tasks are prioritized before later tasks.
- Task completion status: Completed tasks are excluded from upcoming schedules so users only see tasks that still require attention.
- Recurring tasks: Daily tasks are automatically rescheduled for the next day after completion.
- Scheduling conflicts: The scheduler checks whether multiple tasks occur at the same time and alerts the user.

The most important constraint was task timing because pet care activities often depend on specific schedules. For example, feeding a pet or giving medication should happen at the appropriate time. After timing, completion status and recurring behavior were prioritized because they help users maintain consistent routines.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?
### b. Tradeoffs

One tradeoff the scheduler makes is that it prioritizes the scheduled time of tasks rather than automatically rearranging tasks based on other factors such as task difficulty or personal preferences.

For example, if two tasks occur at the same time, PawPal+ detects the conflict and informs the user instead of automatically moving one task. This approach gives the user control over their pet's schedule because they may have additional information that the scheduler does not know, such as availability or importance of a specific task.

This tradeoff is reasonable because pet care schedules are personal, and automatically changing appointments could create unexpected problems. Alerting users about conflicts while allowing them to make decisions provides a safer and more flexible solution.
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
AI helped me to brainstorm design and debug code with understanding what the plan for the code.
- What kinds of prompts or questions were most helpful?
inquiry prompts

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?
checking and validating if the suggestions are related to the uml and plan i had

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?
### a. What you tested

I used pytest to verify that the main functionality of PawPal+ works correctly.

The behaviors tested include:

- Creating tasks and marking them as complete.
- Adding tasks to pets and verifying that tasks are correctly associated with the correct pet.
- Adding pets to owners and confirming ownership relationships.
- Sorting tasks by due date to ensure the scheduler displays tasks in the correct order.
- Detecting scheduling conflicts when multiple tasks have the same due date and time.
- Handling recurring daily tasks by moving the due date to the next day after completion.
- Removing pets from owners and canceling scheduled tasks.

These tests were important because they verify that the core relationships between Owner, Pet, Task, and Scheduler work correctly. They also help prevent future changes from breaking existing functionality. Automated testing gives confidence that the application behaves as expected without needing to manually check every feature each time the code changes.

**b. Confidence**

- How confident are you that your scheduler works correctly?
a 100% sure
- What edge cases would you test next if you had more time?
Not sure yet

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
Testing Reflection

I used pytest to test the main functionality of PawPal+. 
The tests verify that owners can add and remove pets, pets can receive tasks, 
and schedulers correctly sort tasks and detect conflicts.

Writing tests helped identify mismatches between my expected design and my actual implementation. 
The testing phase improved confidence that changes to the application would not break existing functionality.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
I'm not sure yet
**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
It can help accordingly if you give it the right instructions.
