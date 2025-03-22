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

CRUD Operations: Describe the features that allow users to create, read, update, and delete blog posts.

User Permissions: Explain how the permission system works, including the LoginRequiredMixin and UserPassesTestMixin.

Testing: Mention how to test the features, including creating a new post, editing, and deleting it.

## Comment System

The comment system allows users to interact with blog posts by posting, editing, and deleting comments. 

### Features:
1. **Post Comments**: Logged-in users can post comments on blog posts.
2. **Edit Comments**: Only the author of a comment can edit it.
3. **Delete Comments**: Only the author of a comment can delete it.

### Usage:
- To add a comment, navigate to the post's detail page and use the comment form.
- To edit a comment, click "Edit" next to your comment.
- To delete a comment, click "Delete" next to your comment.