"""
Unit tests for the main application entry point.

This module tests that the main application components can be initialized correctly.
"""

from src.main import main
from src.services.storage_service import StorageService
from src.services.task_service import TaskService
from src.cli.cli_interface import CLIInterface


def test_main_components_initialization():
    """Test that main application components can be initialized without errors."""
    # Test storage service initialization
    storage_service = StorageService()
    assert storage_service is not None
    assert storage_service.get_task_count() == 0

    # Test task service initialization
    task_service = TaskService(storage_service)
    assert task_service is not None

    # Test CLI interface initialization
    cli_interface = CLIInterface(task_service)
    assert cli_interface is not None

    # Verify that we can perform basic operations
    task = task_service.add_task("Test Task")
    assert task is not None
    assert task.id == 1
    assert task.title == "Test Task"

    # Verify the task is stored
    retrieved_task = task_service.get_task_by_id(1)
    assert retrieved_task is not None
    assert retrieved_task.id == 1