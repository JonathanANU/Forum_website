# This file deals with the registering of admin users
from Forum1040.data.models import *

# initialize and connect to the database
initialize_db()

# prompt the user to input username and password for the new admin user
ADMIN_USERNAME = input("Username? Press 'Enter' to proceed -- ")
ADMIN_PASSWORD = input("Password? Press 'Enter' to proceed -- ")
registration_status = False

while registration_status is False:
    try:
        Admin.create(
            username=ADMIN_USERNAME,
            password=ADMIN_PASSWORD
        )
        registration_status = True
    except IntegrityError:
        print("Username already exists! Try a new one.\n"
              "Press Control + C to quit registering.")
        ADMIN_USERNAME = input("Username? -- ")
        ADMIN_PASSWORD = input("Password? -- ")

print("Registration done!")
