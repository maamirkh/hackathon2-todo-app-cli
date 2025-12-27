"""
Unit tests for the TaskService.

This module tests the task operations functionality as specified in the functional requirements.
"""

import pytest
from src.services.task_service import TaskService
from src.services.storage_service import StorageService


class TestTaskService:
    """Test cases for the TaskService."""

    def setup_method(self):
        """Set up a fresh task service for each test."""
        self.storage_service = StorageService()
        self.task_service = TaskService(self.storage_service)

    def test_add_task(self):
        """Test adding a task through the task service."""
        task = self.task_service.add_task("Test Task", "Test Description")

        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description == "Test Description"
        assert task.status is False

        # Verify task is stored
        stored_task = self.task_service.get_task_by_id(1)
        assert stored_task is not None
        assert stored_task.id == 1

    def test_add_task_fails_with_empty_title(self):
        """Test that adding a task with empty title raises ValueError."""
        with pytest.raises(ValueError, match="Task title cannot be empty or contain only whitespace"):
            self.task_service.add_task("")

    def test_delete_task(self):
        """Test deleting a task through the task service."""
        task = self.task_service.add_task("Test Task")
        assert self.task_service.get_task_by_id(task.id) is not None

        result = self.task_service.delete_task(task.id)
        assert result is True

        assert self.task_service.get_task_by_id(task.id) is None

    def test_delete_nonexistent_task(self):
        """Test that deleting a non-existent task returns False."""
        result = self.task_service.delete_task(999)
        assert result is False

    def test_update_task(self):
        """Test updating a task through the task service."""
        original_task = self.task_service.add_task("Original Title", "Original Description")

        updated_task = self.task_service.update_task(
            original_task.id,
            title="Updated Title",
            description="Updated Description"
        )

        assert updated_task is not None
        assert updated_task.id == original_task.id
        assert updated_task.title == "Updated Title"
        assert updated_task.description == "Updated Description"

        # Verify update is reflected in storage
        retrieved_task = self.task_service.get_task_by_id(original_task.id)
        assert retrieved_task is not None
        assert retrieved_task.title == "Updated Title"
        assert retrieved_task.description == "Updated Description"

    def test_update_nonexistent_task(self):
        """Test that updating a non-existent task returns None."""
        result = self.task_service.update_task(999, title="New Title")
        assert result is None

    def test_get_all_tasks(self):
        """Test getting all tasks through the task service."""
        task1 = self.task_service.add_task("Task 1")
        task2 = self.task_service.add_task("Task 2")

        all_tasks = self.task_service.get_all_tasks()
        assert len(all_tasks) == 2
        assert task1 in all_tasks
        assert task2 in all_tasks

    def test_get_task_by_id(self):
        """Test getting a specific task by ID."""
        created_task = self.task_service.add_task("Test Task")

        retrieved_task = self.task_service.get_task_by_id(created_task.id)
        assert retrieved_task is not None
        assert retrieved_task.id == created_task.id
        assert retrieved_task.title == "Test Task"

    def test_get_task_by_id_returns_none_for_nonexistent_task(self):
        """Test that getting a non-existent task returns None."""
        task = self.task_service.get_task_by_id(999)
        assert task is None

    def test_mark_task_complete(self):
        """Test marking a task as complete."""
        task = self.task_service.add_task("Test Task")
        assert task.status is False

        completed_task = self.task_service.mark_task_complete(task.id)
        assert completed_task is not None
        assert completed_task.status is True

        # Verify update is reflected in storage
        retrieved_task = self.task_service.get_task_by_id(task.id)
        assert retrieved_task is not None
        assert retrieved_task.status is True

    def test_mark_task_incomplete(self):
        """Test marking a task as incomplete."""
        task = self.task_service.add_task("Test Task")
        # First mark complete
        self.task_service.mark_task_complete(task.id)
        assert task.status is True

        incomplete_task = self.task_service.mark_task_incomplete(task.id)
        assert incomplete_task is not None
        assert incomplete_task.status is False

        # Verify update is reflected in storage
        retrieved_task = self.task_service.get_task_by_id(task.id)
        assert retrieved_task is not None
        assert retrieved_task.status is False

    def test_toggle_task_status(self):
        """Test toggling a task's status."""
        task = self.task_service.add_task("Test Task")
        original_status = task.status
        assert original_status is False

        toggled_task = self.task_service.toggle_task_status(task.id)
        assert toggled_task is not None
        assert toggled_task.status is not original_status

        # Toggle again
        toggled_again_task = self.task_service.toggle_task_status(task.id)
        assert toggled_again_task is not None
        assert toggled_again_task.status == original_status

    def test_get_completed_tasks(self):
        """Test getting completed tasks."""
        incomplete_task = self.task_service.add_task("Incomplete Task")
        complete_task = self.task_service.add_task("Complete Task")
        self.task_service.mark_task_complete(complete_task.id)

        completed_tasks = self.task_service.get_completed_tasks()
        assert len(completed_tasks) == 1
        assert completed_tasks[0].id == complete_task.id

    def test_get_incomplete_tasks(self):
        """Test getting incomplete tasks."""
        incomplete_task = self.task_service.add_task("Incomplete Task")
        complete_task = self.task_service.add_task("Complete Task")
        self.task_service.mark_task_complete(complete_task.id)

        incomplete_tasks = self.task_service.get_incomplete_tasks()
        assert len(incomplete_tasks) == 1
        assert incomplete_tasks[0].id == incomplete_task.id

    def test_get_task_count(self):
        """Test getting the total task count."""
        assert self.task_service.get_task_count() == 0

        self.task_service.add_task("Task 1")
        assert self.task_service.get_task_count() == 1

        self.task_service.add_task("Task 2")
        assert self.task_service.get_task_count() == 2

        self.task_service.delete_task(1)
        assert self.task_service.get_task_count() == 1