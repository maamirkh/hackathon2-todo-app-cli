# Data Model: Phase I – Todo In-Memory Python Console App

**Date**: 2025-12-27
**Feature**: Phase I – Todo In-Memory Python Console App
**Branch**: 001-todo-in-memory-app

## Overview

This document defines the data model for the Phase I Todo In-Memory Python Console App. It outlines the entities, their attributes, relationships, validation rules, and state transitions as specified in the feature requirements.

## Task Entity

### Entity Definition
The Task entity represents a single todo item in the application. It contains all the necessary attributes to track a user's task with its completion status.

### Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| id | Integer | Yes | System-generated unique identifier for the task within the application session |
| title | String | Yes | The main identifier of the task; must not be empty |
| description | String | No | Additional details about the task; can be empty |
| status | Boolean | Yes | Indicator of completion status; True for complete, False for incomplete |

### Validation Rules

1. **Title Validation**:
   - Must not be empty or contain only whitespace
   - Maximum length: 500 characters
   - Cannot exceed 1000 characters (hard limit)
   - Must contain at least one non-whitespace character

2. **Description Validation**:
   - Optional field
   - Maximum length: 2000 characters
   - Can be empty or contain only whitespace

3. **Status Validation**:
   - Must be a boolean value (True/False)
   - Default value: False (incomplete)

4. **ID Validation**:
   - Must be unique within the application session
   - Auto-generated as an incrementing integer
   - Cannot be modified by the user

### State Transitions

The Task entity has a simple state model with only one state attribute (status):

- **Incomplete (False)** → **Complete (True)**: When user marks task as complete
- **Complete (True)** → **Incomplete (False)**: When user marks task as incomplete

## In-Memory Storage Model

### Storage Structure
Tasks are stored in an in-memory dictionary where:
- Keys: Integer IDs (unique task identifiers)
- Values: Task objects with the attributes defined above

### Storage Characteristics
- **Persistence**: None (data is lost when application terminates)
- **Concurrency**: Single-user, no concurrent access
- **Capacity**: Designed to support up to 1000 tasks efficiently
- **Access Pattern**: O(1) average time complexity for CRUD operations

### Data Relationships
- **Task**: Standalone entity with no relationships to other entities in Phase I
- Each task exists independently with its own unique ID

## Data Operations

### Create Task
- Generate unique ID (increment from highest existing ID)
- Validate title (required, non-empty)
- Set default status to False (incomplete)
- Store in in-memory dictionary

### Read Task
- Retrieve task by ID from dictionary
- Return complete task object with all attributes

### Update Task
- Locate task by ID in dictionary
- Update allowed attributes (title, description, status)
- Re-validate updated attributes

### Delete Task
- Remove task by ID from dictionary
- Return confirmation of deletion

### List Tasks
- Return all tasks in the dictionary
- Can be filtered by status (all, complete, incomplete)

## Constraints and Limitations

### System Constraints
1. **Memory Limitation**: Designed to support up to 1000 tasks within reasonable memory usage
2. **Session-Based**: Data exists only during application runtime
3. **Single-User**: No user authentication or multi-user support

### Data Constraints
1. **Title Requirements**: Must be provided and non-empty
2. **ID Uniqueness**: Each task must have a unique ID within the session
3. **Status Binary**: Status can only be True (complete) or False (incomplete)

## Data Validation Summary

| Operation | Validation Performed |
|-----------|---------------------|
| Add Task | Title non-empty, length limits, ID uniqueness |
| Update Task | Title non-empty (if provided), length limits, ID existence |
| Delete Task | ID existence |
| Mark Complete/Incomplete | ID existence, status validity |
| View Tasks | None (read-only operation) |

## Future Extensibility

### Phase II Considerations
- Addition of timestamp fields (created_at, updated_at)
- Addition of user_id for multi-user support
- Addition of category/priority fields
- Migration to persistent storage (database) with schema evolution plan

### Data Migration Strategy
- In-memory structure will map to database table with same core attributes
- ID field will transition from session-unique to globally unique
- Additional metadata fields will be added in Phase II

## Implementation Notes

The data model is designed to be simple yet extensible. The in-memory storage approach in Phase I provides a foundation that can be easily migrated to persistent storage in Phase II while maintaining the same core data structure and relationships.