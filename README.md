# cybersecurity-project1

A note storing app with basic functionality (register, log in, create, view, search, delete notes). Created in order to test security flaws in app design on the MOOC Cyber Security Base-course.

Warning: This app contains intentional security flaws and should not be deployed.

## Flaws:

OWASP Top 10 2021:

- FLAW 1: A01 Broken Access Control in views.py
- FLAW 2: A02 Cryptographic Failures in settings.py
- FLAW 3: A03 Injection in views.py
- FLAW 4: A07 Identification and Authentication Failures in settings.py
- FLAW 5: A09 Security Logging and Monitoring Failures in settings.py and views.py

Each flaw has a marker for `# FLAW N` and `# FIX N` with the fix being the commented out part

The before and after screenshots demonstrating the flaws can be found in [screenshots](https://github.com/w1ll1ey/cybersecurity-project1/tree/main/screenshots).

Note on FLAW 2: `python3 manage.py seed` needs to be rerun after turning the flaw on or off.

## Setup:

1. Install Python version 3.12 or later
2. Run the following commands in the repository folder containing manage.py:
   ```
   python3 -m venv venv
   source venv/bin/activate
   python3 -m pip install -r requirements.txt
   python3 manage.py migrate
   python3 manage.py seed
   python3 manage.py runserver
   ```
3. Open http://127.0.0.1:8000/

(note: on Windows, python3 might need to be replaced by python or py and source venv/bin/activate by venv\Scripts\activate)

Demo users:

username: alice
password: redqueen

username: bob
password: squarepants
