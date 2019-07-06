import requests
import operator
import pandas as pd

response = requests.get('https://api.emp.healthgrades.com/api/auth/reports/user-roles', headers={'Authorization': 'Bearer juolsJI5iLWCcoH27tZqbxGxK3eK1YfRgz7eTew8Gue'})
role_reader = pd.read_csv(response)
decoded_content = response.content.decode('utf-8')

cr = pd.read_csv(decoded_content.splitlines(), delimiter=',')

my_list = list(cr)

my_list.to_csv('new_reponse_csv.csv')
