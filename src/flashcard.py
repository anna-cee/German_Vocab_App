

from colorama import Fore, Back, Style
import randomlist

try:
    class FlashcardGenerator:
        def __init__(self, tablename):
            self.tablename = tablename
            print(Fore.MAGENTA, Style.BRIGHT + "FLASHCARD GENERATOR ...\n")
            self.nav_option(tablename)
        
        def nav_option(self, tablename):
            print(Fore.CYAN, Style.NORMAL)
            direction = input(f"Enter 'E' for English > German, or 'G' for German > English    ('N' = Next) ")
            if direction == 'E':
                self.flash_eng(tablename)
            elif direction == 'G':
                self.flash_germ(tablename)
            elif direction == 'N':
                self.flash_clear(tablename)
            elif direction != 'E' or direction != 'G' or direction != 'N':
                    print('Oops, try again \n')
                    (FlashcardGenerator(tablename))
        
        
        def flash_eng(self,tablename):
            index = 0
            while index < len(randomlist.englishlist):
                print(Fore.MAGENTA + '\n==================')
                print(Fore.MAGENTA, Style.BRIGHT + randomlist.englishlist[index])
                input()
                print(Fore.CYAN, Style.NORMAL + randomlist.germanlist[index])
                input()
                index += 1
            print(Fore.MAGENTA + 'Nochmal? Tryagain?')
            self.nav_option(tablename)
    

        def flash_germ(self,tablename):
            index = 0
            while index < len(randomlist.englishlist):
            
                print(Fore.MAGENTA + '\n==================')
                print(Fore.MAGENTA, Style.BRIGHT + randomlist.germanlist[index])
                input()
                print(Fore.CYAN, Style.NORMAL + randomlist.englishlist[index])
                input()
                index += 1
            print(Fore.MAGENTA + '\n Nochmal? Go again? \n')
            self.nav_option(tablename)
        

        def flash_clear(self,tablename):
                randomlist.englishlist = []
                randomlist.contextlist = []
                randomlist.germanlist = []

except:
     print('Oops, flashcards are not printing for this list.')           
    

            

       

           
        
        







            
