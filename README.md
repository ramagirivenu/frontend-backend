# Backend for Scalable REST API Assignment

This project implements a secure, scalable REST API with authentication, role-based access, CRUD for tasks, API versioning, error handling, validation, and Swagger documentation. Uses SQLite for simplicity.

## Features
- User registration & login (JWT, password hashing)
- Role-based access (user/admin)
- CRUD for tasks
- API versioning
- Error handling & validation
- Swagger API docs
- Scalable project structure

## Tech Stack
- Python (FastAPI)
- SQLite (via SQLAlchemy)
- JWT (PyJWT)
- Swagger (built-in with FastAPI)

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Run the server: `uvicorn main:app --reload`

## API Docs
Visit `/docs` after starting the server.

---

See the assignment README for full requirements.