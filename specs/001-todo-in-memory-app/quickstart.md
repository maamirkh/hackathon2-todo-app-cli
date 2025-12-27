# Quickstart Guide: Phase I – Todo In-Memory Python Console App

**Date**: 2025-12-27
**Feature**: Phase I – Todo In-Memory Python Console App
**Branch**: 001-todo-in-memory-app

## Overview

This guide provides quick instructions for setting up and running the Phase I Todo In-Memory Python Console App. The application is a command-line interface tool for managing personal tasks efficiently.

## Prerequisites

- Python 3.13 or higher
- UV package manager (optional, for dependency management)

## Installation

### Option 1: Direct Execution (No Installation Required)
1. Clone or download the repository
2. Navigate to the project directory
3. Run the application directly using Python

```bash
python src/main.py
```

### Option 2: Using UV Package Manager
1. Install dependencies using UV:
```bash
uv sync
```

2. Run the application:
```bash
uv run python src/main.py
```

## Running the Application

### Basic Execution
```bash
python src/main.py
```

### Command-Line Options
The application supports direct command operations:

- Add a task: `python src/main.py add "Task Title" "Optional Description"`
- List tasks: `python src/main.py list`
- Complete a task: `python src/main.py complete <task_id>`
- Delete a task: `python src/main.py delete <task_id>`

## Using the Interactive Menu

Once the application starts, you'll see a menu with the following options:

1. **Add Task** - Create a new task with title and optional description
2. **View Tasks** - Display all tasks with status indicators
3. **Update Task** - Modify an existing task's title, description, or status
4. **Delete Task** - Remove a task from the list
5. **Mark Complete/Incomplete** - Change a task's completion status
6. **Help** - Display available commands and usage
7. **Exit** - Quit the application

## Example Usage

### Adding a Task
```
> 1
Enter task title: Buy groceries
Enter task description (optional): Milk, bread, eggs
Task added successfully with ID: 1
```

### Viewing Tasks
```
> 2
ID  | Title           | Status     | Description
----|-----------------|------------|------------------
1   | Buy groceries   | Incomplete | Milk, bread, eggs
2   | Call dentist    | Complete   | Schedule appointment
```

### Marking a Task Complete
```
> 5
Enter task ID: 1
Task marked as complete
```

## Important Notes

- **Data Persistence**: All tasks are stored in memory only and will be lost when the application exits
- **Single User**: The application is designed for single-user operation
- **Task Limits**: The application supports up to 1000 tasks in memory
- **Session Based**: Each run of the application starts with an empty task list

## Troubleshooting

### Common Issues
- **Python Version**: Ensure you're using Python 3.13 or higher
- **Missing Modules**: If you encounter import errors, check your Python environment
- **Permission Errors**: Make sure you have execute permissions for the Python files

### Error Messages
- **"Task title cannot be empty"**: Task titles must contain at least one non-whitespace character
- **"Task ID not found"**: Verify the task ID exists before attempting operations
- **"Invalid command"**: Check the menu options for valid commands

## Getting Help

For additional help, use the built-in help option within the application or refer to the full documentation in the project repository.