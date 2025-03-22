# Django Blog Authentication System

## Overview
This system allows users to register, log in, log out, and manage their profile information.

## Setup Instructions

1. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2. **Database Migrations**:
    ```bash
    python3 manage.py migrate
    ```

3. **Create a Superuser (for admin access)**:
    ```bash
    python3 manage.py createsuperuser
    ```

4. **Run the Development Server**:
    ```bash
    python3 manage.py runserver
    ```

## Authentication Features
- **Registration**: Users can register with a username, email, and password.
- **Login**: Users can log in using their credentials.
- **Logout**: Users can log out.
- **Profile**: Users can view and update their email (and other fields if extended).
