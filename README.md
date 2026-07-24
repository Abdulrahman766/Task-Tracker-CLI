# Task Tracker CLI


## A simple Python command-line tool where you can list and track all the important things you need to do for your work, daily routine, etc...


# Installation 
you can this tool by either:
* cloning this repository to your machine:
https://github.com/Abdulrahman766/Task-Tracker-CLI.git

* or by downloading a zip of this repository from the green "code" icon:
  <img width="500" height="400" alt="Screenshot 2026-07-25 015545" src="https://github.com/user-attachments/assets/e319ba19-3fcb-4ded-9d78-7cec41cc5f25" />

# How to run Task Tracker tool

1. Open the Windows Command Prompt or any other command prompt 
2. Navigate to the repository folder: cd Task_tracker 
3. Type "python" followed by the name of the main file, "task_cli.py": python task_cli.py
4. Type the command you want to run (add, update, mark-in-progress, mark-done-list): e.g., python task_cli.py add "buy groceries"


# Usage

- `add`: Add a new task

```bash
python task_cli.py add <task> 
```

- `list`: List all tasks

```bash
python task_cli.py list
```

- `update`: Update a task

```bash
python task_cli.py update <id> <task>
```

- `delete`: Delete a task

```bash
python task_cli.py delete <id>
```

- `mark-in-progress`: changes the task status from "todo" to "in progress"

```bash
  python task_cli.py mark-in-progress <id>
```

- `mark-done`: changes the task status from "in progress" to "done"

```bash
  python task_cli.py mark-done <id>
```

