# import csv
# import operator
# sample = open('user-roles-2019-05-13.csv','w',newline='')
# csv1 = csv.writer(sample,delimiter=',')
# # csv1 = csv.reader(sample,delimiter=',')
# sort = sorted(csv1,key=operator.itemgetter(2))
# for eachline in sort:
#     # cut this out if it doesn't work

#     # print(eachline)
#     csv1.writerows(eachline)


import csv
import operator
sample = open('user-roles-2019-05-13.csv','r')
csv1 = csv.reader(sample,delimiter=',')
sort = sorted(csv1,key=operator.itemgetter(2))
for eachline in sort:
    print(eachline)
