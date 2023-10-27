#random list generator

#create a class that will generate a random list 
#for each vocabulary topic

# import csv


# f = open('/Users/anna/terminalapp/travel_and_directions.csv') # Remember, read-only mode is the default
# data = f.read()
# print(data)
# f.close() # Don't forget to close the file when done!



# import csv

# with open('/Users/anna/terminalapp/travel_and_directions.csv', 'r') as f:
#     reader = csv.reader(f)
#     reader.__next__() # Skip the first row (the column names)
#     for row in reader:
#         print(f'{row[0]} : {row[2]}')

# import csv

# with open('/Users/anna/terminalapp/travel_and_directions.csv','r',encoding='utf-8-sig') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#        print(row)

# import csv

# with open('/Users/anna/terminalapp/travel_and_directions.csv','r',encoding='utf-8-sig') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(row) #"The {row[0]} is {row[1]} years old and {row[2]}cm tall")

import csv

with open('/Users/anna/terminalapp/travel_and_directions.csv','r',encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['German']} means {row['English']} and an example is {row['Context']}.")



# import csv



# with open('/Users/anna/terminalapp/src/CSV/german_months.csv','r') as f:
#     for row in f:
#         print(f)


