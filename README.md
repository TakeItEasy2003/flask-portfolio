# Flask Portfolio Website

This is a simple portfolio website built using Flask, PostgreSQL, HTML, CSS, and JavaScript. It was created as part of a database assignment project.

**Live Site:** [https://flask-portfolio-tus6.onrender.com/messages](https://flask-portfolio-tus6.onrender.com/messages)  
**GitHub Repo:** [https://github.com/TakeItEasy2003/flask-portfolio](https://github.com/TakeItEasy2003/flask-portfolio)

## Features

- Home, About, Projects, Skills, and Contact pages
- Contact form that saves submissions to a PostgreSQL database
- Admin login system (manual)
- Admin-only message viewer and delete functionality
- Responsive design and clean styling
- JavaScript shortcut to access admin login (Shift + A)

## Tech Stack

- Python 3.12
- Flask
- Flask-SQLAlchemy
- PostgreSQL
- HTML, CSS
- JavaScript

## Getting Started

1. Clone the repository:
   git clone https://github.com/TakeItEasy2003/flask-portfolio.git
   cd flask-portfolio

2. Create and activate a virtual environment:
   python3 -m venv venv
   source venv/bin/activate  (or venv\Scripts\activate on Windows)

3. Install dependencies:
   pip install -r requirements.txt

4. Set up PostgreSQL:
   createdb portfolio

5. Initialize the database:
   from app import db, app
   with app.app_context():
       db.create_all()

6. Run the app:
   python app.py

7. Visit http://127.0.0.1:5000 in your browser.

## Admin Access

- Visit /admin-login
- Login with:
  - Username: admin
  - Password: 1234
- After logging in, access /messages to view and delete contact form submissions
- Logout via /logout

Press Shift + A anywhere to quickly open the admin login page.

## Project Structure

```
flask_portfolio/
├── app.py
├── requirements.txt
├── Procfile
├── README.md
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── about.html
│   ├── projects.html
│   ├── skills.html
│   ├── contact.html
│   ├── admin_login.html
│   └── messages.html
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
```

## Deployment

You can deploy this app to Render by:

- Pushing the project to GitHub
- Creating a web service on Render
- Connecting a PostgreSQL database
- Setting environment variables
- Deploying from the GitHub repo
