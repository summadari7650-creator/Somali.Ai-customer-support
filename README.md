# Somali.AI - Automated Customer Support System

An automated AI-driven customer support pipeline that retrieves pending customer inquiries, processes them using Google Gemini API to generate appropriate Somali responses, and updates an SQLite database log.

# Features
- Database Integration: Connects to SQLite (Somali.AI) to pull unresolved issues and record generated support responses.
- AI Processing: Leverages Google Gemini API to produce context-aware responses in Somali.
- Reliable Pipeline: Includes error handling and dynamic database updates for seamless execution.

# Tech Stack
- Language: Python 3.x
- Database: SQLite3
- AI Model: Google GenAI SDK (gemini-3.6-flash)

# How to Run
1. Clone the repository.
2. Set your Gemini API key: API_KEY = "YOUR_GEMINI_API_KEY"
3. Run the script: python run_app.py
