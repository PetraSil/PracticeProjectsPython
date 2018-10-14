import excercise_app as ex
import tkinter as tk
from tkinter import messagebox
import sys

startMessage = False

class Gui(ex.Calculate):
    
    #simple function to delete the placeholder text from entry-widgets
    def clearText(self, event, entry):
        entry.delete(0, tk.END)

    #Check for correct input and reset examples if need be       
    def newValues(self):

        try:
            int(self.inputWeight.get()) and int(self.inputHeight.get()) and int(self.inputGoal.get()) and int(self.inputTime.get())

        except:
            messagebox.showerror("Error", "Please use only whole numbers.")

        else:
            self.newWeight = self.inputWeight.get()
            self.newHeight = self.inputHeight.get()
            self.newGoal = self.inputGoal.get()
            self.newTime = self.inputTime.get()

            #this is needed to destroy the old window as only way to update values is to create a new window
            self.master.destroy()

            return Gui(int(self.newWeight), int(self.newHeight), int(self.newGoal), int(self.newTime)).appGui()
            
    def quit(self):

        #hard exit
        return sys.exit(0)


    def appGui(self):

        #we only want beginning information once
        self.startMessage = False

        #create main window
        self.master = tk.Tk()
        self.master.withdraw()
        self.master = tk.Toplevel(bg="black")
        self.master.geometry("503x650+400+0")
        self.master.lift()
        self.master.title("Copyright 2018, Petra Silavuori, All rights reserved")
        self.master.resizable(width=False, height=False)
    
        #create top banner
        self.bgImage=tk.PhotoImage(file="climb.gif")
        self.banner = tk.Label(self.master, image=self.bgImage)
        self.banner.grid(row=0, column=0, sticky="nesw", columnspan=2)

        #create and style label
        self.title = tk.Label(self.master, text="THE ODD WORKOUT CALCULATOR", bg="black", fg="white")
        self.title.grid(row=1, column=0, sticky="ew", columnspan=2)
        self.title.configure(font=("Arial", 15, "bold"))

        #print the general information
        self.intro = tk.Label(self.master, text=ex.Values.return_info(self), bg="white")
        self.intro.grid(row=2, column=0, sticky="ew", columnspan=2)
        self.intro.configure(font=("Calibri", 10))

        #print the info for the users BMI below the input area
        self.info = tk.Label(self.master, text=ex.Calculate.inform(self), bg="white", fg="black")
        self.info.grid(row=8, column=0, sticky="ew", columnspan=2)
        self.info.configure(font=("Calibri", 11, "bold"), bd=3, relief="solid")

        #entry field for weight
        self.inputWeight = tk.Entry(self.master, highlightbackground="black", highlightthickness=3)
        self.inputWeight.insert(0, "    Enter weight in KG. E.g. 70")
        self.inputWeight.grid(row=4, column=0, sticky="ew", columnspan=1)
        self.inputWeight.configure(font=("Calibri", 11))
        #placeholder text removed with an event
        self.inputWeight.bind("<Button-1>", lambda event: self.clearText(event, self.inputWeight))

        self.weightLabel = tk.Label(self.master, text="WEIGHT IN KG", bg="black", fg="white")
        self.weightLabel.grid(row=4, column=1, sticky="ew", columnspan=1, padx=30)
        self.weightLabel.configure(font=("Calibri", 12))

        #entry field for height
        self.inputHeight = tk.Entry(self.master, highlightbackground="black", highlightthickness=3)
        self.inputHeight.insert(0, "    Enter height in CM. E.g. 180")
        self.inputHeight.grid(row=5, column=0, sticky="ew", columnspan=1)
        self.inputHeight.configure(font=("Calibri", 11))
        self.inputHeight.bind("<Button-1>", lambda event: self.clearText(event, self.inputHeight))

        self.heightLabel = tk.Label(self.master, text="HEIGHT IN CM", bg="black", fg="white")
        self.heightLabel.grid(row=5, column=1, sticky="ew", columnspan=1, padx=30)
        self.heightLabel.configure(font=("Calibri", 12))

        #entry field for goal
        self.inputGoal = tk.Entry(self.master, highlightbackground="black", highlightthickness=3)
        self.inputGoal.insert(0, "    Enter goal loss in KG. E.g. 2")
        self.inputGoal.grid(row=6, column=0, sticky="ew", columnspan=1)
        self.inputGoal.configure(font=("Calibri", 11))
        self.inputGoal.bind("<Button-1>", lambda event: self.clearText(event, self.inputGoal))

        self.kilosLabel = tk.Label(self.master, text="LOSS IN KG", bg="black", fg="white")
        self.kilosLabel.grid(row=6, column=1, sticky="ew", columnspan=1, padx=30)
        self.kilosLabel.configure(font=("Calibri", 12))

        #entry field for time
        self.inputTime = tk.Entry(self.master, highlightbackground="black", highlightthickness=3)
        self.inputTime.insert(0, "    Enter goal time in DAYS. E.g. 10")
        self.inputTime.grid(row=7, column=0, sticky="ew", columnspan=1)
        self.inputTime.configure(font=("Calibri", 11))
        self.inputTime.bind("<Button-1>", lambda event: self.clearText(event, self.inputTime))

        self.timeLabel = tk.Label(self.master, text="TIME IN DAYS", bg="black", fg="white")
        self.timeLabel.grid(row=7, column=1, sticky="ew", columnspan=1, padx=30)
        self.timeLabel.configure(font=("Calibri", 12))

        #button to calculate values, it will also close the old window and open a new one
        self.button2 = tk.Button(self.master, text="CALCULATE", command=self.newValues, bg="black", fg="white")
        self.button2.grid(row=3, column=0, sticky="ew", columnspan=1)
        self.button2.configure(font=("Arial", 12, "bold"))
        self.button2.config(cursor="exchange", bd=5, relief="raised")
        #self.button2.grid(column=0, row=9)

        #calculate the values in the main file
        self.e1 = tk.Label(self.master, text="\nRUNNING PER DAY (Hours, Minutes): "+str(ex.Calculate.calculate_running(self)).strip("()"), bg="black", fg="white", anchor="w", padx=120)
        self.e1.grid(row=9, column=0, sticky="ew", columnspan=100)
        self.e1.configure(font=("Arial", 10, "bold"))

        self.e2 = tk.Label(self.master, text="WALKING PER DAY (Hours, Minutes): "+str(ex.Calculate.calculate_walking(self)).strip("()"), bg="black", fg="white", anchor="w", padx=120)
        self.e2.grid(row=10, column=0, sticky="ew", columnspan=100)
        self.e2.configure(font=("Arial", 10, "bold"))

        self.e3 = tk.Label(self.master, text="CLIMBING PER DAY (Hours, Minutes): "+str(ex.Calculate.calculate_climbing(self)).strip("()"), bg="black", fg="white", anchor="w", padx=120)
        self.e3.grid(row=11, column=0, sticky="ew", columnspan=100)        
        self.e3.configure(font=("Arial", 10, "bold"))

        self.e4 = tk.Label(self.master, text="SWIMMING PER DAY (Hours, Minutes): "+str(ex.Calculate.calculate_swimming(self)).strip("()"), bg="black", fg="white", anchor="w", padx=120)
        self.e4.grid(row=12, column=0, sticky="ew", columnspan=100)        
        self.e4.configure(font=("Arial", 10, "bold"))

        self.e5 = tk.Label(self.master, text="WEIGHTS PER DAY (Hours, Minutes): "+str(ex.Calculate.calculate_weight_lifting(self)).strip("()")+"\n", bg="black", fg="white", anchor="w", padx=120)
        self.e5.grid(row=13, column=0, sticky="ew", columnspan=100)        
        self.e5.configure(font=("Arial", 10, "bold"))

        #hard quit the app
        self.button = tk.Button(self.master, text="QUIT", command=self.quit, bg="black", fg="white")
        self.button.grid(row=3, column=1, sticky="ew", columnspan=1)        
        self.button.configure(font=("Arial", 12, "bold"))
        self.button.config(cursor="X_cursor", bd=5, relief="raised")

        #Ensure the program closes properly if window is closed without using the QUIT button.
        self.master.protocol("WM_DELETE_WINDOW", self.quit)


        global startMessage

        if startMessage == False:
            messagebox.showinfo("IMPORTANT INFORMATION!", "This calculator presumes average level effort and that your calorie intake does not outweight "
                "your calorie outtake and vice versa. "
                "If you need advice with your nutrition then consult a professional "
                "as this calculator does not help you with that. This calculator will also default to average values if your BMI is not realistic e.g. 10, "
                "as someone with that low of a BMI is either dead or severely ill and in no shape to excercise.\n"
                "\nA good rule to remember is that most weight is lost and gained in the kitchen."
                "So keep your goals realistic and rememeber that this is app was only made by " 
                "yours truly for fun and in no way is responsible for anything that might happen "
                "when you excercise.")

            startMessage = True

        return self.master.mainloop() 