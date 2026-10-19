# NOVA AI — Personal Student Assistant

A beginner-friendly Python + Streamlit project with a polished dashboard, a rule-based chat assistant, study-plan generator, task tracker, and calculator.

## Features
- Chat assistant for Python, AI/ML, study planning, resumes, interviews, and projects
- Mini study-plan generator
- Interactive task tracker
- Quick calculator
- Responsive dashboard UI

## Run locally
1. Install Python 3.10 or newer.
2. Open a terminal in this folder.
3. Install the dependency:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the app:
   ```bash
   streamlit run app.py
   ```
5. Open the local URL shown in the terminal.

## Important note
This starter version uses predefined responses. It does **not** connect to a live AI model or send user data to an AI service. A future version can connect to a real model API after adding secure key handling.

## Suggested future upgrades
- Add a live AI model through a secure API key stored in environment variables or Streamlit secrets
- Add speech-to-text and text-to-speech
- Save tasks between sessions
- Add quiz mode and progress charts
- Deploy the demo with Streamlit Community Cloud

## GitHub description
NOVA AI is a student-focused Python web app featuring an AI-inspired chatbot, study planner, task tracker, and calculator, built with Streamlit.
