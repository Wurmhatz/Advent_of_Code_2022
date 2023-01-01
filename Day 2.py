import os
os.chdir('/Users/Helgi/Python/Advent of Code 2022/Day 2')

class RockPaperScissor:

    #Part 1
    #The function below imports the data from the txt file, reads it, and splits it at the line breaks.
    #The function then creates a dictionary for each of the 9 possible game outcomes.
    #The final print statement also maps the game inputs from the txt file to dictionary values and sums them up.
    def pointCalc(self):

        games = open("input.txt", 'r').read().split("\n")

        points = {"A X":4, "A Y":8, "A Z": 3, "B X":1, "B Y":5, "B Z":9, "C X":7, "C Y":2, "C Z":6, '':0}

        print(f"The final score of the player is {sum([points[game] for game in games])}")


    #Part 2
    #The function below works identically to Part 1, it just has an updated dic
    def realPointCalc(self):

        realGames = open("input.txt", 'r').read().split("\n")

        realPoints = {"A X":3, "A Y":4, "A Z": 8, "B X":1, "B Y":5, "B Z":9, "C X":2, "C Y":6, "C Z":7, '':0}

        print(f"The ACTUAL final score of the player is {sum([realPoints[game] for game in realGames])}")


s = RockPaperScissor()
s.pointCalc()
s.realPointCalc()