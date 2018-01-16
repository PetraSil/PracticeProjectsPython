# Simply some practice with matplotlib.
# I imported the average running data for each month
# for the last three years to play with.

import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons

# running date transformed into lists
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
year_2015 = [7.01, 6.55, 6.51, 6.48, 6.45, 6.39, 6.38, 6.40, 6.35, 6.34,
             6.33, 6.30]
year_2016 = [6.30, 6.28, 6.20, 6.19, 6.16, 6.11, 6.10, 6.05, 5.58, 5.55,
             5.54, 5.52]
year_2017 = [6.01, 5.50, 5.51, 5.49, 5.45, 5.39, 5.38, 5.37, 5.35, 5.35,
             5.30, 5.29]

# calculate the average of the past three years
all_years = [(year_2015), (year_2016), (year_2017)]
average_setup = [sum(i) / len(i) for i in zip(*all_years)]
average = [round(elem, 2) for elem in average_setup]

# determine the syle of the plot
plt.style.use("bmh")

# determine and set what the plot looks like and set variables
fig, ax = plt.subplots()
lineAverage, = ax.plot(average, visible=False, lw=1, color="b", label="Avg")
line2015, = ax.plot(year_2015, lw=1, color="r", label="2015")
line2016, = ax.plot(year_2016, lw=1, color="g", label="2016")
line2017, = ax.plot(year_2017, lw=1, color="y", label="2017")
lines = [lineAverage, line2015, line2016, line2017]
plt.subplots_adjust(left=0.3)

# name the labels
plt.xlabel("Month, January - December")
plt.ylabel("Average min/km")
plt.title("5k Running 2015 - 2017")

# set up the checkbox where you can choose what year to show
box = plt.axes([0.05, 0.4, 0.15, 0.2])
labels = [str(line.get_label()) for line in lines]
visibility = [line.get_visible() for line in lines]
check = CheckButtons(box, labels, visibility)


# function to make the checkbox to actually work
def click(label):
    index = labels.index(label)
    lines[index].set_visible(not lines[index].get_visible())
    plt.draw()


check.on_clicked(click)
plt.legend()
plt.show()
