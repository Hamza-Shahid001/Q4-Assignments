# 🛠 **Multi-API AI Agent Framework**

## 1. Overview
This project provides a flexible and extensible framework for developing AI agents leveraging both OpenAI SDK Agent and Google Gemini API. It offers different levels of abstraction (Agent, Runner, Global) to suit various development needs, from fine-grained control over agent behavior to high-level, streamlined execution.

Whether you're building intelligent chatbots, sophisticated automation tools, or advanced decision-making systems, this framework provides the foundation to integrate powerful large language models (LLMs) from leading providers.

Fantastic! Building AI agents with both OpenAI and Google Gemini APIs at different levels of abstraction (Agent, Runner, Global) is a powerful setup. Here's a comprehensive README.md file tailored for your project.


## 2. Features
#### **Multi-API Support:** 
Seamlessly integrate with OpenAI and Google Gemini models.

#### **Layered Abstraction:**

**Agent Level:** Define and configure individual AI agents with specific instructions, tools, and model preferences.

**Runner Level:** Control agent execution with run, run_sync, and run_streamed methods for synchronous, asynchronous, and streaming interactions.

**Global Level:** Manage overall API configurations, default models, and shared resources across all agents and runners.

**Configurable Models:** Easily switch between different OpenAI (e.g., GPT-4o, GPT-3.5-turbo) and Google Gemini (e.g., Gemini 1.5 Pro, Gemini 1.5 Flash) models.

**Scalable Design:** Built to support growing complexity and multiple concurrent agent interactions.

**Extensible:** Designed to be easily extended with new tools, custom agent behaviors, and additional LLM providers.

Fantastic! Building AI agents with both OpenAI and Google Gemini APIs at different levels of abstraction (Agent, Runner, Global) is a powerful setup. Here's a comprehensive README.md file tailored for your project.

## 3. Architecture
The framework is structured to promote modularity and reusability:

Global Configuration: Manages universal settings like API keys and default models.

Agent Class: Encapsulates the core logic for an individual AI agent, including its instructions, tools, and the specific model it uses.

Runner Class: Provides the execution interface for agents, handling the interaction loop with the LLM and managing different execution modes (sync, async, streaming).

[ Your Application ]
      |
      V
+---------------------+
| Global Configuration| <--- API Keys (OpenAI, Gemini)
+---------------------+
      |
      V
+---------------------+     +------------------+
|    Runner Level     | --> |   Agent Level    |
| (run, run_sync,     |     | (Instructions,   |
|  run_streamed)      |     |  Tools, Model)   |
+---------------------+     +------------------+
      |                           |
      V                           V
+-------------------+       +-------------------+
|   OpenAI SDK Agent| <---> | Google Gemini API |
+-------------------+       +-------------------+

## 4. Getting Started
Follow these steps to get your project up and running.

**Prerequisites**
Before you begin, ensure you have the following installed:

* Python 3.8+
* uv (python package installer)

**Initialization**

Create projects using uv package manager
uv init [project name]

Install following libraries using uv package manager:
* uv add python-dotenv
* uv add openai-agents

**API Key Setup**
This project requires API keys for OpenAI or Google Gemini. Never hardcode your API keys directly in your code. We recommend using environment variables.

Create a .env file in the root directory of your project:

API_KEY="your_openai_api_or_gemini_api_key_here"
