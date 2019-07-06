import requests
import csv

response = requests.get('https://api.emp.healthgrades.com/api/auth/reports/user-roles', headers={'Authorization': 'Bearer juolsJI5iLWCcoH27tZqbxGxK3eK1YfRgz7eTew8Gue'})

decoded_content = response.content.decode('utf-8')

cr = csv.reader(decoded_content.splitlines(), delimiter=',')
my_list = list(cr)
for row in my_list:
    print(row)







import csv
import operator
with open('user-roles.csv','r') as csv_file:
    role_reader = csv.reader(csv_file)
    sort = sorted(role_reader,key=operator.itemgetter(2))

with open('User_Roles.csv','w') as new_file:
    role_writer = csv.writer(new_file,delimiter=',')

    for eachline in sort:
        role_writer.writerow(eachline)
