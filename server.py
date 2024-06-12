import json
import anvil.server
import threading
from anvil.tables import app_tables
import os.path

# Function to save email to local storage
def save_email_to_local_storage(email):
    data = {'email_user': email}  # Create a new data dictionary with the latest email
    # Save the updated data to local storage, overwriting the existing file
    with open('emails.json', 'w') as file:
        json.dump(data, file)

# Function to retrieve email from local storage
def get_email_from_local_storage():
    try:
        with open('emails.json', 'r') as file:
            data = json.load(file)
            email = data.get('email_user', None)
    except FileNotFoundError:
        email = None
    return email

# Function to share email
@anvil.server.callable
def share_email(email):
    save_email_to_local_storage(email)
    return email

# Function to retrieve shared email
@anvil.server.callable
def another_method():
    email_user = get_email_from_local_storage()
    print(email_user)
    return email_user

# Check if the 'emails.json' file exists on the mobile device
# If not, create an empty file to prevent FileNotFoundError
if not os.path.isfile('emails.json'):
    with open('emails.json', 'w') as file:
        json.dump({}, file)
# Function to share email
@anvil.server.callable
def share_email(email):
    save_email_to_local_storage(email)
    return email

# Function to retrieve shared email
@anvil.server.callable
def another_method():
    email_user = get_email_from_local_storage()
    print(email_user)
    return email_user




text = None
lock = threading.Lock()

@anvil.server.callable
def loan_text(new_text):
    # Acquire the lock before updating the global variable
    with lock:
        globals()['text'] = new_text
    return new_text

@anvil.server.callable
def loan_amount_text():
    with lock:
        current_text = globals().get('text', None)
        print(current_text)
        return current_text

@anvil.server.callable
def view_loan(new_text):
    # Acquire the lock before updating the global variable
    with lock:
        globals()['num'] = new_text
    return new_text

@anvil.server.callable
def view_loan_text():
    with lock:
        current_text = globals().get('num', None)
        print(current_text)
        return current_text
