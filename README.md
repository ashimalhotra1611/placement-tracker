 # Placement Tracker

A Django web app to track internship and job applications in one place.

## Features
- Add a new application (company, role, status, date, notes)
- View all applications in a table
- Edit and delete applications
- Status tracking: Applied, Interview, Offer, Rejected
-  User login and signup (each user sees only their own           applications)
- Dashboard with status-wise charts
- Resume upload with job description match score

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
Then open http://127.0.0.1:8000 in your browser.

## Author
Ashi Malhotra, MCA (Integrated) student    