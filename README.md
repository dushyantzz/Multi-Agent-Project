# Agentic AI Project: Single and Multi-Agent Systems for Research

## Overview

This project demonstrates the creation of AI agents using the CrewAI framework, designed to automate research tasks. It includes two main scripts: `single_agent.py` and `multi_agent.py`, each showcasing different approaches to agent deployment and task execution.

## Table of Contents

1.  [Project Structure](#project-structure)
2.  [single\_agent.py: Research Agent](#single_agentpy-research-agent)
    *   [Purpose](#purpose)
    *   [Tools Used](#tools-used)
    *   [Workflow](#workflow)
    *   [Flowchart](#flowchart)
3.  [multi\_agent.py: Collaborative Research Crew](#multi_agentpy-collaborative-research-crew)
    *   [Purpose](#purpose-1)
    *   [Agents and Roles](#agents-and-roles)
    *   [Tasks](#tasks)
    *   [Process Flow](#process-flow)
    *   [Flowchart](#flowchart-1)
4.  [Setup and Installation](#setup-and-installation)
5.  [Environment Variables](#environment-variables)
6.  [Usage](#usage)
7.  [Contributing](#contributing)
8.  [License](#license)

## Project Structure
Multi-Agent-Project/ ├── single_agent.py # Script for a single research agent ├── multi_agent.py # Script for a multi-agent research crew ├── .env # Environment variables (API keys) ├──


## single\_agent.py: Research Agent

### Purpose

The `single_agent.py` script creates a single AI agent that can research a given topic and provide a comprehensive summary. It's designed for simple research tasks where a single agent can handle the entire process from start to finish.

### Tools Used

*   **`os`**: Used for interacting with the operating system, mainly to access environment variables.
*   **`dotenv`**: Used to load environment variables from a `.env` file. This is where you store your API keys (like the Google and Serper API keys) so they're not directly in the code.
*   **`crewai`**: This is the main framework for creating and managing agents, tasks, and crews (groups of agents).
    *   `Agent`: Represents an individual agent with a specific role, goal, and set of tools.
    *   `Task`: Represents a specific task that an agent needs to perform.
    *   `Crew`: Represents a group of agents working together to complete a set of tasks.
*   **`crewai_tools`**: Provides tools that can be used by CrewAI agents. In this case, it provides `SerperDevTool`.
    *   `SerperDevTool`: A tool that allows the agent to perform searches on the internet using the Serper API.
*   **`langchain_google_genai`**: Used to integrate with Google's Gemini Pro language model.
    *   `ChatGoogleGenerativeAI`: A class that allows you to use the Gemini Pro model for generating text.
*   **`langchain.tools`**: Provides a way to define tools that the agent can use.
    *   `Tool`: A class that represents a tool that the agent can use. It takes a name, a function to execute, and a description of what the tool does.

### Workflow

1.  **Setup**:
    *   It loads API keys from a `.env` file.
    *   It initializes the `SerperDevTool` with the Serper API key.
2.  **Create Research Agent**:
    *   It creates an agent with the role of "Research Specialist".
    *   It gives the agent a goal, a backstory, and a search tool.
    *   It uses the Gemini Pro model as the agent's language model (the "brain" of the agent).
3.  **Create Research Task**:
    *   It creates a task that tells the agent to research a specific topic and provide a summary.
4.  **Run Research**:
    *   It creates a crew with the research agent and the research task.
    *   It tells the crew to start working on the task.
    *   The agent uses the search tool to find information on the topic.
    *   The agent uses the Gemini Pro model to summarize the information.
5.  **Output**:
    *   The script prints the research result (the summary) to the console.

### Flowchart

```mermaid
graph LR
    A[Start] --> B{Load API Keys};
    B --> C{Initialize SerperDevTool};
    C --> D{Create Research Agent};
    D --> E{Create Research Task};
    E --> F{Create Crew};
    F --> G{Kickoff Crew};
    G --> H{Agent Researches Topic};
    H --> I{Agent Summarizes Information};
    I --> J[Print Research Result];
    J --> K[End];