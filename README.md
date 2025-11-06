
# SAVI_CHATbot

## Overview

SAVI_CHATbot is a simple chatbot web app. It provides an user-interface to interact with the chatbot which answers queries relevant to USR(Universal Semantic Representation).

---

## Features

- Web UI (frontend) to chat with the bot  
- Backend logic in Python (`app.py`, `data.py`)  
- Environment configuration via `.env` file  
- Handles user messages and returns responses via backend  

---

## Installation

### 1. Clone the repository

```bash
  git clone https://github.com/dwsds/SAVI_CHATbot.git
  cd SAVI_CHATbot
```

### 2. Install dependencies

```bash
  pip install -r requirements.txt
```

### 3. Configuration

Copy the example environment file:
```bash
  cp .env.example .env
```

Then open `.env` and set the required GEMINI_API_KEY.

### 4. Run the application

```bash
  python app.py
```

Once the app is running, open your web browser and visit:

```bash
  http://localhost:3000
```
