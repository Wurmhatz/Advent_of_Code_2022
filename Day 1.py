import os
os.chdir('/Users/Helgi/Python/Advent of Code 2022/Day 1')

class ElfCalCalc:

    #Imports data from .txt file, sums the values until there is a line break (e.g. a ValueError) and adds it to a list for analysis.
    def elfCalories(self):
        with  open('input.txt', 'r') as caloricReadout:
            elfCalorieTotal = []
            total = 0

            for line in caloricReadout.readlines():
                try:
                    total += int(line)
                except ValueError:
                    elfCalorieTotal.append(total)
                    total = 0
                    pass

        #Prints the largest value in the the list, corresponding to the largest number of "calories" carried by an elf. 
        print('The largest number of calories carried by a single elf is ' + str(max(elfCalorieTotal)))
        maxCal = max(elfCalorieTotal)
        print('Elf # ' + str([index for index, item in enumerate(elfCalorieTotal) if item == maxCal]) + ' is carrying the most calories.')
        
        #Reverse sorts the caloric list and sums the top three numbers together.
        sortedElfCal = sorted(elfCalorieTotal, reverse=True)
        topThreeCal = sum(sortedElfCal[:3])
        print('The total calories carried by the top 3 elves is ' + str(topThreeCal))
        
        return elfCalorieTotal

s = ElfCalCalc()
s.elfCalories()
