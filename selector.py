import keyboard
from functions import *


def refresh():
    clearConsole()
    entries = 0
    game = index-2
    if game < 0:
        game = 0
    if game > len(games)-5:
        game = len(games)-5
    printed_games = 0
    while printed_games < 5 and game < len(games):
        try:
            if game == index:
                print(">" + games[game])
            else:
                print(" " + games[game])
            printed_games += 1
            game += 1

        except IndexError:
            game += 1
    

def down():
    global index
    index += 1
    if index > len(games)-1:
        index = 0
    refresh()
def up():
    global index
    index -= 1
    if index < 0:
        index = len(games)-1
    refresh()
def select():
    global selector
    global index
    selector = False
    __import__(games[index]).main()
    


def main():
    selector = True
    keyboard.add_hotkey('up', lambda: up())
    keyboard.add_hotkey('down', lambda: down())
    keyboard.add_hotkey('enter', lambda: select())
    global index
    refresh()
    while selector:
        keyboard.wait()

if __name__ == "__main__":
    games = ["01_Acey_ducey", "02_Amazing", "03_Animal", "04_Awari", "05_Bagels", "06_Banner", "07_Basketball"]
    index = 0
    main()