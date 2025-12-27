"""
Unit tests for the StorageService.

This module tests the in-memory storage functionality as specified in the requirements.
"""

import pytest
from src.services.storage_service import StorageService
from src.models.task import Task


class TestStorageService:
    """Test cases for the StorageService."""

    def test_create_task(self):
        """Test creating a task in storage."""
        storage = StorageService()
        task = storage.create_task("Test Task", "Test Description")

        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description == "Test Description"
        assert task.status is False

        # Verify task is stored
        stored_task = storage.get_task(1)
        assert stored_task is not None
        assert stored_task.id == 1
        assert stored_task.title == "Test Task"

    def test_create_task_fails_with_empty_title(self):
        """Test that creating a task with empty title raises ValueError."""
        storage = StorageService()
        with pytest.raises(ValueError, match="Task title cannot be empty or contain only whitespace"):
            storage.create_task("")

    def test_get_task_by_id(self):
        """Test retrieving a task by its ID."""
        storage = StorageService()
        created_task = storage.create_task("Test Task")

        retrieved_task = storage.get_task(created_task.id)
        assert retrieved_task is not None
        assert retrieved_task.id == created_task.id
        assert retrieved_task.title == created_task.title

    def test_get_task_by_id_returns_none_for_nonexistent_task(self):
        """Test that getting a non-existent task returns None."""
        storage = StorageService()
        task = storage.get_task(999)
        assert task is None

    def test_get_all_tasks(self):
        """Test retrieving all tasks."""
        storage = StorageService()
        task1 = storage.create_task("Task 1")
        task2 = storage.create_task("Task 2")

        all_tasks = storage.get_all_tasks()
        assert len(all_tasks) == 2
        assert task1 in all_tasks
        assert task2 in all_tasks

    def test_get_tasks_by_status(self):
        """Test retrieving tasks filtered by status."""
        storage = StorageService()
        incomplete_task = storage.create_task("Incomplete Task")
        complete_task = storage.create_task("Complete Task")
        storage.update_task(complete_task.id, status=True)

        # Get incomplete tasks
        incomplete_tasks = storage.get_tasks_by_status(completed=False)
        assert len(incomplete_tasks) == 1
        assert incomplete_tasks[0].id == incomplete_task.id

        # Get complete tasks
        complete_tasks = storage.get_tasks_by_status(completed=True)
        assert len(complete_tasks) == 1
        assert complete_tasks[0].id == complete_task.id

        # Get all tasks (completed=None)
        all_tasks = storage.get_tasks_by_status(completed=None)
        assert len(all_tasks) == 2

    def test_update_task(self):
        """Test updating a task's attributes."""
        storage = StorageService()
        original_task = storage.create_task("Original Title", "Original Description")

        updated_task = storage.update_task(
            original_task.id,
            title="Updated Title",
            description="Updated Description",
            status=True
        )

        assert updated_task is not None
        assert updated_task.id == original_task.id
        assert updated_task.title == "Updated Title"
        assert updated_task.description == "Updated Description"
        assert updated_task.status is True

        # Verify the update is reflected in storage
        retrieved_task = storage.get_task(original_task.id)
        assert retrieved_task is not None
        assert retrieved_task.title == "Updated Title"
        assert retrieved_task.description == "Updated Description"
        assert retrieved_task.status is True

    def test_update_task_returns_none_for_nonexistent_task(self):
        """Test that updating a non-existent task returns None."""
        storage = StorageService()
        result = storage.update_task(999, title="New Title")
        assert result is None

    def test_delete_task(self):
        """Test deleting a task."""
        storage = StorageService()
        task = storage.create_task("Test Task")

        # Verify task exists
        assert storage.get_task(task.id) is not None

        # Delete task
        result = storage.delete_task(task.id)
        assert result is True

        # Verify task no longer exists
        assert storage.get_task(task.id) is None

    def test_delete_nonexistent_task(self):
        """Test that deleting a non-existent task returns False."""
        storage = StorageService()
        result = storage.delete_task(999)
        assert result is False

    def test_get_task_count(self):
        """Test getting the total task count."""
        storage = StorageService()
        assert storage.get_task_count() == 0

        storage.create_task("Task 1")
        assert storage.get_task_count() == 1

        storage.create_task("Task 2")
        assert storage.get_task_count() == 2

        storage.delete_task(1)
        assert storage.get_task_count() == 1