"""
Integration tests for the complete task workflow.

This module tests the integration between all components as specified in the requirements.
"""

from src.services.storage_service import StorageService
from src.services.task_service import TaskService
from src.models.task import Task


class TestTaskWorkflow:
    """Test cases for the complete task workflow integration."""

    def setup_method(self):
        """Set up a fresh task service for each test."""
        self.storage_service = StorageService()
        self.task_service = TaskService(self.storage_service)

    def test_complete_task_lifecycle(self):
        """Test the complete lifecycle of a task: create, read, update, delete."""
        # Create a task
        created_task = self.task_service.add_task("Buy groceries", "Milk, bread, eggs")
        assert created_task.id == 1
        assert created_task.title == "Buy groceries"
        assert created_task.description == "Milk, bread, eggs"
        assert created_task.status is False

        # Retrieve the task
        retrieved_task = self.task_service.get_task_by_id(1)
        assert retrieved_task is not None
        assert retrieved_task.id == 1
        assert retrieved_task.title == "Buy groceries"

        # Update the task
        updated_task = self.task_service.update_task(1, title="Buy groceries and cook dinner", description="Milk, bread, eggs, chicken")
        assert updated_task is not None
        assert updated_task.title == "Buy groceries and cook dinner"
        assert updated_task.description == "Milk, bread, eggs, chicken"

        # Verify update is reflected in storage
        verified_task = self.task_service.get_task_by_id(1)
        assert verified_task is not None
        assert verified_task.title == "Buy groceries and cook dinner"
        assert verified_task.description == "Milk, bread, eggs, chicken"

        # Mark as complete
        completed_task = self.task_service.mark_task_complete(1)
        assert completed_task is not None
        assert completed_task.status is True

        # Verify completion is reflected in storage
        final_task = self.task_service.get_task_by_id(1)
        assert final_task is not None
        assert final_task.status is True

        # Delete the task
        delete_result = self.task_service.delete_task(1)
        assert delete_result is True

        # Verify task is deleted
        deleted_task = self.task_service.get_task_by_id(1)
        assert deleted_task is None

    def test_multiple_tasks_workflow(self):
        """Test workflow with multiple tasks."""
        # Add multiple tasks
        task1 = self.task_service.add_task("Task 1", "Description 1")
        task2 = self.task_service.add_task("Task 2", "Description 2")
        task3 = self.task_service.add_task("Task 3", "Description 3")

        # Verify all tasks exist
        all_tasks = self.task_service.get_all_tasks()
        assert len(all_tasks) == 3

        # Mark one as complete
        completed_task = self.task_service.mark_task_complete(task2.id)
        assert completed_task is not None
        assert completed_task.status is True

        # Verify status counts
        all_tasks = self.task_service.get_all_tasks()
        completed_tasks = self.task_service.get_completed_tasks()
        incomplete_tasks = self.task_service.get_incomplete_tasks()

        assert len(all_tasks) == 3
        assert len(completed_tasks) == 1
        assert len(incomplete_tasks) == 2

        # Update a task
        updated_task = self.task_service.update_task(task1.id, title="Updated Task 1")
        assert updated_task is not None
        assert updated_task.title == "Updated Task 1"

        # Delete a task
        delete_result = self.task_service.delete_task(task3.id)
        assert delete_result is True

        # Verify final state
        final_tasks = self.task_service.get_all_tasks()
        assert len(final_tasks) == 2

    def test_task_status_transitions(self):
        """Test task status transitions."""
        task = self.task_service.add_task("Test Task")

        # Initially incomplete
        assert task.status is False

        # Mark complete
        completed_task = self.task_service.mark_task_complete(task.id)
        assert completed_task.status is True

        # Mark incomplete
        incomplete_task = self.task_service.mark_task_incomplete(task.id)
        assert incomplete_task.status is False

        # Toggle to complete
        toggled_task = self.task_service.toggle_task_status(task.id)
        assert toggled_task.status is True

        # Toggle back to incomplete
        toggled_back_task = self.task_service.toggle_task_status(task.id)
        assert toggled_back_task.status is False

    def test_error_handling_workflow(self):
        """Test error handling in the workflow."""
        # Try to get a non-existent task
        nonexistent_task = self.task_service.get_task_by_id(999)
        assert nonexistent_task is None

        # Try to update a non-existent task
        updated_task = self.task_service.update_task(999, title="New Title")
        assert updated_task is None

        # Try to delete a non-existent task
        delete_result = self.task_service.delete_task(999)
        assert delete_result is False

        # Try to mark complete a non-existent task
        completed_task = self.task_service.mark_task_complete(999)
        assert completed_task is None

        # Verify the service still works after error attempts
        new_task = self.task_service.add_task("Valid Task")
        assert new_task is not None
        assert new_task.title == "Valid Task"