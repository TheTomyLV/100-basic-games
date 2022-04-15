from functions import *

class Room:
    def __init__(self) -> None:
        self.left = None
        self.right = None
        self.down = None
        self.up = None

class Maze:
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width
        self.rooms = []
    def create_maze(self) -> None:
        for y in range(self.width):
            self.rooms.append([])
            for x in range(self.length):
                self.rooms[y].append(Room())
    def draw_rooms(self) -> None:
        for y in range(len(self.rooms)):
            for room in self.rooms[y]:
                if y == 0:
                    print(" __", end="")
                    continue
                print("|__", end="")
            if y == 0:
                print(" __")
            else:
                print("|__|")

def main():
    clearConsole()
    maze = Maze(15, 10)
    maze.create_maze()
    maze.draw_rooms()

if __name__ == "__main__":
    main()