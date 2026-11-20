# Placement Tracker

A Django web app to track internship and job applications in one place.

## Features
- Add a new application (company, role, status, date, notes)
- View all applications in a table
- Edit and delete applications
- Status tracking: Applied, Interview, Offer, Rejected
- User signup, login and logout (each user sees only their own applications)
- Dashboard with status counts and a status chart
- Search and filter applications
- Bootstrap-styled responsive UI

## Tech Stack
- Python
- Django
- SQLite
- HTML

## How to Run
```
git clone https://github.com/ashimalhotra1611/placement-tracker.git
cd placement-tracker
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Then open http://127.0.0.1:8000 in your browser and sign up for a new account.

## Planned Features
- Resume upload with job description match score

## Author
Ashi Malhotra, MCA (Integrated) student