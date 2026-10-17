# cybersecurity-project1

A note storing app with basic functionality (register, log in, create, view, search, delete notes). Created in order to test security flaws in app design on the MOOC Cyber Security Base-course.

Warning: This app contains intentional security flaws and should not be deployed.

## Setup:

1. Install Python version 3.12 or later
2. Run the following commands in root:
   ```
   python3 -m pip install -r requirements.txt
   python3 manage.py migrate
   python3 manage.py seed
   python3 manage.py runserver
   ```
3. Open http://127.0.0.1:8000/

(note: on Windows, python3 might need to be replaced by python or py)

Demo users:

username: alice
password: redqueen

username: bob
password: squarepants
