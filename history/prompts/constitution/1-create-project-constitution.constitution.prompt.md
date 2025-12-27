---
id: 1
title: Create-project-constitution
stage: constitution
date: 2025-12-27
surface: agent
model: Claude Sonnet 4.5
feature: none
branch: master
user: user
command: /sp.constitution
labels: [constitution,spec-driven-development,ai-engineering]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
---

## Prompt

```text
You are an expert Software Product Architect and Spec-Driven Development Mentor.

Your task is to generate a highly structured, professional constitution.md document for the project:

Evolution of Todo App using SpecKit Plus

This constitution must define the global rules, constraints, governance model, and development principles of the entire project. It must not contain detailed feature specifications or implementation tasks. It should only define project-level laws and discipline.

Important Constraint:
At this stage, no coding and no installation will be performed. Only the constitution.md file will be created.

Overall Objective
The constitution should formally define how this project will be built from Phase I to Phase V using Spec-Driven Development, Claude Code, and AI-first engineering practices.

The constitution must include the following sections:

1. Project Vision and Philosophy
2. Scope Boundaries (what is allowed and what is not allowed)
3. Spec-Driven Development Rules
4. AI Usage Policy
5. Coding Restrictions and Prohibited Practices
6. Versioning and Change Control Policy
7. Collaboration and Review Rules
8. Documentation Standards
9. Testing and Validation Principles
10. Security and Ethics Guidelines
11. Failure Handling and Recovery Policy
12. Acceptance Criteria for Each Phase
13. Non-Functional Requirements Governance
14. Compliance with Hackathon Rules
15. Future Evolution and Extensibility Guidelines

Global Development Constraints (must be clearly stated)

- No manual coding is allowed
- All implementation must be generated using Claude Code or AI coding agents
- Specification must be iteratively refined until correct implementation is generated
- Constitution applies to all five phases:
  - Phase I – In-Memory Python Console App
  - Phase II – Full-Stack Web Application
  - Phase III – AI-Powered Todo Chatbot
  - Phase IV – Local Kubernetes Deployment
  - Phase V – Cloud-Native Distributed System

Reusable Intelligence and Agent Architecture Guidelines

- Use reusable intelligence in the form of agent skills wherever possible
- Agent skills should encapsulate common logic so it can be reused across phases
- Sub-agents may be created for specialized responsibilities
- Both agent skills and sub-agents may be used together to simplify workflow execution
- A primary orchestrator agent may coordinate sub-agents and skills to execute end-to-end flows

Technology Stack References to be mentioned in constitution

- SpecKit Plus
- Claude Code or AI Coding Agent
- OpenAI ChatKit
- OpenAI Agents SDK with compatible Gemini API key
- Official MCP SDK
- Docker, Minikube, Helm, Kubernetes
- DigitalOcean Kubernetes Service (DOKS)

Mandatory Rules to Declare

- No feature implementation will be started without an approved specification
- Constitution overrides any developer decision
- Every feature must include:
  - Constitution compliance verification
  - Specification document
  - AI-generated implementation
- Natural language todo management and Urdu language support will be considered in later phases

Output Requirements

- The final document must be in clean Markdown format
- Tone must be formal and professional
- Use structured headings and bullet points
- Do not include emojis
- Avoid casual language

Now generate the complete constitution.md document.
```

## Response snapshot

Created the complete constitution.md document for the Todo App evolution project with all required sections including Core Principles, Scope Boundaries, Spec-Driven Development Rules, AI Usage Policy, Coding Restrictions, Versioning Policy, Collaboration Rules, Documentation Standards, Testing Principles, Security Guidelines, Failure Handling, Acceptance Criteria for each phase, Non-Functional Requirements, Hackathon Compliance, and Future Evolution Guidelines.

## Outcome

- ✅ Impact: Created comprehensive project constitution that defines global rules, constraints, governance model, and development principles for the Todo App evolution project across all five phases
- 🧪 Tests: N/A (documentation task)
- 📁 Files: Created .specify/memory/constitution.md with 257 lines containing all required sections
- 🔁 Next prompts: Implementation can now proceed according to the established constitution
- 🧠 Reflection: The constitution establishes a solid foundation for AI-first engineering with Spec-Driven Development principles

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A