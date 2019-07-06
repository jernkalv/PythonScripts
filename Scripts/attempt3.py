#this works!
import pandas as pd

df = pd.read_csv("C:\\Users\\blambert\\Documents\\Temp\\user-roles-2019-05-20.csv",  header=None, names=["Email Address","Cleint","Client Code","Roles 1","Roles 2","Roles 3","Roles 4","Roles 5","Roles 6","Roles 7","Roles 8","Roles 9","Roles 10"])
df


df.to_csv('new.csv', index=False)