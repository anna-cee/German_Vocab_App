# German Vocab Randomiser App

## Links

### [Code Style Guide](https://peps.python.org/pep-0008/)

### [GitGub](https://github.com/anna-cee/German_Vocab_App)
Please find the source code here. <br>
https://github.com/anna-cee/German_Vocab_App

### [Trello](https://trello.com/invite/b/0XZqDmc2/ATTI6be474109fc97b7e4a14337c8c0c24863C592958/terminal-app-development-planning-board) Board


## Purpose & Features
The German Vocab Randomiser App is a simple CLI app tool designed for the user who is a language learner to learn, recall and recycle vocabulary from a pool of lexical items targeted at their level. 
The lexical items are organised by topic, with a translation in to English and an example sentence in topic.
The app features are structures sequentially in order of complexity for the learner.
In German_Vocab_Randomiser App you can
- Choose a topic from a menu.
- Get a randomised list of 10 items with a translation and example. 
    - the following steps all practice this list.
- Generate on screen flashcards for each list
    - Learn the vocab items in either language direction
    - Unlimited cycles available, move on at end of any cycle.
- Generate a matching quiz to recall the items
    - Spelling also practiced here
    - No penalty for incorrect answers or spelling, unlimited guesses
    - Option to request answer
    - First-time guess score given!
    - Unlimited cycles available.
- Generate a gap-fill quiz to recall words and identify meaning from context.
    - Spelling practiced.
    - One guess only, then answer given
    - Unlimited cycles through quiz available.
    - Exit or move on at end of a cycle.

For a detailed rundown of the concept, features and code, please see my slide documentation in /ppt.

## Requirements 

### Python3
Python3 is required to run the app.
Check if you have python3 installed run:

    
```python3 --version```

You may have previous versions of Python. Upgrade to Python3 for this app.

To install python3 according to your OS, go to 
https://www.python.org/downloads/
and use the official installer.

### PiP Install

Pip is a widely-used package installer for Python.
A prompt in the bash script will get Pip to install all the app's dependencies automatically when it opens using the requirements.txt. Pip is included with Python versions 3.4 and higher. So after installing Python3, check if you have Pip on your system.


or  ```pip3 --version```



If it's not showing or you're not sure, you can install pip.<br>

    pip install pip==1.0.2 

Or to check out Pip before downloading it, go  [here](https://pypi.org/project/pip/1.0.2/#:~:text=In%20order%20to%20use%20pip,with%20easy_install%20pip%3D%3Ddev.) for more info 


### German Language Keyboard

You'll be able to use all the features with a standard keyboard, however some user input requires unique German alphabet characters to return a correct response. So, any words with *ö, ä, ü, ß*
#### For Windows
- Set system language to German: click on language bar and select German, or for more info go [here](https://support.microsoft.com/en-us/office/switch-between-languages-using-the-language-bar-1c2242c0-fe15-4bc3-99bc-535de6f4f258#:~:text=Click%20the%20language%20icon%20on,layouts%2C%20press%20Alt%2BShift.)
- Open Onscreen Keyboard, for more info go [here](https://support.microsoft.com/en-us/windows/use-the-on-screen-keyboard-osk-to-type-ecbb5e08-5b4e-d8c8-f794-81dbf896267a)

#### For Mac OS
- Set system language to German. Go to System Preferences > Keyboard > Input Sources and add German. Ensure box" "Show input in menu bar" is ticked. Or for more info [here](https://support.apple.com/en-au/guide/mac-help/mh26684/mac#:~:text=Change%20the%20system%20language,may%20need%20to%20scroll%20down.)
- Then in menu bar ensure language is set to "DE", then click on icon and select "Show Keyboard Viewer". Or for more info [here](https://support.apple.com/en-au/guide/mac-help/mchlp1015/mac)

This is the most straightforward and error-free way to enter the characters. It also allows you to learn your way around the German Keyboard layout. 


## Dependencies 

All package dependencies beyond the standard library in Python 3 will be installed by PiP when the program is run. They are listed in requirements.txt. Instructions for installing PiP is in the  *Requirements* under *PIP*.

colorama==0.4.6 <br>
iniconfig==2.0.0<br>
packaging==23.2<br>
pluggy==1.3.0<br>
prettytable==3.9.0<br>
pytest==7.4.3<br>
wcwidth==0.2.8<br>

## Installation Guide


1. Before installing, ensure you've checked your Python version as per *Requirements*.
2. Get a local copy of the repo: <br>
    - Go to the repo [homepage](https://github.com/anna-cee/German_Vocab_App) on GitHub 
    - Click the green Code button to open a drop-down menu and choose "Download Zip" to copy the app files to your local drive.
3. Unzip and go to code on your local drive 

    - Open your terminal and navigate to your Downloads directory (or folder where your web downloads are located).

    - Locate the zip file there and unzip. The name could be  German_Vocab_App.zip or German_Vocab_App-main.zip  To unzip:<br>
        ``` unzip German_Vocab_App-main.zip```

    - Once open navigate into the main App file.<br>
        ```cd German_Vocab_App-main```
    - Then into the source code file <br>
        ```cd src```
4. Run the code..
    - From here you can run the following command to get the bash script running, which will load the python program.<br>
    ```bash ./run_vocabapp.sh```
    or
    ```./run_vocabapp.sh```
    - If permission problems are present, run the following command:

        ```chmod +x run_vocabapp.sh ```
    
        then run the file again...
        ```bash ./run_vocabapp.sh```


    - The program will load and go from there!
        


## Style
[Code Style Guide](https://peps.python.org/pep-0008/)

## Sources

Garrels, M (2008) *Bash Guide for Beginners*, viewed 26 October 2023, https://tldp.org/LDP/Bash-Beginners-Guide/html/index.html

Goethe Institute (2012) *Goethe-Zertifikat A1 Start Deutsch 1: Wortliste"Goethe Institiue*, viewed 25 October 2023 <https://www.goethe.de/pro/relaunch/prf/de/A1_SD1_Wortliste_02.pdf>


## Software Development Plan 
please see my slide documentation in /ppt for detailed run down on plan, screenshots and features etx. Some screenshots included here as unsure exactly where they must be documented.

#### Monday 23.10
![alt text](image.jpg)
#### Tuesday 24.10

#### Wednesday 25.10

#### Thursday 26.10

#### Friday 27.10

#### Saturday 28.10

#### Sunday 29.10

#### Monday 30.10

#### Tuesday 31.10




Purpose & Scope
This is  a simple CLI app for practising a pool of vocabulary for language learners.
The idea is that rather than having discrete lists for different textbook modules or topics in different places or random words from the dictionary, you have the pool of vocabulary for your level in one place, but with the benefit of having the words organised by topic, as you would in language learning materials

Its aim is to:
	organise a pool of vocabulary aimed at a specific learning level into topical groups.
	allow you, the user, to choose random lists from each topic group.
	The random lists from a select pool help you mix recycling learned vocabulary while 		
	learning new vocabulary.
	Help you to practice recalling the lexical items, much like handmade flashcards.
	Have an opportunity to practice spelling accuracy.
	Have the opportunity to learn the lexical item in context as well as isolation.
	Allow for shorter or longer learning times.
	
The purpose is not to:
	tally/log incorrect answers or limit number of guesses, though correct recall is praised.

Instead, features are designed to allow you to freely repeat each exercise as much as you like, or skip one, or get a new list if you like.

Flow:

Activities are sequential, and in order of difficulty.
First a list is generated, then recall is practised with a Flashcard Generator, then user input is required to match the meanings, then finally a gap fill where user input has to match a missing word from context (a sentence).

Adaptablility/Personalisation

The application has been loaded with csv files generated from Goethe Institute’s A1 Vocabulary pool. However, the source code will draw the same activities from more csv files with the same column formatting - or the existing ones can be altered! This means that you cou For example, if you already have items organised into .csv on places like Anki (https://apps.ankiweb.net) or your purchased textbook materials, you could incorporate them all.
Filepath updates in randomlist.py and main.py and adding menu items in main.py would be needed for new csv items.
It also means the app could be adapted to other languages where ‘German’ or ‘germ’ in the source code, as well as the ‘German’ column in the csv files, was renamed. Or indeed, the English replaced with another first language.

Limitations

Once the user has completed the activities of one random list and returns to main, they cannot access the exact same list again. They can produce another list from the same vocabulary pool. How often they encounter the same words in each pool is largely dependent on the size of the pool, which you can alter directly with access to the csv.
The number of words is always 10. Because there is so much opportunity for the user to practice or exit the learning cycle, it didn’t seem necessary to add a range of list lengths, however this could be altered.
The application does not account for word form changes in activities where words are in context, including verb conjugation, declination of articles etc. Applying lemmatisation was beyond the scope of this project but python packages for German are available here and could make this possible for future larger projects.



Features

Welcome 
Menu
A menu to choose from 5 topics
The topic menu takes a number input and generates the list from there.
You can navigate back to the menu after any activity. This means you can extend or shorten how much time or how many activities you want on each list.
The menu also lets you quit the program at any time.

Random list generator
	Prints random list of 10 items in a table English + German
	Extension reprints table with context or items in sentences.
	The user navigates simple through the options pressing any key.
Navigation
	At the end of the random list, as as the end of each activity you can navigate onto the the next step or return to menu and from there start afresh or exit the program. At the end of the last activity

Flashcard generator
	the Flashcard Generator lets you choose which direction to learn in German > English or English > German. The user cycles through the list pressing any key to print the lexical item followed by the translation. At the end of the list you can cycle through again with option to choose the same translation direction or another, or move to next activity.
Again the Navigation option allows for a return to the main menu/

Match Quiz Generator

The Match Quiz Generator generates a question for the meaning of one lexical item at a time. The user should input the correct spelling of the word. There are no penalties for incorrect attempts or spelling, and unlimited attempts are possible or check the answer with ‘C’. At the end of the list, a tally of first-time guesses is printed.
Note, for nouns (substantives), the direct article has been retained, so correct answer for ‘apple’ is ‘das Apfel’. German spelling variations ü, ö, ä and ß should also be entered. See Installation and requirements, but the easiest option is to use a keyboard viewer on your machine for this.
At the end of the quiz you can repeat it, move to next to navigate back to main menu.

Context Quiz Generator
	

The Context Quiz Generator reproduces the context sentence from the original random list with the target vocabulary to be learned blanked out. You get a prompt to enter the missing word, if the entry is incorrect or misspelled, the answer is printed. As the Match Quiz allows for many tries, this one just offers one, then gives the answer. 
There is praise for correct first-time guesses but no penalty for incorrect entries. This is also designed this way as inevitably there is often more than one possible word for a sentence or there maybe synonyms in the list e.g. “der Zug” and “die S-Bahn” would both translate as train, and in-/definite articles may not be present or beginner level learner may not be able to interpret them sufficiently to determine which is missing.
Though only one try is given per prompt, the user can opt to do the quiz again or move on.
The navigation feature returns back to main menu.




