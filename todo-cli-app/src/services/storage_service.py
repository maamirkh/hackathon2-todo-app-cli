"""
In-memory storage service for the Todo In-Memory Python Console App.

This module implements the storage operations for tasks using Python data structures,
providing O(1) average time complexity for CRUD operations as specified in the plan.
"""

from typing import Dict, List, Optional
from src.models.task import Task


class StorageService:
    """
    Manages in-memory storage of tasks using a dictionary structure.

    The storage maintains tasks with integer IDs as keys and Task objects as values,
    supporting up to 1000 tasks efficiently as specified in the requirements.
    """

    def __init__(self):
        """Initialize the in-memory storage with an empty task dictionary."""
        self._tasks: Dict[int, Task] = {}
        self._next_id = 1

    def create_task(self, title: str, description: str = "") -> Task:
        """
        Create a new task and store it in memory.

        Args:
            title: The title of the task (required)
            description: The description of the task (optional)

        Returns:
            The created Task object with a unique ID and default incomplete status
        """
        # Validate title before creating task
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty or contain only whitespace")

        # Create task with auto-generated ID
        task_id = self._get_next_id()
        task = Task(id=task_id, title=title.strip(), description=description, status=False)

        # Store the task
        self._tasks[task_id] = task
        return task

    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Retrieve a task by its ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            The Task object if found, None otherwise
        """
        return self._tasks.get(task_id)

    def get_all_tasks(self) -> List[Task]:
        """
        Retrieve all tasks in the storage.

        Returns:
            A list of all Task objects in the storage
        """
        return list(self._tasks.values())

    def get_tasks_by_status(self, completed: Optional[bool] = None) -> List[Task]:
        """
        Retrieve tasks filtered by status.

        Args:
            completed: If True, return completed tasks; if False, return incomplete tasks;
                      if None, return all tasks (default)

        Returns:
            A list of Task objects matching the status filter
        """
        if completed is None:
            return self.get_all_tasks()

        return [task for task in self._tasks.values() if task.status == completed]

    def update_task(self, task_id: int, title: Optional[str] = None,
                   description: Optional[str] = None, status: Optional[bool] = None) -> Optional[Task]:
        """
        Update an existing task's attributes.

        Args:
            task_id: The ID of the task to update
            title: New title for the task (optional)
            description: New description for the task (optional)
            status: New status for the task (optional)

        Returns:
            The updated Task object if successful, None if task doesn't exist
        """
        task = self.get_task(task_id)
        if task is None:
            return None

        # Update attributes if provided
        if title is not None:
            task.update_title(title)
        if description is not None:
            task.update_description(description)
        if status is not None:
            task.status = status
            task.validate()  # Re-validate after status change

        return task

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task from storage.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if the task was deleted, False if task didn't exist
        """
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False

    def _get_next_id(self) -> int:
        """
        Get the next available ID for a new task.

        Returns:
            An integer ID that is unique within the current session
        """
        while self._next_id in self._tasks:
            self._next_id += 1
        return self._next_id

    def get_task_count(self) -> int:
        """
        Get the total number of tasks in storage.

        Returns:
            The number of tasks currently stored
        """
        return len(self._tasks)