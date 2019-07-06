# import csv
# import operator
# with open('roles.csv','r') as csv_file:
#     role_reader = csv.reader(csv_file)
#     sort = sorted(role_reader,key=operator.itemgetter(2))

# with open('User_Roles.csv','w') as new_file:
#     role_writer = csv.writer(new_file,delimiter=',')

#     for eachline in sort:
#         role_writer.writerow(eachline)

#this works, don't touch


import csv
import operator
with open('user-roles.csv','r') as csv_file:
    role_reader = csv.reader(csv_file)
    sort = sorted(role_reader,key=operator.itemgetter(2))

with open('User_Roles_Processed.csv','w') as new_file:
    role_writer = csv.writer(new_file,delimiter=',')

    for eachline in sort:
        role_writer.writerow(eachline)