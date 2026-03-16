# AI Doctor Interaction Logger

## Project Overview

AI Doctor Interaction Logger is a backend system designed to log and manage interactions between Medical Representatives and Healthcare Professionals (HCPs).

The system allows users to record discussions with doctors, edit interactions, search previous interactions, generate summaries, and recommend follow-up actions using an AI agent workflow.

This project demonstrates the use of a modern AI-ready backend architecture with an agent-based design.

---

## Tech Stack

* Python
* FastAPI
* LangGraph (Agent Workflow Concept)
* Uvicorn (ASGI Server)
* Git & GitHub

---

## Project Structure

ai-doctor-interaction-logger

backend/

* main.py → FastAPI API routes
* agent.py → Agent logic that selects tools
* tools.py → Tools used by the agent

requirements.txt → Python dependencies
README.md → Project documentation

---

## Implemented Tools

The system provides the following tools for interaction management:

### 1. Log Interaction

Records interaction between medical representative and doctor.

### 2. Edit Interaction

Allows modification of previously recorded interaction details.

### 3. Search Interaction

Searches previous interactions with a specific doctor.

### 4. Summarize Interaction

Generates a summary of the interaction.

### 5. Follow-up Recommendation

Suggests next steps or follow-up actions after interaction.

---

## API Documentation

FastAPI automatically generates interactive API documentation.

Run the project and open:

http://127.0.0.1:8000/docs

From this interface you can test all API endpoints.

---

## How to Run the Project

### Step 1: Clone the Repository

git clone https://github.com/prachuu21/ai-doctor-interaction-logger.git

### Step 2: Navigate to the Project

cd ai-doctor-interaction-logger

### Step 3: Install Dependencies

pip install -r requirements.txt

### Step 4: Run the Server

cd backend
uvicorn main:app --reload

### Step 5: Open API Docs

http://127.0.0.1:8000/docs

---

## Architecture Overview

The system follows a simple AI-agent based workflow:

User Request → FastAPI Endpoint → Agent → Tool Execution → Response

The agent decides which tool should handle the request and executes it.

---

## Future Improvements

* Integration with LLM models
* React frontend dashboard
* Persistent database storage
* Advanced interaction analytics

---

## Author

Prachi Bambhare
BCA Student | Aspiring AI/ML Engineer
