"""
Unit tests for the Task model.

This module tests the Task entity and its validation methods as specified in the data model.
"""

import pytest
from src.models.task import Task


class TestTask:
    """Test cases for the Task model."""

    def test_task_creation_with_valid_data(self):
        """Test creating a task with valid data."""
        task = Task(id=1, title="Test Task", description="Test Description", status=False)
        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description == "Test Description"
        assert task.status is False

    def test_task_creation_with_minimal_data(self):
        """Test creating a task with minimal required data."""
        task = Task(id=1, title="Test Task")
        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description == ""
        assert task.status is False

    def test_task_creation_fails_with_empty_title(self):
        """Test that creating a task with empty title raises ValueError."""
        with pytest.raises(ValueError, match="Task title cannot be empty or contain only whitespace"):
            Task(id=1, title="")

    def test_task_creation_fails_with_whitespace_only_title(self):
        """Test that creating a task with whitespace-only title raises ValueError."""
        with pytest.raises(ValueError, match="Task title cannot be empty or contain only whitespace"):
            Task(id=1, title="   ")

    def test_task_creation_fails_with_title_exceeding_max_length(self):
        """Test that creating a task with title exceeding max length raises ValueError."""
        long_title = "A" * 1001  # Exceeds 1000 character limit
        with pytest.raises(ValueError, match="Task title cannot exceed 1000 characters"):
            Task(id=1, title=long_title)

    def test_task_creation_with_description_exceeding_max_length(self):
        """Test that creating a task with description exceeding max length raises ValueError."""
        long_description = "A" * 2001  # Exceeds 2000 character limit
        with pytest.raises(ValueError, match="Task description cannot exceed 2000 characters"):
            Task(id=1, title="Test Task", description=long_description)

    def test_task_update_title(self):
        """Test updating task title with valid data."""
        task = Task(id=1, title="Original Title")
        task.update_title("New Title")
        assert task.title == "New Title"

    def test_task_update_title_fails_with_empty_title(self):
        """Test that updating task title with empty string raises ValueError."""
        task = Task(id=1, title="Original Title")
        with pytest.raises(ValueError, match="Task title cannot be empty or contain only whitespace"):
            task.update_title("")

    def test_task_update_description(self):
        """Test updating task description with valid data."""
        task = Task(id=1, title="Test Task", description="Original Description")
        task.update_description("New Description")
        assert task.description == "New Description"

    def test_task_update_description_with_none(self):
        """Test updating task description with None sets it to empty string."""
        task = Task(id=1, title="Test Task", description="Original Description")
        task.update_description(None)
        assert task.description == ""

    def test_task_toggle_status(self):
        """Test toggling task status."""
        task = Task(id=1, title="Test Task", status=False)
        assert task.status is False
        task.toggle_status()
        assert task.status is True
        task.toggle_status()
        assert task.status is False

    def test_task_is_complete_method(self):
        """Test the is_complete method."""
        task = Task(id=1, title="Test Task", status=True)
        assert task.is_complete() is True

        task.status = False
        assert task.is_complete() is False

    def test_task_is_incomplete_method(self):
        """Test the is_incomplete method."""
        task = Task(id=1, title="Test Task", status=False)
        assert task.is_incomplete() is True

        task.status = True
        assert task.is_incomplete() is False