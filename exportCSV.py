import csv

path = "E:/Python_project/new.csv"

dict1 = {"xiaoming":'60', "xiaoli":'25', "wangwu":'35'}

with open(path, 'w', newline='') as csv_file:
    fieldnames = ['name', 'age']
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()
    tuples = dict1.items()
    for tup in tuples:
        data = dict()
        data['name']=list(tup)[0]
        data['age']=list(tup)[1]
        csv_writer.writerow(data)

