
# This simulator was made by https://github.com/PetraSil for fun and practice
# by me, a first year ICT-student.
# If you have any guestions or constructive suggestions drop me a message!


import random
import matplotlib.pyplot as plt
import numpy as np
import time


def main():
    while True:
        intro()
        popAmount = population()
        popDensity = populationDensity()
        inDays = infectionDays()
        virus = virusSeverity()
        vaccine = vaccineCheck()
        start = simulationClass(popAmount, popDensity, inDays, virus, vaccine)
        start.simulation(popAmount, popDensity, inDays, virus, vaccine)
        if exit():
            return


# explain what happens and what to do
def intro():
    time.sleep(1)
    print("Welcome to a little simulator that I made just for fun and "
          "practice, so do not expect anything realistic as this is just "
          "for fun with mostly arbitrary numbers and odds! \n\n"
          "In this simulator, you can choose from certain options "
          "that determine how effective an imaginary virus will be "
          "at infecting humans in the period of a year or less. "
          "Simply follow the instructions given and all will be well! \n\n")
    time.sleep(2)


# ask for the amount of population
def population():
    while True:
        try:
            popAmount = int(input("Give the amount of population for the virus"
                                  " to play with. Use only whole numbers and "
                                  "no decimals: "))
            print("\n")
            time.sleep(1)
            return popAmount
        except ValueError:
            print("Please give a valid number.\n")


# ask for the population density
def populationDensity():
    while True:
        try:
            popDensity = int(input("Give the population density (1-100) of "
                                   "the imaginary world. As a guideline, the "
                                   "average population density in the world is"
                                   " about 15 per square kilometer: "))
            if popDensity not in range(1, 101):
                print("Please choose a number between 1 and 100. \n")
                populationDensity()
            else:
                print("\n")
                time.sleep(1)
                return popDensity
        except ValueError:
            print("Please give a valid number.\n")


# ask for the amount of days the simulation will be running
def infectionDays():
    while True:
        try:
            inDays = int(input("Give a whole number between 1 and 365. That"
                               " determines how many days of the year the "
                               "simulation will run. Using a high number "
                               "might take a longer time to complete: "))
            if inDays not in range(1, 366):
                print("Please choose a number between 1 and 365. \n")
                infectionDays()
            else:
                print("\n")
                time.sleep(1)
                return inDays
        except ValueError:
            print("Please give a valid number.\n")


# ask for the severity of the virus
def virusSeverity():
    virus = input("Give the severity of the virus. Easy(e), medium(m) "
                  "or hard(h). It determines how effective the virus "
                  "is at infecting people: ").lower()
    print("\n")
    if virus == "easy" or virus == "e":
        virusInt = 0.90
        print("The virus will now be less effective at infecting.\n\n")
        time.sleep(1)
        return virusInt
    elif virus == "medium" or virus == "m":
        virusInt = 0.80
        print("The virus will now be average at infecting.\n\n")
        time.sleep(1)
        return virusInt
    elif virus == "hard" or virus == "h":
        virusInt = 0.70
        print("The virus will now be effective at infecting.\n\n")
        time.sleep(1)
        return virusInt
    else:
        print("Please give a valid severity from the choises given. \n")
        virusSeverity()


# ask if there is a chance for a vaccine
def vaccineCheck():
    vaccine = False
    vaccineChance = input("Is there a chance for a vaccine to be created? "
                          " In the case of yes, there will be a 0.01 chance "
                          " of a vaccine be created per infected person."
                          " Y or N: ").lower()
    print("\n")
    if vaccineChance == "no" or vaccineChance == "n":
        print("No vaccine will be created in the simulation now. \n\n")
        time.sleep(1)
        return vaccine
    elif vaccineChance == "yes" or vaccineChance == "y":
        print("A vaccine will now be created in the simulation. \n\n")
        vaccine = True
        time.sleep(1)
        return vaccine
    else:
        print("Please choose between YES and NO.\n")
        vaccineCheck()


# make it all happen
class simulationClass ():

    # arg1 = populationAmount, arg2 = popDensity arg3 = infectionDays
    # arg4 = virusSeverity and arg5 = vaccineCheck
    def __init__(self, arg1, arg2, arg3, arg4, arg5):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.arg4 = arg4
        self.arg5 = arg5

# set some variables that we need
    def simulation(self, arg1, arg2, arg3, arg4, arg5):
        infected = []
        counter = 0
        chance = 1000
        start = time.time()

        print("Simulation in progress...\n")
        time.sleep(1)

        # for each day, see if the infection spreads and if it does,
        # add it to the infected list.
        for counter in range(arg3):
            time.sleep(0.2)
            viHit = random.randint(1, chance)
            print("Day " + str(counter) + ". The amount of "
                  "infected: " + str(len(infected)))
            counter += 1

            # if the length of the infected list is equal or greater than
            # population amount, stop looping.
            if len(infected) >= arg1:
                time.sleep(1)
                break
            if viHit in range(1, arg2):
                infected.append("infected")
                print("The infection spreads!")
                vaHit = random.randint(1, 1000)

                # for each infection, alter the chance of next infection
                # happening. virus severity affects this.
                chance = np.fix(chance * arg4 + 2)

                # iterate through infection list and see if more happen.
                for i in infected:
                    extraVhit = random.randint(1, chance)
                    if extraVhit in range(1, 2):
                        infected.append("infected")
                        vaHit = random.randint(1, 1000)
                        if arg5 is True:
                            break

                # if vaccine is True, see if a vaccine is created.
                if arg5 is True:
                    if vaHit == 1:
                        time.sleep(1)
                        print("A vaccine was created!\n")
                        time.sleep(1)
                        break

        # if there are more infections than population, set infections to
        # max population as it is just silly to have more infections than
        # there is population.
        if len(infected) >= arg1:
            average = np.around(arg1 / arg3, decimals=1)
            amount = arg1
            print("\n\n")

            # print out some stats about the simulation
            print("{} of {} humans were infected in {} "
                  "days.".format(str(amount), str(arg1), str(counter)))
            print("On average {} infections happened "
                  "per day.".format(str(average)))
            print("The simulation took "
                  "{0:0.1f} seconds.\n".format(time.time() - start))
            time.sleep(1)
        else:
            average = np.around(len(infected) / arg3, decimals=1)
            amount = len(infected)
            print("\n\n")
            print("{} of {} humans were infected in {} "
                  "days.".format(str(amount), str(arg1), str(counter)))
            print("On average {} infections happened "
                  "per day.".format(str(average)))
            print("The simulation took "
                  "{0:0.1f} seconds.\n".format(time.time() - start))
            time.sleep(1)

        # I like statistics so make a pie chart for the sake of it
        plt.style.use('ggplot')
        healthy = arg1 - amount

        # some data for the chart and visual effects
        labels = "Infected", "Healthy"
        sizes = []
        sizes.append(amount)
        sizes.append(healthy)
        colors = ["Red", "Green"]
        explode = (0.2, 0)

        # determine the plot
        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=160)
        plt.legend(labels, loc="best")
        plt.axis("equal")
        plt.title("Total Population of the Infection Simulation")
        plt.show()


# simulation exit
def exit():
    while True:
        try:
            answer = input("Do you wish to exit the simulation? "
                           "Y or N: ").lower()
            print("\n")
            if answer == "yes" or answer == "y":
                return True
            if answer == "no" or answer == "n":
                return False
        except ValueError:
            print("Please give a valid number.\n")


if __name__ == "__main__":
    main()
