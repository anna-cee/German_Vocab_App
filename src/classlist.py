import csv
import random
import string




class randomList:
    def __init__(self, topic_filename):
        self.vocablist = [r for r in csv.DictReader(topic_filename)]
        self.randomlist = random.sample(self.vocablist, 3)
        #for row in self.randomlist: 
            #print(f"{row['German']} : {row['English']}")
    

    # Setter
    def set_list(self, listname):
        for row in self.randomlist: 
            print(f"{row['German']} : {row['English']}")
        print('\n')
        
        
    
    

    
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




            


            


