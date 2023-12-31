import csv
import random
import os
import string
from prettytable import PrettyTable
#from prettytable.colortable import ColorTable
from colorama import Fore, Back, Style


table = PrettyTable()
germanlist = []
englishlist = []
contextlist = []



healthlist = open(f'body_and_health.csv','r',encoding='utf-8-sig')
spendinglist= open(f'money_and_transactions.csv','r',encoding='utf-8-sig')
foodlist = open(f'food.csv','r',encoding='utf-8-sig')
timelist = open(f'time_vocab.csv','r',encoding='utf-8-sig')
travellist = open(f'travel_and_directions.csv','r',encoding='utf-8-sig')

try:

    class Randomlist:
        def __init__(self, listdir):
            self.vocablist = [r for r in csv.DictReader(listdir)]
            self.randomlist = random.sample(self.vocablist, 10)
            self.workinglist = self.randomlist
        
        

    class TableGenerator:
        def __init__(self, tablevocab):
            self.tablevocab = tablevocab
            self.germanlist = germanlist
            self.englishlist = englishlist
            self.contextlist = contextlist 
        
            for row in self.tablevocab:
                for k, v in row.items():
                    if k == "German":
                        germanlist.append(v)
                for k, v in row.items():
                    if k == "English":
                        englishlist.append(v)
                for k, v in row.items():
                    if k == "Context":
                        contextlist.append(v)
            table.add_column("English", self.englishlist)
            table.add_column("German", self.germanlist)
            table.add_column("Context", self.contextlist)
            self.vocabtable = table.get_string(fields=["German", "English"])
            print(Fore.GREEN, Style.BRIGHT + 'RANDOM LIST...')
            print(Fore.GREEN, Style.NORMAL + self.vocabtable)
            print(Style.RESET_ALL)
        
            input('Press any key to see list with words in context.')
            self.vocabtable = table.get_string(fields=["German", "English", "Context"])
            print(Fore.GREEN + self.vocabtable)
            print(Style.RESET_ALL)

            self.vocabtable = table.clear()
            
except:
    print("Oops we couldn't find that list")
    

        
            


                

                
                    







                
