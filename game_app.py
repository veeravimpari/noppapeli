from tkinter import *
import random


class Application(Frame) :
    ''' GUI '''

    def __init__(self, master):
        Frame.__init__(self, master, pady=30, padx=20)
        self.pack()

        self.main_label = Label(self, text="The Dice Generator 2000", font=('courier new', 26, 'bold'), pady=10)
        self.main_label.pack()
        #the label that keeps the player informed
        self.game_label = Label(self, fg="orange", text="Are you ready?", font=('courier new',20))
        self.game_label.pack(side=TOP)

        #create the quit button
        self.quit_button = Button(self, text="Quit", command=root.destroy)
        self.quit_button.pack(side=BOTTOM)

        #call the starOver function
        self.startOver()


    def startOver(self):
        #button for starting the game
        self.start_button = Button(self, text="Play", command=self.start)
        self.start_button.pack()


    def start(self):

        #labels
        self.game_label.config(text='Guess the sum of two six sided dice. \n Lets play!', fg="orange", font=('courier new',20))
        self.instruction_label = Label(self, text="Insert your guess to the field and hit enter to roll the dice", font=('courier new',16))
        self.instruction_label.pack(side=BOTTOM)


        # Destroy the start button
        self.start_button.destroy()

        # Create the entry field
        self.user_entry = Entry(self)
        self.user_entry.pack()

        #the dices
        self.dice1 = random.randint(1,6)
        self.dice2 = random.randint(1,6)
        self.dice = self.dice1 + self.dice2

        #the variable where the contents of the entry widget will be stored
        self.contents = StringVar()
        #set the variable to some value
        self.contents.set(0)

        #tell the entry widget to use this variable
        self.user_entry["textvariable"] = self.contents
        #bind the entry widget to function self.play
        self.user_entry.bind('<Key-Return>', self.play)


    def play(self, event):

        #destroy the instruction label
        self.instruction_label.destroy()

        #the total of the two dice
        t = self.dice
        #the player's guess
        i = self.contents.get()

        if i.isdigit():

            if t == int(i):
                self.game_label.config(text="You guessed \n" + i + "\nand the result was \n" + str(t) + "\n Congratulations, you won! \n Click Play to start a new round!",
                                       fg="green", font=('courier new',20,'bold'))
                #destroy the entry field
                self.user_entry.destroy()
                #call the star over button
                self.startOver()
            else:
                self.game_label.config(text="You guessed \n" + i + "\n but the result was \n" + str(t) + "\n Sorry, you lost. \n Click play to start a new round!" ,
                                       fg="blue", font=('courier new',20,'bold'))
                #destroy the entry field
                self.user_entry.destroy()
                #call the start over button
                self.startOver()
        else:
            self.game_label.config(text="Invalid input, please try again. \n Tip: This time, try guessing a number between 2 and 12.", fg="red", font=('courier new',20))
            #clear the input field
            self.user_entry.delete(0, 'end')


#create window
root = Tk()
root.title("The Dice Game")
root.geometry("700x500")
root.configure(background='blue', pady=80)

app = Application(master=root)

root.mainloop()



