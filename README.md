🔐 Ephemeral 2.0

A lightweight, real-time chat web application built with FastAPI and WebSockets.

Ephemeral 2.0 is focused on creating a simple private chat experience with room-based access, real-time messaging, and a foundation for future end-to-end encryption.

«🚧 Work in Progress — This project is actively being developed.»

---

✨ Features

- 🔑 Login / access-code based entry
- 💬 Real-time messaging
- ⚡ WebSocket communication
- 🚪 Private chat rooms
- 🌐 Browser-based interface
- 🐍 FastAPI backend
- 🔐 Encryption planned
- 🧹 Ephemeral-message architecture planned

---

🛠️ Tech Stack

Backend

- Python
- FastAPI
- WebSockets
- Uvicorn

Frontend

- HTML
- CSS
- JavaScript

Development

- Git
- GitHub
- Linux / Pop!_OS

---

📁 Project Structure

ephemeral2.0/
│
├── main.py
├── README.md
├── requirements.txt
│
├── static/
│   ├── style.css
│   └── script.js
│
└── templates/
    └── index.html

The exact structure may change as the project develops.

---

🚀 Getting Started

1. Clone the repository

git clone <your-repository-url>
cd ephemeral2.0

2. Create a virtual environment

python3 -m venv venv

Activate it:

source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Start the server

uvicorn main:app --reload

The application will normally be available at:

http://127.0.0.1:8000

---

🔌 WebSocket Architecture

Ephemeral 2.0 uses WebSockets for real-time communication.

Instead of repeatedly asking the server for new messages:

Client ── request ──> Server
Client <── response ── Server

the client maintains a persistent connection:

Client
   │
   │ WebSocket
   ▼
FastAPI Server
   │
   ▼
Chat Room

This allows messages to be delivered immediately.

---

🔐 Security

The project is being developed with privacy and security in mind.

Current/planned security layers include:

- Access-code protected chat
- Private chat rooms
- Server-side validation
- WebSocket authentication
- Secure session handling
- End-to-end encryption
- Minimal message persistence
- Ephemeral message deletion

Important

The current development version should not be considered fully secure or production-ready.

Encryption and authentication are being developed incrementally.

---

🗺️ Roadmap

Phase 1 — Basic Chat

- [x] FastAPI server
- [x] Basic HTML client
- [x] WebSocket connection
- [x] Send messages
- [x] Receive messages
- [x] Real-time communication

Phase 2 — Private Access

- [x] Login
- [x] Access code
- [ ] Proper session management
- [ ] Protected WebSocket connections
- [ ] Private chat rooms

Phase 3 — Secure Messaging

- [ ] Message encryption
- [ ] Key generation
- [ ] Key exchange
- [ ] End-to-end encryption
- [ ] Secure authentication

Phase 4 — Ephemeral System

- [ ] Temporary chat rooms
- [ ] Automatic message deletion
- [ ] Room expiration
- [ ] User disconnect cleanup
- [ ] No permanent message storage

Phase 5 — Deployment

- [ ] Production configuration
- [ ] HTTPS
- [ ] Secure WebSocket ("wss://")
- [ ] Domain
- [ ] Cloud deployment
- [ ] Production database/session storage

---

🧠 Project Goal

The goal of Ephemeral 2.0 is to learn how modern real-time web applications work while building a privacy-focused messaging system from the ground up.

The project explores:

HTTP
 │
 ▼
FastAPI
 │
 ▼
WebSockets
 │
 ▼
Authentication
 │
 ▼
Private Rooms
 │
 ▼
Encryption
 │
 ▼
Ephemeral Messaging

---

⚠️ Development Status

Ephemeral 2.0 is an experimental learning project.

Do not use the current development version for sensitive or confidential communication.

---

📜 License

License to be decided.
