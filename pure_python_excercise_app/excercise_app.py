#excercise App made with pure Python in autumn 2018 by https://github.com/PetraSil
import excercise_app_gui as ui

class Values():

    def __init__(self, weight, height, goal, time):

        self.weight = weight
        self.height = height
        self.goal = goal
        self.time = time

    #set default/example values to load with
    def ask_values(self):

        self.weight = 70
        self.height = 180
        self.goal = 2
        self.time = 10

        return ui.Gui(self.weight, self.height, self.goal, self.time).appGui()
        
    def return_info(self):

        return ("\nHow much one needs to excercise to lose weight varies from person to person and\n" 
            "body composition matters, so these are only very rough estimates. As an example,\n"
            "an average person needs to burn nearly 8000 calories in the span of 7 days, "
            "\nif they wish to lose 1kg in those 7 days with excercise alone.\n"
            "\nWe will now calculate some options for you to choose from with some funky math!\n")


class Calculate(Values):

    def bmi(self):

        return self.weight / ((self.height / 100)**2)

    def average_loss(self):

        return self.goal / self.time

    def inform(self):

        return (f"\nWith your BMI, {round(self.bmi(), 2)}, and your goal of losing {self.goal} "
              f"kilos in {self.time} days,\n on average, "
              f"you need to lose {round(self.average_loss(),3)} kilos per day.\n")

    def turn_to_grams(self):

        return self.average_loss() * 1000

    #give each BMI category a multiplier as current weight directly affects weight loss amount
    def calculate_effort(self):

        #some default for weird bmi values that should not happen
        if self.bmi() <= 9.99 or self.bmi() >= 41:
            return self.turn_to_grams() * 1.0 
        #severely underweight
        elif self.bmi() > 9.99 and self.bmi() < 15:
            return self.turn_to_grams() * 2.2
        #underweight
        elif self.bmi() > 14.99 and self.bmi() < 18.6:
            return self.turn_to_grams() * 1.7
        #average weight
        elif self.bmi() > 18.5 and self.bmi() < 25:
            return self.turn_to_grams() * 1.0
        #overweight
        elif self.bmi() > 24.99 and self.bmi() < 30:
            return self.turn_to_grams() * 0.3
        #severely overweight
        elif self.bmi() > 29.9 and self.bmi() < 41:
            return self.turn_to_grams() * 0.1

    #To lose 0.001kg (1 gram) a day takes about (very roughly!) 8 calories burned,
    #so that's my guideline in the upcoming calculations.
    #Also, we presume decent effort when it comes to doing these sports.
    def calculate_running(self):

        #running burns about 12 calories per minute (0.076 * weight in kg * 2.25)
        #calculate sport specific time and effort
        time_needed = round((((((0.076 * self.weight * 2.25 * self.calculate_effort()) / 12) / 60)
                              / self.average_loss()) / self.time), 1)

        running_hours = 0
        while (time_needed - 1) >= running_hours:
            running_hours += 1

        running_minutes = int((time_needed - running_hours) * 60)

        return running_hours, running_minutes

    def calculate_cycling(self):

        #cycling burns about 10 calories per minute (0.076 * weight in kg * 2.25)
        #calculate sport specific time and effort
        time_needed = round((((((0.076 * self.weight * 2.25 * self.calculate_effort()) / 10) / 60)
                              / self.average_loss()) / self.time), 1)

        cycling_hours = 0
        while (time_needed - 1) >= cycling_hours:
            cycling_hours += 1

        cycling_minutes = int((time_needed - cycling_hours) * 60)

        return cycling_hours, cycling_minutes

    def calculate_swimming(self):

        #swimming burns about 9 calories per minute (0.076 * weight in kg * 2.25)
        #calculate sport specific time and effort
        time_needed = round((((((0.076 * self.weight * 2.25 * self.calculate_effort()) / 9) / 60)
                              / self.average_loss()) / self.time), 1)

        swimming_hours = 0
        while (time_needed - 1) >= swimming_hours:
            swimming_hours += 1

        swimming_minutes = int((time_needed - swimming_hours) * 60)

        return swimming_hours, swimming_minutes

    def calculate_climbing(self):

        #climbing burns about 8 calories per minute (0.076 * weight in kg * 2.25)
        #calculate sport specific time and effort
        time_needed = round((((((0.076 * self.weight * 2.25 * self.calculate_effort()) / 8) / 60)
                              / self.average_loss()) / self.time), 1)

        climbing_hours = 0
        while (time_needed - 1) >= climbing_hours:
            climbing_hours += 1

        climbing_minutes = int((time_needed - climbing_hours) * 60)

        return climbing_hours, climbing_minutes

    def calculate_weight_lifting(self):

        #weight lifting about 6 calories per minute (0.076 * weight in kg * 2.25)
        #calculate sport specific time and effort
        time_needed = round((((((0.076 * self.weight * 2.25 * self.calculate_effort()) / 6) / 60)
                              / self.average_loss()) / self.time), 1)

        weight_hours = 0
        while (time_needed - 1) >= weight_hours:
            weight_hours += 1

        weight_minutes = int((time_needed - weight_hours) * 60)

        return weight_hours, weight_minutes

    def calculate_walking(self):

        #walking roughly burns 5 calories per minute (0.076 * weight in kg * 2.25)
        #calculate sport specific time and effort
        time_needed = round((((((0.076 * self.weight * 2.25 * self.calculate_effort()) / 5) / 60)
                              / self.average_loss()) / self.time), 1)

        walking_hours = 0
        while (time_needed - 1) >= walking_hours:
            walking_hours += 1

        walking_minutes = int((time_needed - walking_hours) * 60)

        return walking_hours, walking_minutes


if __name__ == '__main__':
    Values(0, 0, 0, 0).ask_values()