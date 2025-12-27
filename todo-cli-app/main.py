from src.services.storage_service import StorageService
from src.services.task_service import TaskService
from src.cli.cli_interface import CLIInterface


def main():
    """
    Main function to initialize and run the Todo application.

    This function:
    1. Sets up the storage service for in-memory task storage
    2. Creates the task service with business logic
    3. Initializes the CLI interface for user interaction
    4. Runs the application in either interactive or command-line mode
    """
    # Initialize the storage service (in-memory)
    storage_service = StorageService()

    # Initialize the task service with storage dependency
    task_service = TaskService(storage_service)

    # Initialize the CLI interface with task service dependency
    cli_interface = CLIInterface(task_service)

    # Run the application
    # If command-line arguments are provided, use command-line mode
    # Otherwise, use interactive menu mode
    cli_interface.run_command_line()


if __name__ == "__main__":
    main()
