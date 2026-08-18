# 🧠 AI Startup & Idea Stress Tester

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![CrewAI](https://img.shields.io/badge/Orchestration-CrewAI-red.svg)](https://crewai.com)
[![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B.svg)](https://streamlit.io)
[![Gemini API](https://img.shields.io/badge/LLM-Google%20Gemini-orange.svg)](https://ai.google.dev/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)

An autonomous multi-agent AI system that aggressively stress-tests startup and business ideas before launch. By simulating a virtual boardroom debate, three specialized agents evaluate market viability, red-team operational and financial vulnerabilities, and deliver an **Executive Decision Memorandum** with an objective viability score.

---

## 🤖 Multi-Agent Architecture

The system uses **CrewAI** to execute a sequential pipeline where downstream agents inherit full context from upstream debates:

            ┌──────────────────────────────┐
              │    User Idea (Streamlit/CLI) │
              └──────────────┬───────────────┘
                             │
                             ▼
     ┌─────────────────────────────────────────────────┐
     │ 1. Visionary Strategist (Optimist Agent)         │
     │    • Market upside, moat & value propositions   │
     └───────────────────────┬─────────────────────────┘
                             │ (Context Passed)
                             ▼
     ┌─────────────────────────────────────────────────┐
     │ 2. Ruthless Skeptic (Critic Agent)              │
     │    • Unit economics traps, occlusion & churn    │
     └───────────────────────┬─────────────────────────┘
                             │ (Full Context Passed)
                             ▼
     ┌─────────────────────────────────────────────────┐
     │ 3. Executive Arbiter (Decision Strategist)      │
     │    • Pre-launch fixes checklist & strategic horizon│
     │    • Objective Viability Score Calculation      │
     └───────────────────────┬─────────────────────────┘
                             │
                             ▼
              ┌──────────────────────────────┐
              │ Executive Decision Memorandum│
              └──────────────────────────────┘
| Agent Persona | Role & Primary Focus |
| :--- | :--- |
| **Visionary Product Strategist** | Identifies expansion potential, product-market fit, and high-leverage growth engines. |
| **Ruthless Red-Team Skeptic** | Attacks logistics friction, micro-fulfillment unit economics, and liability points. |
| **Executive Arbiter** | Synthesizes opposing viewpoints, issues an objective score, and defines mandatory pre-launch pivots. |

---

## 🛠️ Tech Stack

* **Multi-Agent Orchestration:** [CrewAI](https://crewai.com) (Sequential Pipeline)
* **LLM Engine:** Google Gemini Flash (`gemini-1.5-flash` / `gemini-2.0-flash` via `google-genai`)
* **User Interface:** [Streamlit](https://streamlit.io)
* **Environment & Package Manager:** [`uv`](https://github.com/astral-sh/uv)

---

## 📂 Project Structure

```text
idea_stress_tester/
├── app.py                     # Streamlit web interface entry point
├── pyproject.toml             # Dependencies and project metadata
├── uv.lock                    # Locked dependency tree
├── .env.example               # Environment template
│
└── src/
    └── idea_stress_tester/
        ├── crew.py            # Crew, Agent, and Task orchestration
        ├── main.py            # CLI entry point (`crewai run`)
        └── config/
            ├── agents.yaml    # Agent personas and backstories
            └── tasks.yaml     # Task descriptions and expected outputs
🚀 Quickstart & Setup
1. Clone the Repository
Bash
git clone [https://github.com/binarylaiba/Idea-Stress-Tester.git](https://github.com/binarylaiba/Idea-Stress-Tester.git)
cd Idea-Stress-Tester/idea_stress_tester
2. Configure Environment Variables
Create a .env file in the root folder[cite: 1]:

Code snippet
GEMINI_API_KEY="your-gemini-api-key-here"
3. Run Locally with uv
To launch the Streamlit Web UI:

[cite: 1]

Bash
uv sync
uv run streamlit run app.py
To run via CLI directly:

[cite: 1]

Bash
uv run crewai run
📄 Output Artifact
Every assessment produces a structured Executive Decision Memorandum covering[cite: 1]:

Executive Viability Score (Rated out of 100)[cite: 1]

Core Moat & Growth Levers

[cite: 1]

Fatal Operational & Unit Economics Traps

[cite: 1]

Top 3 Actionable Fixes & Pre-Launch Checklist

[cite: 1]

Phase-by-Phase Strategic Horizon Plan

[cite: 1]
              
              
              
              
              
              
              
              
              │ Executive Decision Memorandum│
              └──────────────────────────────┘
