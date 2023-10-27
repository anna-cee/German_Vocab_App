
#working random list generator or 10 items

import csv
import random


#data = [r for r in csv.reader(open('/Users/anna/terminalapp/travel_and_directions.csv','r',encoding='utf-8-sig'))]
vocablist = [r for r in csv.DictReader(open('/Users/anna/terminalapp/travel_and_directions.csv','r',encoding='utf-8-sig'))]
randomlist = random.sample(vocablist, 10)
for row in randomlist: 
    print(f"{row['German']} : {row['English']}")