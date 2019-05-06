import tkinter
import tkinter.messagebox
import pickle

# game start
class GameGUI:
    def __init__(self, start):
        self.start = start
        self.start.title("WIRES")

        # variables
        self.fname = tkinter.StringVar()
        self.lname = tkinter.StringVar()
        self.age = tkinter.StringVar()
        self.zod = tkinter.StringVar()
        self.info = tkinter.StringVar()
        self.conf = 0

        # create frames
        self.top_frame = tkinter.Frame(self.start)
        self.bottom_frame = tkinter.Frame(self.start)

        # top frame widgets, info entry
        self.fname_label = tkinter.Label(self.top_frame, text="please enter your given name.")
        self.fname_entry = tkinter.Entry(self.top_frame, width="12")
        self.lname_label = tkinter.Label(self.top_frame, text="please enter your surname.")
        self.lname_entry = tkinter.Entry(self.top_frame, width="12")
        self.age_label = tkinter.Label(self.top_frame, text="please enter your age.")
        self.age_entry = tkinter.Entry(self.top_frame, width="12")
        self.zod_label = tkinter.Label(self.top_frame, text="please enter your zodiac sign.")
        self.zod_entry = tkinter.Entry(self.top_frame, width="12")

        # restate entered info
        self.info_conf = tkinter.Label(self.top_frame, textvariable=self.info)

        # pack it up
        self.fname_label.pack(side="top")
        self.fname_entry.pack(side="top")
        self.lname_label.pack(side="top")
        self.lname_entry.pack(side="top")
        self.age_label.pack(side="top")
        self.age_entry.pack(side="top")
        self.zod_label.pack(side="top")
        self.zod_entry.pack(side="top")

        # buttons
        self.conf_but = tkinter.Button(self.bottom_frame, text="confirm", command=self.confirm)
        self.quit_but = tkinter.Button(self.bottom_frame, text="leave", command=self.start.destroy)

        # button box, pack 'em in it
        self.conf_but.pack(side="left")
        self.quit_but.pack(side="right")

        # Frame packin'
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Main loop
        tkinter.mainloop()

        # confirms the entry, shows it to the player, asks for additional confirmation
    def confirm(self):
        fname = str(self.fname_entry.get())
        lname = str(self.lname_entry.get())
        age = str(self.age_entry.get())
        zod = str(self.zod_entry.get())

        # Make one press show the info, and the next run the game
        if self.conf == 0:
            self.conf += 1
            self.info.set('Your name is ' + fname + lname + '. You are ' + age + ' years old. Your star sign is ' + zod + '. If this is correct, please press Confirm again.')
        elif self.conf == 1:
            _ = BeginGUI(self.start)

        # GAME MECHANIC: self.conf also tracks meta nonsense, adding to it at certain story points.
        else:
            self.info.set('NONSENSE PLACEHOLDER')


class BeginGUI:
    def __init__(self, start):
        # I am definitely going to need a nonsense repository to store values
        try:
            fun_file = open("nonsense.dat", 'rw')
            self.nonsense = pickle.load(fun_file)
            fun_file.close()
        except (FileNotFoundError, IOError):
            self.nonsense = {}






def main():
    # create a window
    root = tkinter.Tk()
    # call the GUI and send it the root menu
    # use _ as variable name because the variable will not be needed after instantiating GUI
    # the GUI itself will handles the remaining program logic
    _ = GameGUI(root)
    # control the mainloop from main instead of the class
    root.mainloop()


main()
