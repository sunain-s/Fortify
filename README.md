# Fortify
Online Password Management System

A secure password management and generation tool built with FastAPI, React (TypeScript), and SQLite.

Overview

Fortify is a lightweight password manager designed to help users securely generate, store, and manage their passwords in one place. The project utilizes a modern React + TypeScript frontend and a FastAPI backend with SQLite as its database. User passwords are stored securely with hashing and encryption measures in place.

Features

1. User Registration and Authentication
Create an account, log in, and get authenticated with JWT-based token cookies.
2. Secure Password Storage
Store website credentials (site name, password) in your personal vault.
3. Password Generationß
Generate random passwords of specified length using a secure library.
4. Password Strength Meter
Receive feedback on password complexity when signing up.
5. Profile Management
View and update your account info (username, password). Optionally delete your account.

Requirements
- Python 3.9+
- Node.js 16+ and npm
- (Optional) SQLite CLI or DB Browser tool for debugging the database locally

Project Structure
.
├── backend
│   ├── auth
│   ├── databases
│   ├── password
│   ├── user
│   ├── main.py
│   ...
├── frontend
│   ├── public
│   ├── src
│   ├── index.html
│   └── ...
├── README.md
└── ...

Getting Started

Backend Setup
1. Navigate to the backend folder:
cd backend
2. Create and activate a virtual environment (example for macOS/Linux):
python3 -m venv venv
source venv/bin/activate
3. Install the required packages:
pip install fastapi uvicorn sqlalchemy passlib python-jose pydantic
4. Ensure you have a file named main.py that starts the FastAPI app:
uvicorn main:app --reload

This should start the server at http://127.0.0.1:8000.

Database Initialization
In a Python shell or script, create the SQLite tables:

from databases.database import engine
from databases.models import Base

Base.metadata.create_all(bind=engine)

This ensures users and passwords tables exist.

Frontend Setup
1. Open a separate terminal window.
2. Navigate to the frontend folder:
cd ../frontend
3. Install dependencies:
npm install
4. Start the development server:
npm run dev
5. The React application should now be running at http://127.0.0.1:5173.

Usage

Once the backend is running on port 8000 and the frontend is running on port 5173, open http://127.0.0.1:5173 in your browser.

Sign Up
1. Go to Sign Up.
2. Enter a valid username, email, and a password of at least 8 characters.
3. Click Sign Up.
4. On success, you’ll be redirected to Log In.

Log In
1. Go to Log In.
2. Provide your email and password.
3. On success, you can now access Dashboard and Profile without encountering a 401 Unauthorized.

Dashboard
- Shows a list of any stored passwords.
- You can add new passwords by specifying “Site Name” and “Password,” then clicking Add.
- You can generate random passwords with Generate Random Password and copy them as needed.

Profile
- Displays your current username and email.
- You can update them by entering a new username/password and clicking Update.
- Delete your account permanently with Delete Account.

Local Development Notes

1. Cross-Site Cookies
If your backend is on http://127.0.0.1:8000 and frontend on http://127.0.0.1:5173, the browser considers them different sites. By default, cookies may be blocked in some browsers (e.g., Safari). For local dev:
- You may need to set secure=False and samesite="none" on your cookies.
- In Safari, you might disable Prevent cross-site tracking in Settings → Privacy to allow cookies during development.

2. CORS
Ensure your FastAPI main.py includes:
from fastapi.middleware.cors import CORSMiddleware

origins = ["http://127.0.0.1:5173", "http://localhost:5173"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

3. Axios withCredentials
In the frontend, confirm your Axios instance is created like this:
const instance = axios.create({
  baseURL: "http://127.0.0.1:8000",
  withCredentials: true
})
This allows cookies to be sent with each request.

Troubleshooting

1. 422 Unprocessable Entity
- The data sent to the server fails validation. Check your email format and ensure passwords are ≥ 8 characters.
- Open DevTools → Network tab to see if the server returns a detailed validation error.
2. 401 Unauthorized
- You may not be logged in, or the browser is not sending cookies.
- Check DevTools → Application → Cookies to confirm access_token is set.
- Set secure=False and samesite="none" on cookies for local testing, and ensure you have the correct CORS + Axios config.
3. No Tables
- If the database file is empty, run the initialization commands again.
- Confirm Base.metadata.create_all(bind=engine) is actually called.
4. Blank Screens
- Open DevTools → Console to see if there’s a React error.
- Check the Network tab for 404 or 500 statuses that might indicate misconfiguration or missing backend routes.
License

This project is for educational purposes. You can adapt or extend it as you see fit. If you use it in production, ensure you apply robust security measures (HTTPS, environment variables for secrets, etc.).