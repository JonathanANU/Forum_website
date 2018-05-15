from Forum1040.data.models import *

initialize_db()

file = open("id_demo.txt", "w")
for i in range(1000, 1100):
    file.writelines('u'+str(i)+'\n')

file = open("id_demo.txt", "r")
for each_line in file:
    each_id = str(each_line.strip())
    if each_id != '':
        User.create(username=each_id,
                    password=each_id)
