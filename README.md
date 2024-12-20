# FastBlogify - A FastAPI Blog Application

FastBlogify is a blog platform built using **FastAPI**, allowing users to create, read, update, and delete blog posts. It includes user authentication and authorization using JWT tokens and OAuth2.

## Features
- **Create Blog**: Allows users to create a blog post.
- **Read Blog**: Allows users to read blog posts.
- **Update Blog**: Allows users to update their own blog posts.
- **Delete Blog**: Allows users to delete their own blog posts.
- **User Authentication**: Login and sign up functionality with JWT token.
- **OAuth2 Authentication**: Secure login using OAuth2 for third-party authentication.

## Technologies Used
- **FastAPI**: A modern web framework for building APIs with Python 3.7+.
- **Pydantic**: Data validation and settings management.
- **JWT**: JSON Web Token for secure user authentication.
- **OAuth2**: Authorization framework for third-party logins.
- **SQLite**: Database to store user and blog data.

## Requirements

Make sure you have Python 3.7+ installed. You can install the dependencies using `pip` from the `requirements.txt` file.

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Mubeen-Zaki/FastBlogify.git
   cd FastBlogify
2. **Create a virtual environment (optional but recommended)**:
   ```bash
   python -m venv .venv
3. **Activate the virtual environment:**
   ```bash
   venv\Scripts\activate
4. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
5. **Running the Application**
   ```bash
   uvicorn blog.main:app --reload

### Shoutouts:
   - Special thanks to [Sarthak](https://github.com/sarthaksavvy) for this amazing FastAPI tutorial!
   - Tutorial Link: [Youtube Video](https://www.youtube.com/watch?v=7t2alSnE2-I&list=LL&index=2)
   - Documentation: [User Guide](https://fastapi.tiangolo.com/tutorial/)
