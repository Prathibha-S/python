import csv
with open('/content/csv1.csv','r')as f:
  data = csv.reader(f)
  for row in data:
        print(row)
