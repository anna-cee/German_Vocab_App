import csv
import random
import string
from prettytable import PrettyTable
from colorama import Fore, Back, Style





table = PrettyTable()
germanlist = []
englishlist = []
contextlist = []

healthlist = open(f'/Users/anna/terminalapp/body_and_health.csv','r',encoding='utf-8-sig')
spendinglist= open(f'/Users/anna/terminalapp/money_and_transactions.csv','r',encoding='utf-8-sig')
foodlist = open(f'/Users/anna/terminalapp/food.csv','r',encoding='utf-8-sig')
timelist = open(f'/Users/anna/terminalapp/time_vocab.csv','r',encoding='utf-8-sig')
travellist = open(f'/Users/anna/terminalapp/travel_and_directions.csv','r',encoding='utf-8-sig')


class Randomlist:
    def __init__(self, listdir):
        self.vocablist = [r for r in csv.DictReader(listdir)]
        self.randomlist = random.sample(self.vocablist, 10)
        self.workinglist = self.randomlist
        print(self.randomlist)


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
        print(Fore.GREEN + 'RANDOM LIST...')
        print(Fore.GREEN + self.vocabtable)
        input('Press any key to see list with words in context.')
        self.vocabtable = table.get_string(fields=["German", "English", "Context"])
        print(Fore.GREEN +self.vocabtable)
        input('Press any key to start FLASHCARDS.\n')

# def reset_table(self, tablename):
#         self.germanlist  = None
#         self.englishlist = None
#         self.contextlist = None     

        

               
                







            
