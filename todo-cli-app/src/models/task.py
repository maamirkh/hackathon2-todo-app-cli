"""
Task model for the Todo In-Memory Python Console App.

This module defines the Task entity with attributes for title, description, and status,
along with validation methods as specified in the data model.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    """
    Represents a single todo item in the application.

    Attributes:
        id: System-generated unique identifier for the task within the application session
        title: The main identifier of the task; must not be empty
        description: Additional details about the task; can be empty (optional)
        status: Indicator of completion status; True for complete, False for incomplete
    """

    id: int
    title: str
    description: Optional[str] = ""
    status: bool = False

    def __post_init__(self):
        """Validate task attributes after initialization."""
        self.validate()

    def validate(self):
        """Validate task attributes according to the data model."""
        # Validate title is not empty or contains only whitespace
        if not self.title or not self.title.strip():
            raise ValueError("Task title cannot be empty or contain only whitespace")

        # Validate title length limits
        if len(self.title) > 1000:
            raise ValueError("Task title cannot exceed 1000 characters")

        # Validate description length if provided
        if self.description and len(self.description) > 2000:
            raise ValueError("Task description cannot exceed 2000 characters")

        # Validate status is boolean
        if not isinstance(self.status, bool):
            raise ValueError("Task status must be a boolean value")

    def update_title(self, new_title: str):
        """Update the task title with validation."""
        if not new_title or not new_title.strip():
            raise ValueError("Task title cannot be empty or contain only whitespace")
        if len(new_title) > 1000:
            raise ValueError("Task title cannot exceed 1000 characters")

        self.title = new_title
        self.validate()

    def update_description(self, new_description: Optional[str]):
        """Update the task description with validation."""
        if new_description and len(new_description) > 2000:
            raise ValueError("Task description cannot exceed 2000 characters")

        self.description = new_description if new_description is not None else ""
        self.validate()

    def toggle_status(self):
        """Toggle the task status between complete/incomplete."""
        self.status = not self.status
        self.validate()

    def is_complete(self) -> bool:
        """Check if the task is complete."""
        return self.status

    def is_incomplete(self) -> bool:
        """Check if the task is incomplete."""
        return not self.status