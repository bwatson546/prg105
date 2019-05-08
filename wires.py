import tkinter
import tkinter.messagebox
import pickle


# game start
class GameGUI:
    def __init__(self, master):
        # Open nonsense repository for opening shenanigans in later playthroughs
        try:
            fun_file = open("nonsense.txt", 'w')
            self.nonsense = pickle.load(fun_file)
            fun_file.close()
        except (FileNotFoundError, IOError):
            self.nonsense = {}

        self.master = master
        self.master.title("WIRES")

        # variables
        self.fname = tkinter.StringVar()
        self.lname = tkinter.StringVar()
        self.age = tkinter.StringVar()
        self.zod = tkinter.StringVar()
        self.info = tkinter.StringVar()
        self.conf = 0

        # create frames
        self.top_frame = tkinter.Frame(self.master)
        self.bottom_frame = tkinter.Frame(self.master)

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
        self.info_conf.pack(side='top')

        # buttons
        self.conf_but = tkinter.Button(self.bottom_frame, text="confirm", command=self.confirm)
        self.quit_but = tkinter.Button(self.bottom_frame, text="leave", command=self.master.destroy)

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
        fname = self.fname_entry.get()
        lname = self.lname_entry.get()
        age = self.age_entry.get()
        zod = self.zod_entry.get()
        # Make one press show the info, and the next run the game
        if self.conf == 0:
            self.conf += 1
            self.info.set('Your name is ' + str(fname) + str(lname) + '.\nYou are ' + str(age) + ' years old.\nYour star sign is ' + str(zod) + '.\nIf this is correct, please press confirm again.\n')
        elif self.conf == 1:
            self.nonsense[fname] = lname, age, zod
            outfile = open('nonsense.txt', 'w')
            pickle.dump(self.nonsense, outfile)
            outfile.close()
            _ = BeginGUI(self.master)

        # GAME MECHANIC: self.conf also tracks meta nonsense, adding to it at certain story points.
        else:
            self.info.set('NONSENSE PLACEHOLDER')


class BeginGUI:
    def __init__(self, master):
        # I am definitely going to need a nonsense repository to store values
        try:
            fun_file = open("nonsense.txt", 'w')
            self.nonsense = pickle.load(fun_file)
            fun_file.close()
        except (FileNotFoundError, IOError):
            self.nonsense = {}

        self.begin = tkinter.Toplevel(master)
        self.begin.title('AGREEMENT')

        # variables here

        # the warning
        self.warn_frame = tkinter.Frame(self.begin)
        self.warn_frame_label = tkinter.Label(self.begin, text='All decisions you are about to make are final.\nThere is no saving in this game.\nThere is no back button.\nIf you wish to make another choice,\nyou will have to make all of your choices again.\nDo you understand this?')
        self.warn_frame_label.pack(side='top')
        self.warn_frame.pack()

        # Button frame
        self.button_frame = tkinter.Frame(self.begin)

        # Buttons
        self.accept_button = tkinter.Button(self.button_frame, text='I do', command=self.scene1)
        self.decline_button = tkinter.Button(self.button_frame, text='I don\'t', command=self.back)

        # packin'
        self.accept_button.pack()
        self.decline_button.pack()
        self.button_frame.pack()

    def scene1(self):
        return

    def back(self):
        return


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
