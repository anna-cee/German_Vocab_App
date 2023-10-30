

from colorama import Fore, Back, Style
import randomlist

class FlashcardGenerator:
    def __init__(self, tablename):
        self.tablename = tablename
        print(Fore.MAGENTA + "FLASHCARD GENERATOR ...\n")
        self.nav_option(tablename)
    
    def nav_option(self, tablename):
        direction = input(f"Enter 'E' for English > German, or 'G' for German > English    ('N' = Next) ")
        if direction == 'E':
            self.flash_eng(tablename)
        elif direction == 'G':
            self.flash_germ(tablename)
        elif direction == 'N':
            self.flash_clear(tablename)
        elif direction != 'E' or direction != 'G' or direction != 'N':
                print('Oops, try again')
                (FlashcardGenerator(tablename))
       
    
    def flash_eng(self,tablename):
        index = 0
        while index < len(randomlist.englishlist):
            print(Fore.MAGENTA + '\n==================')
            print(Fore.MAGENTA, Style.BRIGHT + randomlist.englishlist[index])
            input()
            input(randomlist.germanlist[index])
            index += 1
        print('Nochmal? Tryagain?')
        self.nav_option(tablename)
   

    def flash_germ(self,tablename):
        index = 0
        while index < len(randomlist.englishlist):
        
            print('\n==================')
            print(randomlist.germanlist[index])
            input()
            input(randomlist.englishlist[index])
            index += 1
        print('\n  Nochmal? Go again? \n')
        self.nav_option(tablename)
      

    def flash_clear(self,tablename):
            randomlist.englishlist = []
            randomlist.contextlist = []
            randomlist.germanlist = []
          
    

            

       

           
        
        







            
