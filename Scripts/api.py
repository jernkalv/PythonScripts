import requests
import csv
import operator

response = requests.get('https://api.emp.healthgrades.com/api/auth/reports/user-roles', headers={'Authorization': 'Bearer juolsJI5iLWCcoH27tZqbxGxK3eK1YfRgz7eTew8Gue'})
role_reader = csv.reader(response)
decoded_content = response.content.decode('utf-8')

cr = csv.reader(decoded_content.splitlines(), delimiter=',')
sort = sorted(response,key=operator.itemgetter(2))

my_list = list(cr)

for row in my_list:
    print(row)


    