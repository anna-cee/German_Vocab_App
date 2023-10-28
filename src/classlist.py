import csv
import random
import string
from prettytable import PrettyTable
x = PrettyTable()


germanlist = []
englishlist = []
contextlist = []

class randomList:
    def __init__(self, topic_filename):
        self.vocablist = [r for r in csv.DictReader(topic_filename)]
        self.randomlist = random.sample(self.vocablist, 10)
        #for row in self.randomlist: 
            #print(f"{row['German']} : {row['English']}")
    

    # Setter
    def set_list(self, listname):
        for row in self.randomlist:
            for k, v in row.items():
                if k == "German":
                    germanlist.append(v)
            for k, v in row.items():
                if k == "English":
                    englishlist.append(v)
            for k, v in row.items():
                if k == "Context":
                    contextlist.append(v)

        x.add_column("German", germanlist)
        x.add_column("English", englishlist)
        x.add_column("Context", contextlist)
        print(x.get_string(fields=["German", "English"]))


        
    
    

    
    def list_cycle(self, listname):
        response = input(f"Press ENTER to cycle the list or 'f' to exit.")
        while response != 'f':
            for row in self.randomlist: 
                if response != 'f':
                    response = input(row['German'])
                    response = input(row['English'])
                print('\n')

    

    def quiz_generator(self, listname):
        correctcounter = 0
        for item in self.randomlist:
            targetvocab = item['German']
            definevocab = item['English']
            cleantarget = targetvocab.rstrip()
            cleandefine = definevocab.rstrip()
            
            answer = input(f'What is the German for {cleandefine}? ')
            if answer == cleantarget:
                correctcounter += 1
                print(f"Richtig! {cleandefine} is '{cleantarget}'\n")
            while answer != cleantarget:
                answer = input(f"Nochmal eingeben bitte! (try again or hit 'c' to check answer)  \n ")  
                if answer == 'c':
                    answer = cleantarget
                    print(f"{cleandefine} is '{cleantarget}'")
                elif answer == cleantarget:
                    correctcounter += 1
                    print(f"Richtig! {cleandefine} is '{cleantarget}' \n")
        print(f" Toll! You remembered {correctcounter} items! \n")




            


# for row in self.randomlist: 
#             print(f"{row['German']} : {row['English']}")
#         print('\n')            


