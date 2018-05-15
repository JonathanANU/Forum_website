# This file reads id.txt and assigns each student ID in the id.txt
# a default password which can be changed later
from Forum1040.data.models import *

initialize_db()


def register():
    try:
        file = open("id.txt", "r")
        for each_line in file:
            each_id = str(each_line.strip())
            if each_id != '':
                User.create(username=each_id,
                            password=each_id)
        file.close()
        print("Registration complete!")

    except IntegrityError:
        print("You have already registered some or all users in 'id.txt'!")
        print("To register new users, delete all the previously "
              "registered users first, \n"
              "And then input new users in 'id.txt'")
        print("Please contact IT team if you need help.")
        print("Email: example@awesome.com")
        print("Phone: 1234-5678-0000")

register()
