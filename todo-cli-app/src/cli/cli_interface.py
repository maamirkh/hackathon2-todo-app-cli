"""
CLI interface for the Todo In-Memory Python Console App.

This module implements the menu-driven interface and command-line argument parsing
as specified in the functional requirements for user interaction.
"""

import argparse
from typing import Optional
from src.services.task_service import TaskService
from src.models.task import Task


class CLIInterface:
    """
    Provides a command-line interface for users to interact with the task management system.

    Implements FR-006: System MUST provide a menu-based interface for users to select operations
    and FR-007: System MUST accept command-line arguments for direct task operations.
    """

    def __init__(self, task_service: TaskService):
        """
        Initialize the CLI interface with a task service dependency.

        Args:
            task_service: The task service to use for business operations
        """
        self.task_service = task_service
        self.parser = self._create_parser()

    def _create_parser(self) -> argparse.ArgumentParser:
        """Create and configure the argument parser for command-line operations."""
        parser = argparse.ArgumentParser(
            description="Todo In-Memory Python Console App",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
Examples:
  %(prog)s add "Buy groceries" "Milk, bread, eggs"
  %(prog)s list
  %(prog)s complete 1
  %(prog)s delete 1
  %(prog)s
            """
        )

        subparsers = parser.add_subparsers(dest='command', help='Available commands')

        # Add command
        add_parser = subparsers.add_parser('add', help='Add a new task')
        add_parser.add_argument('title', help='Task title')
        add_parser.add_argument('description', nargs='?', default='', help='Task description (optional)')

        # List command
        list_parser = subparsers.add_parser('list', help='List all tasks')
        list_parser.add_argument('--status', choices=['all', 'complete', 'incomplete'],
                                default='all', help='Filter tasks by status (default: all)')

        # Complete command
        complete_parser = subparsers.add_parser('complete', help='Mark a task as complete')
        complete_parser.add_argument('id', type=int, help='Task ID')

        # Incomplete command
        incomplete_parser = subparsers.add_parser('incomplete', help='Mark a task as incomplete')
        incomplete_parser.add_argument('id', type=int, help='Task ID')

        # Delete command
        delete_parser = subparsers.add_parser('delete', help='Delete a task')
        delete_parser.add_argument('id', type=int, help='Task ID')

        # Update command
        update_parser = subparsers.add_parser('update', help='Update a task')
        update_parser.add_argument('id', type=int, help='Task ID')
        update_parser.add_argument('--title', help='New task title')
        update_parser.add_argument('--description', help='New task description')

        return parser

    def run_command_line(self, args=None):
        """Run the application in command-line mode with provided arguments."""
        parsed_args = self.parser.parse_args(args)

        if parsed_args.command == 'add':
            self._handle_add(parsed_args.title, parsed_args.description)
        elif parsed_args.command == 'list':
            self._handle_list(parsed_args.status)
        elif parsed_args.command == 'complete':
            self._handle_complete(parsed_args.id)
        elif parsed_args.command == 'incomplete':
            self._handle_incomplete(parsed_args.id)
        elif parsed_args.command == 'delete':
            self._handle_delete(parsed_args.id)
        elif parsed_args.command == 'update':
            self._handle_update(parsed_args.id, parsed_args.title, parsed_args.description)
        else:
            # No command provided, show interactive menu
            self.run_interactive()

    def run_interactive(self):
        """Run the application in interactive menu mode."""
        print("Welcome to the Todo In-Memory Python Console App!")
        print("Type 'help' for available commands or 'exit' to quit.\n")

        while True:
            try:
                # Display menu options
                self._display_menu()

                # Get user input
                choice = input("\nEnter your choice: ").strip().lower()

                if choice in ['7', 'exit', 'quit', 'q']:
                    print("Thank you for using the Todo App. Goodbye!")
                    break
                elif choice in ['1', 'add', 'a']:
                    self._handle_interactive_add()
                elif choice in ['2', 'view', 'list', 'v']:
                    self._handle_interactive_view()
                elif choice in ['3', 'update', 'u']:
                    self._handle_interactive_update()
                elif choice in ['4', 'delete', 'd']:
                    self._handle_interactive_delete()
                elif choice in ['5', 'complete', 'mark', 'c']:
                    self._handle_interactive_mark()
                elif choice in ['6', 'help', 'h']:
                    self._display_help()
                else:
                    print("Invalid choice. Please enter a number between 1-7 or a command name.")
            except KeyboardInterrupt:
                print("\n\nThank you for using the Todo App. Goodbye!")
                break
            except Exception as e:
                print(f"An error occurred: {e}")

    def _display_menu(self):
        """Display the main menu options."""
        print("\n" + "="*50)
        print("TODO APP - MAIN MENU")
        print("="*50)
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Complete/Incomplete")
        print("6. Help")
        print("7. Exit")
        print("="*50)

    def _display_help(self):
        """Display help information for the application."""
        print("\n" + "="*50)
        print("HELP - Todo App Commands")
        print("="*50)
        print("1. Add Task: Create a new task with title and optional description")
        print("2. View Tasks: Display all tasks with status indicators")
        print("3. Update Task: Modify an existing task's title or description")
        print("4. Delete Task: Remove a task from the list")
        print("5. Mark Complete/Incomplete: Change a task's completion status")
        print("6. Help: Display this help information")
        print("7. Exit: Quit the application")
        print("\nCommand-line usage:")
        print("  python main.py add \"Task Title\" \"Optional Description\"")
        print("  python main.py list [--status all|complete|incomplete]")
        print("  python main.py complete <task_id>")
        print("  python main.py incomplete <task_id>")
        print("  python main.py delete <task_id>")
        print("  python main.py update <task_id> [--title \"New Title\"] [--description \"New Description\"]")
        print("\nNote: This is an in-memory application, so data is not persistent")
        print("between separate command executions. Use the interactive mode")
        print("(run 'python main.py' without arguments) to maintain state during")
        print("a single session.")
        print("="*50)

    def _handle_add(self, title: str, description: str = ""):
        """Handle adding a task via command line."""
        try:
            task = self.task_service.add_task(title, description)
            print(f"Task added successfully with ID: {task.id}")
        except ValueError as e:
            print(f"Error: {e}")

    def _handle_list(self, status_filter: str):
        """Handle listing tasks via command line."""
        if status_filter == 'complete':
            tasks = self.task_service.get_completed_tasks()
        elif status_filter == 'incomplete':
            tasks = self.task_service.get_incomplete_tasks()
        else:
            tasks = self.task_service.get_all_tasks()

        if not tasks:
            print("No tasks found.")
        else:
            self._display_tasks(tasks)

    def _handle_complete(self, task_id: int):
        """Handle marking a task as complete via command line."""
        task = self.task_service.mark_task_complete(task_id)
        if task:
            print(f"Task {task_id} marked as complete")
        else:
            print(f"Task with ID {task_id} not found")

    def _handle_incomplete(self, task_id: int):
        """Handle marking a task as incomplete via command line."""
        task = self.task_service.mark_task_incomplete(task_id)
        if task:
            print(f"Task {task_id} marked as incomplete")
        else:
            print(f"Task with ID {task_id} not found")

    def _handle_delete(self, task_id: int):
        """Handle deleting a task via command line."""
        success = self.task_service.delete_task(task_id)
        if success:
            print(f"Task {task_id} deleted successfully")
        else:
            print(f"Task with ID {task_id} not found")

    def _handle_update(self, task_id: int, title: Optional[str], description: Optional[str]):
        """Handle updating a task via command line."""
        task = self.task_service.update_task(task_id, title, description)
        if task:
            print(f"Task {task_id} updated successfully")
        else:
            print(f"Task with ID {task_id} not found")

    def _handle_interactive_add(self):
        """Handle adding a task in interactive mode."""
        try:
            title = input("Enter task title: ").strip()
            if not title:
                print("Task title cannot be empty.")
                return

            description = input("Enter task description (optional): ").strip()

            task = self.task_service.add_task(title, description)
            print(f"Task added successfully with ID: {task.id}")
        except ValueError as e:
            print(f"Error: {e}")

    def _handle_interactive_view(self):
        """Handle viewing tasks in interactive mode."""
        tasks = self.task_service.get_all_tasks()

        if not tasks:
            print("No tasks found.")
            return

        print(f"\nTotal tasks: {len(tasks)}")
        self._display_tasks(tasks)

    def _handle_interactive_update(self):
        """Handle updating a task in interactive mode."""
        try:
            task_id = int(input("Enter task ID to update: "))
        except ValueError:
            print("Invalid task ID. Please enter a number.")
            return

        # Check if task exists
        existing_task = self.task_service.get_task_by_id(task_id)
        if not existing_task:
            print(f"Task with ID {task_id} not found")
            return

        print(f"Current task: {existing_task.title}")
        if existing_task.description:
            print(f"Current description: {existing_task.description}")
        print(f"Current status: {'Complete' if existing_task.status else 'Incomplete'}")

        new_title = input(f"Enter new title (or press Enter to keep '{existing_task.title}'): ").strip()
        new_title = new_title if new_title else None

        new_description = input(f"Enter new description (or press Enter to keep current): ").strip()
        new_description = new_description if new_description else None

        try:
            task = self.task_service.update_task(task_id, new_title, new_description)
            if task:
                print(f"Task {task_id} updated successfully")
            else:
                print(f"Failed to update task {task_id}")
        except ValueError as e:
            print(f"Error: {e}")

    def _handle_interactive_delete(self):
        """Handle deleting a task in interactive mode."""
        try:
            task_id = int(input("Enter task ID to delete: "))
        except ValueError:
            print("Invalid task ID. Please enter a number.")
            return

        success = self.task_service.delete_task(task_id)
        if success:
            print(f"Task {task_id} deleted successfully")
        else:
            print(f"Task with ID {task_id} not found")

    def _handle_interactive_mark(self):
        """Handle marking a task as complete/incomplete in interactive mode."""
        try:
            task_id = int(input("Enter task ID to mark: "))
        except ValueError:
            print("Invalid task ID. Please enter a number.")
            return

        # Check if task exists
        task = self.task_service.get_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found")
            return

        print(f"Current status for task '{task.title}': {'Complete' if task.status else 'Incomplete'}")

        new_status = not task.status
        action = "complete" if new_status else "incomplete"

        confirm = input(f"Mark task as {action}? (y/N): ").strip().lower()
        if confirm in ['y', 'yes']:
            if new_status:
                updated_task = self.task_service.mark_task_complete(task_id)
            else:
                updated_task = self.task_service.mark_task_incomplete(task_id)

            if updated_task:
                print(f"Task {task_id} marked as {'complete' if updated_task.status else 'incomplete'}")
            else:
                print(f"Failed to update task {task_id}")
        else:
            print("Operation cancelled.")

    def _display_tasks(self, tasks: list):
        """Display tasks in a formatted table."""
        if not tasks:
            print("No tasks to display.")
            return

        # Print header
        print(f"\n{'ID':<4} | {'Title':<20} | {'Status':<12} | {'Description'}")
        print("-" * 60)

        # Print each task
        for task in tasks:
            status = "Complete" if task.status else "Incomplete"
            title = task.title[:17] + "..." if len(task.title) > 20 else task.title
            description = task.description[:30] + "..." if len(task.description) > 30 else task.description
            print(f"{task.id:<4} | {title:<20} | {status:<12} | {description}")