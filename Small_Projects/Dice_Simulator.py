import random
import matplotlib.pyplot as plt
import numpy as np


class Dice:
    def __init__(self, sides):
        self.number = sides

    def show_sides(self):
        print(self.number)

    def roll_the_dice(self):
        return random.randint(1, self.number)


class Data:
    def __init__(self, sides):
        self.number = sides
        self.rolls = [[0 for _ in range(self.number)]]

    def add_date(self, rolled_number):
        self.rolls.append([x for x in self.rolls[len(self.rolls)-1]])
        self.rolls[len(self.rolls) - 1][rolled_number-1] += 1

    def print_date(self):
        print(self.rolls)

    def get_date(self):
        return self.rolls

    def extract_number_data(self, time):
        extracted = []
        for x in range(self.number):
            extracted.append([self.rolls[i][x] for i in range(time+1)])
        return extracted

    def print_index(self, index):
        print(self.rolls[index][5])

    def plot_date(self, time):
        """After plt.show()"""
        extracted = self.extract_number_data(time)
        fig = plt.figure()
        ax = fig.gca()
        ax.set_xticks(np.arange(0, time+1, int(max(time/30, 1))))
        ax.set_yticks(np.arange(0, int(max([i.pop() for i in extracted])+1), int(max(max([i.pop() for i in extracted])/10, 1))))

        for number in range(self.number):
            plt.plot(extracted[number], '-')

        plt.legend('123')
        plt.xlabel("Time")
        plt.ylabel("Rolls")
        plt.grid()

    def plot_highest_lowest_date(self, time):
        extracted = self.extract_number_data(time)
        extracted_last_values = [i.pop() for i in extracted]

        fig = plt.figure()
        ax = fig.gca()
        ax.set_xticks(np.arange(0, time + 1, max(time / 50, 1)))
        ax.set_yticks(np.arange(0, int(max(extracted_last_values)+1), int(max(max(extracted_last_values)/10, 1))))

        plt.plot(extracted[extracted_last_values.index(max(extracted_last_values))])
        plt.plot(extracted[extracted_last_values.index(min(extracted_last_values))])

        plt.xlabel("Time")
        plt.ylabel("Rolls")
        plt.grid()

    def print_tail(self, length=10):
        print(self.rolls[(len(self.rolls)-length)::])


random.seed(22)
NUMBER_SIDES = 100
TIME = 5000
six_dice = Dice(NUMBER_SIDES)
rolled_data = Data(NUMBER_SIDES)
for i in range(TIME):
    rolled_data.add_date(six_dice.roll_the_dice())

rolled_data.plot_highest_lowest_date(TIME)
rolled_data.plot_date(TIME)
plt.show()