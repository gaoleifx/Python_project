import csv
import os

with open('20_2.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        keys = str(list(row.keys())[0]).split('\t')
        values = str(list(row.values())[0]).split('\t')
        mycomp = {mykey:myvalue for mykey, myvalue in zip(keys, values)}
        posInfo = mycomp['位置信息']
        aa = posInfo.rsplit(sep=',')
        print(posInfo)
        
            