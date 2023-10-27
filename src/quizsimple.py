 

import csv
import random



vocablist = [r for r in csv.DictReader(open('/Users/anna/terminalapp/travel_and_directions.csv','r',encoding='utf-8-sig'))]
randomlist = random.sample(vocablist, 3)
#print(randomlist)
correctcounter = 0
for item in randomlist:
    errorcounter = 0
    targetvocab = item['German']
    definevocab = item['English']
    cleantarget = targetvocab.rstrip()
    cleandefine = definevocab.rstrip()
    
    answer = input(f'What is the German for {cleandefine}? ')
    if answer == cleantarget:
        correctcounter += 1
        print(f"Richtig! {cleandefine} is '{cleantarget}'")
    while answer != cleantarget:
        errorcounter += 1
        answer = input(f"Nochmal eingeben bitte! (try again or hit 'c' to check answer)   ")  
        if answer == 'c':
            answer = cleantarget
            print(f"{cleandefine} is '{cleantarget}'")
        elif answer == cleantarget:
            correctcounter += 1
            print(f"Richtig! {cleandefine} is '{cleantarget}'")
        #elif errorcounter == 1:
            #input("Don't forget articles for nouns: 'der', 'die' or 'das'. Try again..  ")
print(f" Toll! You remembered {correctcounter} items!")

    
        
  
    