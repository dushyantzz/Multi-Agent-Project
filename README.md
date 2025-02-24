# 🤖 Agentic AI Project: Single and Multi-Agent Systems for Research

> 🌟 An intelligent research automation system powered by CrewAI and Google's Gemini Pro

This repository showcases two powerful approaches to AI-driven research:
- 🎯 **`single_agent.py`**: A focused, single-agent researcher
- 👥 **`multi_agent.py`**: A collaborative team of specialized AI agents

## 📚 Table of Contents

1. [🏗️ Project Structure](#project-structure)
2. [🔍 Single Agent System](#single-agent-system)
3. [👥 Multi-Agent System](#multi-agent-system)
4. [⚙️ Setup & Installation](#setup--installation)
5. [🔑 Environment Setup](#environment-setup)
6. [📝 Usage Guide](#usage-guide)

## 🏗️ Project Structure

```plaintext
Multi-Agent-Project/
├── 🤖 single_agent.py    # Single researcher agent
├── 👥 multi_agent.py     # Multi-agent research crew
├── 🔐 .env               # API keys & configuration
└── 📘 README.md          # Documentation
```

## 🔍 Single Agent System

### 🎯 Purpose
A standalone AI researcher that can:
- 📥 Accept any research topic
- 🌐 Search the internet for relevant information
- 🧠 Process and analyze findings
- 📤 Generate comprehensive summaries

### 🛠️ Tools & Technologies
- **🔌 Core Dependencies**
  - `crewai`: Agent management framework
  - `langchain_google_genai`: Gemini Pro integration
  - `SerperDevTool`: Web search capabilities

### 📊 Workflow

```mermaid
graph TD
    A[🎬 Start] --> B[🔑 Load API Keys]
    B --> C[🛠️ Initialize Tools]
    C --> D[🤖 Create Agent]
    D --> E[📋 Assign Task]
    E --> F[🔍 Research]
    F --> G[📝 Summarize]
    G --> H[📤 Output Results]
```

## 👥 Multi-Agent System

### 🎯 Purpose
A collaborative AI research team featuring:
- 🔍 **Research Specialist**: Deep-dives into topics
- ✍️ **Content Writer**: Crafts engaging narratives

### 🤝 Agent Collaboration

```mermaid
graph LR
    A[🔍 Researcher] -->|Findings| B[✍️ Writer]
    B -->|Article| C[📄 Final Output]
    style A fill:#ff9999
    style B fill:#99ff99
    style C fill:#9999ff
```

## ⚙️ Setup & Installation

1. **📥 Clone & Setup**
```bash
git clone https://github.com/yourusername/agentic-ai-project.git
cd agentic-ai-project
```

2. **🔧 Create Virtual Environment**
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
```

3. **📚 Install Dependencies**
```bash
pip install -r requirements.txt
```

## 🔑 Environment Setup

Create a `.env` file with your API keys:
```plaintext
SERPER_API_KEY=your_serper_key_here
GOOGLE_API_KEY=your_google_key_here
```

## 📝 Usage Guide

### 🤖 Single Agent Mode
```bash
python single_agent.py
```
> 💡 Enter your research topic when prompted

### 👥 Multi-Agent Mode
```bash
python multi_agent.py
```
> 🔄 Watch as the agents collaborate on research and content creation

## 🌟 Features

- 🔄 **Automated Research**: Streamlined information gathering
- 🧠 **AI-Powered Analysis**: Smart insights generation
- 📊 **Structured Output**: Clear, organized results
- 🤝 **Collaborative Agents**: Specialized task handling
- 📱 **User-Friendly**: Simple command-line interface

## 🤝 Contributing

1. 🍴 Fork the repository
2. 🌿 Create your feature branch
3. 💾 Commit your changes
4. 📤 Push to the branch
5. 🎯 Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
### 🌟 Made with AI, Powered by CrewAI and Gemini Pro 🚀