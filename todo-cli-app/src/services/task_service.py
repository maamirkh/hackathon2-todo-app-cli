"""
Task operations service for the Todo In-Memory Python Console App.

This module implements the core task operations (CRUD + status changes) as specified
in the functional requirements, interacting with the storage service.
"""

from typing import List, Optional
from src.models.task import Task
from src.services.storage_service import StorageService


class TaskService:
    """
    Provides business logic for task operations including add, delete, update, view,
    and mark complete/incomplete functionality as specified in the requirements.
    """

    def __init__(self, storage_service: StorageService):
        """
        Initialize the task service with a storage service dependency.

        Args:
            storage_service: The storage service to use for data operations
        """
        self.storage_service = storage_service

    def add_task(self, title: str, description: str = "") -> Task:
        """
        Add a new task to the system.

        Implements FR-001: System MUST allow users to add new tasks with a required title,
        optional description, and default incomplete status.

        Args:
            title: The title of the task (required)
            description: The description of the task (optional)

        Returns:
            The created Task object

        Raises:
            ValueError: If the title is empty or invalid
        """
        # Validate input before creating task
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty or contain only whitespace")

        # Create and store the task
        task = self.storage_service.create_task(title.strip(), description)
        return task

    def delete_task(self, task_id: int) -> bool:
        """
        Delete an existing task from the system.

        Implements FR-002: System MUST allow users to delete existing tasks by identifier.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if the task was deleted, False if task didn't exist
        """
        return self.storage_service.delete_task(task_id)

    def update_task(self, task_id: int, title: Optional[str] = None,
                   description: Optional[str] = None) -> Optional[Task]:
        """
        Update an existing task's attributes (title and description).

        Implements FR-003: System MUST allow users to update existing tasks including title and description.

        Args:
            task_id: The ID of the task to update
            title: New title for the task (optional)
            description: New description for the task (optional)

        Returns:
            The updated Task object if successful, None if task doesn't exist
        """
        # Get the existing task to check if it exists
        existing_task = self.storage_service.get_task(task_id)
        if existing_task is None:
            return None

        # Update the task with provided attributes
        updated_task = self.storage_service.update_task(task_id, title, description)
        return updated_task

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in the system.

        Implements FR-004: System MUST allow users to view all tasks in a formatted list with status indicators.

        Returns:
            A list of all Task objects in the system
        """
        return self.storage_service.get_all_tasks()

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Get a specific task by its ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            The Task object if found, None otherwise
        """
        return self.storage_service.get_task(task_id)

    def mark_task_complete(self, task_id: int) -> Optional[Task]:
        """
        Mark a task as complete.

        Implements FR-005: System MUST allow users to mark tasks as complete or incomplete.

        Args:
            task_id: The ID of the task to mark as complete

        Returns:
            The updated Task object if successful, None if task doesn't exist
        """
        # Get the existing task to check if it exists
        existing_task = self.storage_service.get_task(task_id)
        if existing_task is None:
            return None

        # Update the task status to complete
        updated_task = self.storage_service.update_task(task_id, status=True)
        return updated_task

    def mark_task_incomplete(self, task_id: int) -> Optional[Task]:
        """
        Mark a task as incomplete.

        Implements FR-005: System MUST allow users to mark tasks as complete or incomplete.

        Args:
            task_id: The ID of the task to mark as incomplete

        Returns:
            The updated Task object if successful, None if task doesn't exist
        """
        # Get the existing task to check if it exists
        existing_task = self.storage_service.get_task(task_id)
        if existing_task is None:
            return None

        # Update the task status to incomplete
        updated_task = self.storage_service.update_task(task_id, status=False)
        return updated_task

    def toggle_task_status(self, task_id: int) -> Optional[Task]:
        """
        Toggle a task's completion status.

        Args:
            task_id: The ID of the task to toggle

        Returns:
            The updated Task object if successful, None if task doesn't exist
        """
        # Get the existing task to check if it exists
        existing_task = self.storage_service.get_task(task_id)
        if existing_task is None:
            return None

        # Toggle the status
        new_status = not existing_task.status
        updated_task = self.storage_service.update_task(task_id, status=new_status)
        return updated_task

    def get_completed_tasks(self) -> List[Task]:
        """
        Get all completed tasks.

        Returns:
            A list of completed Task objects
        """
        return self.storage_service.get_tasks_by_status(completed=True)

    def get_incomplete_tasks(self) -> List[Task]:
        """
        Get all incomplete tasks.

        Returns:
            A list of incomplete Task objects
        """
        return self.storage_service.get_tasks_by_status(completed=False)

    def get_task_count(self) -> int:
        """
        Get the total number of tasks in the system.

        Returns:
            The number of tasks currently in the system
        """
        return self.storage_service.get_task_count()