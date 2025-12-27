# API Contracts: Phase I – Todo In-Memory Python Console App

**Date**: 2025-12-27
**Feature**: Phase I – Todo In-Memory Python Console App
**Branch**: 001-todo-in-memory-app

## Overview

This document defines the API contracts for the Phase I Todo In-Memory Python Console App. These contracts establish the interface specifications that will be used in future phases when extending the application with web interfaces and external integrations.

## CLI Interface Contracts

### Command-Line Arguments

#### Add Task Command
- **Command**: `python todo.py add <title> [description]`
- **Parameters**:
  - `title` (string, required): The task title (1-500 characters)
  - `description` (string, optional): Task description (0-2000 characters)
- **Success Response**: Task object with ID and creation confirmation
- **Error Responses**:
  - 400: Title is empty or exceeds length limits
  - 507: Storage limit reached (1000 tasks)

#### List Tasks Command
- **Command**: `python todo.py list [--status=<status>]`
- **Parameters**:
  - `--status` (string, optional): Filter by status (all, complete, incomplete)
- **Success Response**: Array of task objects
- **Error Responses**: None (returns empty array if no tasks)

#### Update Task Command
- **Command**: `python todo.py update <id> [title] [description]`
- **Parameters**:
  - `id` (integer, required): Task identifier
  - `title` (string, optional): New task title
  - `description` (string, optional): New task description
- **Success Response**: Updated task object
- **Error Responses**:
  - 404: Task ID not found
  - 400: Title is empty or exceeds length limits

#### Complete Task Command
- **Command**: `python todo.py complete <id>`
- **Parameters**:
  - `id` (integer, required): Task identifier
- **Success Response**: Updated task object with status=True
- **Error Responses**:
  - 404: Task ID not found

#### Delete Task Command
- **Command**: `python todo.py delete <id>`
- **Parameters**:
  - `id` (integer, required): Task identifier
- **Success Response**: Deletion confirmation
- **Error Responses**:
  - 404: Task ID not found

## Internal Service Contracts

### Task Service Interface

#### create_task(title: str, description: str = "") -> dict
- **Purpose**: Create a new task with the given parameters
- **Input**:
  - title (str, 1-500 chars, required)
  - description (str, 0-2000 chars, optional)
- **Output**: Task object with id, title, description, and status
- **Side Effects**: Adds task to in-memory storage

#### get_task(task_id: int) -> dict | None
- **Purpose**: Retrieve a specific task by ID
- **Input**: task_id (int, required)
- **Output**: Task object or None if not found
- **Side Effects**: None

#### update_task(task_id: int, title: str = None, description: str = None, status: bool = None) -> dict | None
- **Purpose**: Update an existing task's properties
- **Input**:
  - task_id (int, required)
  - title (str, optional)
  - description (str, optional)
  - status (bool, optional)
- **Output**: Updated task object or None if not found
- **Side Effects**: Modifies existing task in storage

#### delete_task(task_id: int) -> bool
- **Purpose**: Remove a task from storage
- **Input**: task_id (int, required)
- **Output**: True if successful, False if task not found
- **Side Effects**: Removes task from in-memory storage

#### list_tasks(status_filter: str = "all") -> list
- **Purpose**: Retrieve all tasks, optionally filtered by status
- **Input**: status_filter (str: "all", "complete", "incomplete"; default: "all")
- **Output**: Array of task objects
- **Side Effects**: None

#### toggle_task_status(task_id: int) -> dict | None
- **Purpose**: Toggle a task's completion status
- **Input**: task_id (int, required)
- **Output**: Updated task object or None if not found
- **Side Effects**: Updates status of existing task

## Data Contracts

### Task Object Structure
```json
{
  "id": 1,
  "title": "string (1-500 characters)",
  "description": "string (0-2000 characters)",
  "status": "boolean (true for complete, false for incomplete)"
}
```

### Error Response Structure
```json
{
  "error": "error message string",
  "code": "error code",
  "timestamp": "ISO 8601 timestamp"
}
```

## Validation Rules

### Input Validation
- Title: Required, 1-500 characters, no leading/trailing whitespace
- Description: Optional, 0-2000 characters
- Status: Boolean value only
- ID: Positive integer, must exist in storage

### Business Rules
- Task titles cannot be empty or contain only whitespace
- Task IDs must be unique within the session
- Status can only be True (complete) or False (incomplete)
- Maximum of 1000 tasks allowed in memory

## Future Phase Considerations

These contracts are designed to support future phases:
- Phase II: Web API endpoints will use similar data structures
- Phase III: Chatbot interfaces will use these task representations
- Phase IV: Service-to-service communication will follow these patterns
- Phase V: Distributed system interfaces will build on these foundations