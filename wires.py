import tkinter
import tkinter.messagebox
import random
import pickle


# game start
class GameGUI:
    def __init__(self, master):
        try:
            id_file = open("id_file.dat", 'rb')
            self.id = pickle.load(id_file)
            id_file.close()
        except (FileNotFoundError, IOError):
            self.id = {}

        self.master = master
        self.master.title("WIRES")

        # variables
        self.fname = tkinter.StringVar()
        self.lname = tkinter.StringVar()
        self.age = tkinter.StringVar()
        self.gender = tkinter.IntVar()
        self.info = tkinter.StringVar()
        global conf
        conf = 0
        global gend
        gend = 0
        global age
        age = 0

        self.gender.set(1)

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

        # gender zone (radio buttons, etc.)
        self.gen_label = tkinter.Label(self.top_frame, text="please identify your gender.")
        self.gen_male = tkinter.Radiobutton(self.top_frame, text='Male', variable=self.gender, value=1)
        self.gen_female = tkinter.Radiobutton(self.top_frame, text='Female', variable=self.gender, value=2)
        self.gen_nonbinary = tkinter.Radiobutton(self.top_frame, text='Other/Neutral/Nonbinary', variable=self.gender, value=3)

        # restate entered info
        self.info_conf = tkinter.Label(self.top_frame, textvariable=self.info)

        # pack it up
        self.fname_label.pack(side="top")
        self.fname_entry.pack(side="top")
        self.lname_label.pack(side="top")
        self.lname_entry.pack(side="top")
        self.age_label.pack(side="top")
        self.age_entry.pack(side="top")
        self.gen_label.pack(side="top")
        self.gen_male.pack(side="top", anchor="w")
        self.gen_female.pack(side="top", anchor="w")
        self.gen_nonbinary.pack(side="top", anchor="w")
        # self.gen_machine.pack(side="top", anchor="w")
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
        global gend
        global age
        fname = self.fname_entry.get()
        lname = self.lname_entry.get()
        age = self.age_entry.get()
        gender = self.gender.get()
        if gender == 1:
            gender = 'MALE'
            gend = 1
        elif gender == 2:
            gender = 'FEMALE'
            gend = 2
        elif gender == 3:
            gender = 'NOT INTERESTED IN A GENDER BINARY'
            gend = 3
        else:
            gender = 'A CHEATER'
            gend = random.randrange(1, 3)

        # Make one press show the info, and the next run the game
        global conf
        if conf == 0:
            conf += 1
            self.info.set('Your name is ' + str(fname).upper() + ' ' + str(lname).upper() + '.\nYou are ' + str(age) + ' years old.\nYou are ' + str(gender).upper() + '.\nIf this is correct, please\npress confirm again.\n\nIf it is not, correct it,\nand it will display properly\nin game.\n')
        elif conf == 1:
            _ = BeginGUI(self.master)
        elif conf == 2:
            _ = A2S1(self.master)
        elif conf == 3:
            _ = A3S1(self.master)
        elif conf == 4:
            tkinter.messagebox.showinfo('', 'THE WIRES GOT THE BEST OF THEM')
        # GAME MECHANIC: global conf tracks playthroughs, moving on to the next story
        else:
            self.info.set('NONSENSE PLACEHOLDER')


class BeginGUI:
    def __init__(self, master):
        # I am definitely going to need a nonsense repository to store values

        self.begin = tkinter.Toplevel(master)
        self.begin.title('AGREEMENT')

        # variables here

        # the warning
        self.warn_frame = tkinter.Frame(self.begin)
        self.warn_frame_label = tkinter.Label(self.begin, text='All decisions you are about to make are final.\nThere is no saving in this game.\nThere is no back button.\nIf you wish to make another choice,\nyou will have to make all of your choices again.\nIf you are not careful, the Wires will get the best of you.\nDo you understand this?')
        self.warn_frame_label.pack(side='top')
        self.warn_frame.pack()

        # Button frame
        self.button_frame = tkinter.Frame(self.begin)

        # Buttons
        self.accept_button = tkinter.Button(self.button_frame, text='I do', command=self.transition)
        self.decline_button = tkinter.Button(self.button_frame, text='I don\'t', command=self.back)

        # packin'
        self.accept_button.pack(side='left')
        self.decline_button.pack(side='right')
        self.button_frame.pack(side='bottom')

    def s1(self):
        _ = Scene1(self.begin)

    def clear_window(self):
        self.begin.withdraw()

    def transition(self):
        self.s1()
        self.clear_window()

    def back(self):
        self.begin.destroy()


# first scene of the actual game; A king holds court and has to make decisions about important matters. These decisions are kept, and referred to later using if statements.
class Scene1:
    def __init__(self, master):
        self.scene1 = tkinter.Toplevel(master)
        self.scene1.title('AWAKE')

        # variables
        global conf
        global gend
        possess = 0
        monarch = 0
        if gend == 1:
            possess = 'his'
            monarch = 'king'
        if gend == 2:
            possess = 'her'
            monarch = 'queen'
        if gend == 3:
            possess = 'their'
            monarch = 'ruler'

        # text frame
        self.sc1_frame = tkinter.Frame(self.scene1)
        self.sc1_frame_label = tkinter.Label(self.scene1, text='-THE ' + monarch.upper() + ' IN ' + possess.upper() + ' CASTLE-')
        self.sc1_frame_text = tkinter.Label(self.scene1, text='You are a mighty ' + monarch + ', ruling over your subjects.\nToday, they come to you with their petty squabbles,\neager to hear your divine wisdom\nto solve their problems.\n')
        self.sc1_frame_label.pack(side='top')
        self.sc1_frame_text.pack(side='top', anchor='w')
        self.sc1_frame.pack(side='top')

        # Button frame
        self.button_frame = tkinter.Frame(self.scene1)

        # buttons
        self.op1_button = tkinter.Button(self.button_frame, text='LET THEM COME', command=self.transition1)
        self.op2_button = tkinter.Button(self.button_frame, text='MAYBE... NOT TODAY', command=self.transition2)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.back)

        self.op1_button.pack(side='left')
        self.op2_button.pack(side='left')
        self.quit_button.pack(side='right')

        self.button_frame.pack(side='bottom')

    def sc1_op1(self):
        _ = Scene2a(self.scene1)

    def sc1_op2(self):
        _ = Scene2b(self.scene1)

    def clear_window(self):
        self.scene1.withdraw()

    def transition1(self):
        self.sc1_op1()
        self.clear_window()

    def transition2(self):
        self.sc1_op2()
        self.clear_window()

    def back(self):
        self.scene1.destroy()


class Scene2a:
    def __init__(self, master):
        self.scene2a = tkinter.Toplevel(master)
        self.scene2a.title('AWAKE')

        # variables
        global conf
        global gend
        possess = 0
        aura = 0
        if gend == 1:
            possess = 'his'
            aura = 'masculine'
        if gend == 2:
            possess = 'her'
            aura = 'feminine'
        if gend == 3:
            possess = 'their'
            aura = 'powerful'

        # text frame
        self.sc2a_frame = tkinter.Frame(self.scene2a)
        self.sc2a_frame_label = tkinter.Label(self.scene2a, text='-YOUR GRACE ASTOUNDS-')
        self.sc2a_frame_text = tkinter.Label(self.scene2a, text='Your subjects meekly crowd before your throne,\ncowed by your ' + aura + ' might.\nThey seem to be having a silent argument;\nwho will be the first to approach ' + possess + ' majesty?\n\nAs amusing as it is, though, it has been going on a bit long...\n')
        self.sc2a_frame_label.pack(side='top')
        self.sc2a_frame_text.pack(side='top', anchor='w')
        self.sc2a_frame.pack(side='top')

        # Button frame
        self.button_frame = tkinter.Frame(self.scene2a)

        # buttons
        self.op1_button = tkinter.Button(self.button_frame, text='PICK ONE', command=self.transition1)
        self.op2_button = tkinter.Button(self.button_frame, text='FORCE THE ISSUE', command=self.transition2)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.back)

        self.op1_button.pack(side='left')
        self.op2_button.pack(side='left')
        self.quit_button.pack(side='right')

        self.button_frame.pack(side='bottom')

    def sc2a_op1(self):
        global rule2
        rule2 = 1
        _ = Scene3a(self.scene2a)

    def sc2a_op2(self):
        global rule2
        rule2 = 2
        _ = Scene3b(self.scene2a)

    def clear_window(self):
        self.scene2a.withdraw()

    def transition1(self):
        self.sc2a_op1()
        self.clear_window()

    def transition2(self):
        self.sc2a_op2()
        self.clear_window()

    def back(self):
        self.scene2a.destroy()


class Scene2b:
    def __init__(self, master):
        self.scene2b = tkinter.Toplevel(master)
        self.scene2b.title('AWAKE')

        # variables
        global conf
        global gend
        monarch = 0
        if gend == 1:
            monarch = 'king'
        if gend == 2:
            monarch = 'queen'
        if gend == 3:
            monarch = 'ruler'

        # text frame
        self.sc2b_frame = tkinter.Frame(self.scene2b)
        self.sc2b_frame_label = tkinter.Label(self.scene2b, text='-YOUR GRACE ABSTAINS-')
        self.sc2b_frame_text = tkinter.Label(self.scene2b, text='You wave your crier away.\nThey bow in understanding, and leave to tell\nthe masses that the ' + monarch + ' is not holding audience today.\nYou hear a quiet groan, quickly stifled,\nas the peasantry leave you be.\n\nPerhaps tomorrow, you will hear their concerns.\n\nPerhaps not.\n')
        self.sc2b_frame_label.pack(side='top')
        self.sc2b_frame_text.pack(side='top', anchor='w')
        self.sc2b_frame.pack(side='top')

        # Button frame
        self.button_frame = tkinter.Frame(self.scene2b)

        # buttons
        self.op1_button = tkinter.Button(self.button_frame, text='PERHAPS', command=self.sc2b_op1)
        self.op2_button = tkinter.Button(self.button_frame, text='PERHAPS NOT', command=self.transition1)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.back)

        self.op1_button.pack(side='left')
        self.op2_button.pack(side='left')
        self.quit_button.pack(side='right')

        self.button_frame.pack(side='bottom')

    @staticmethod
    def sc2b_op1():
        tkinter.messagebox.showinfo('To be honest', 'you really aren\'t feeling it today either...')

    def sc2b_op2(self):
        _ = Scene3c(self.scene2b)

    def clear_window(self):
        self.scene2b.withdraw()

    def transition1(self):
        self.sc2b_op2()
        self.clear_window()

    def back(self):
        self.scene2b.destroy()


class Scene3a:
    def __init__(self, master):
        self.scene3a = tkinter.Toplevel(master)
        self.scene3a.title('AWAKE')

        # variables
        global conf
        global gend
        finger = 0
        possess = 0
        if gend == 1:
            finger = 'strong'
            possess = 'his'
        if gend == 2:
            finger = 'lithe'
            possess = 'her'
        if gend == 3:
            finger = 'sharp'
            possess = 'their'

        # text frame
        self.sc3a_frame = tkinter.Frame(self.scene3a)
        self.sc3a_frame_label = tkinter.Label(self.scene3a, text='-YOU.-')
        self.sc3a_frame_text = tkinter.Label(self.scene3a, text='You extend a ' + finger + ' finger in the direction of a random peasant.\n\n\'You,\'\n\nyou rumble out, voice spreading to fill your hallowed hall.\nYour subject scrambles to collect himself, and scrambles to present his needs.\n\n\'Well y\'see, if it pleases ' + possess + ' grace, here\'s the thing...')
        self.sc3a_frame_label.pack(side='top')
        self.sc3a_frame_text.pack(side='top', anchor='w')
        self.sc3a_frame.pack(side='top')

        # Button frame
        self.button_frame = tkinter.Frame(self.scene3a)

        # buttons
        self.op1_button = tkinter.Button(self.button_frame, text='THIS GOES ON FOR HOURS', command=self.transition1)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.back)

        self.op1_button.pack(side='left')
        self.quit_button.pack(side='right')

        self.button_frame.pack(side='bottom')

    def sc3a_op1(self):
        repeats = random.randrange(7, 15)
        for loop in range(repeats):
            tkinter.messagebox.showinfo('', 'AND HOURS,')
        tkinter.messagebox.showinfo('', 'and hours.')
        _ = Scene4a(self.scene3a)

    def clear_window(self):
        self.scene3a.withdraw()

    def transition1(self):
        self.sc3a_op1()
        self.clear_window()

    def back(self):
        self.scene3a.destroy()


class Scene3b:
    def __init__(self, master):
        self.scene3b = tkinter.Toplevel(master)
        self.scene3b.title('AWAKE')

        # variables
        global conf
        global gend
        monarch = 0
        if gend == 1:
            monarch = 'KING'
        if gend == 2:
            monarch = 'QUEEN'
        if gend == 3:
            monarch = 'RULER'

        # text frame
        self.sc3b_frame = tkinter.Frame(self.scene3b)
        self.sc3b_frame_label = tkinter.Label(self.scene3b, text='-NOW.-')
        self.sc3b_frame_text = tkinter.Label(self.scene3b, text='You clear your throat, a thundering roar that commands the attention of the nervous horde.\nTheir eyes on you, you intone;\n\n\'The last one to speak today, should they displease me, will be executed.\nThe rest will be safe.\'\n\nThis wakes them up neatly, triggering a scramble to the throne.\nFor a while, they desperately try to give their grievances,\nuntil another rumble from your throat demands order.\nAfter this, their petty squabbles invade your ears,\n\none at a time,\n\njust\n\nso\n\nslowly.')
        self.sc3b_frame_label.pack(side='top')
        self.sc3b_frame_text.pack(side='top', anchor='w')
        self.sc3b_frame.pack(side='top')

        # Button frame
        self.button_frame = tkinter.Frame(self.scene3b)

        # buttons
        self.op1_button = tkinter.Button(self.button_frame, text='IT\'S ENOUGH TO DRIVE A ' + monarch + ' MAD', command=self.transition1)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.back)

        self.op1_button.pack(side='left')
        self.quit_button.pack(side='right')

        self.button_frame.pack(side='bottom')

    def sc3b_op1(self):
        tkinter.messagebox.showinfo('', 'and so it does.')
        _ = Scene4b(self.scene3b)

    def clear_window(self):
        self.scene3b.withdraw()

    def transition1(self):
        self.sc3b_op1()
        self.clear_window()

    def back(self):
        self.scene3b.destroy()


class Scene3c:
    def __init__(self, master):
        try:
            id_file = open("id_file.dat", 'rb')
            self.id = pickle.load(id_file)
            id_file.close()
        except (FileNotFoundError, IOError):
            self.id = {}
        self.scene3c = tkinter.Toplevel(master)
        self.scene3c.title('AWAKE')

        # variables
        global conf
        global gend
        monarch = 0
        pronoun = 0
        if gend == 1:
            monarch = 'KING'
            pronoun = 'him'
        if gend == 2:
            monarch = 'QUEEN'
            pronoun = 'her'
        if gend == 3:
            monarch = 'RULER'
            pronoun = 'them'

        # text frame
        self.sc3c_frame = tkinter.Frame(self.scene3c)
        self.sc3c_frame_label = tkinter.Label(self.scene3c, text='-WITHERING-')
        self.sc3c_frame_text = tkinter.Label(self.scene3c, text='You spend your days in quiet contemplation. An eternity of days thinking about the world, your place in it, and your duties. While you consider the role of a ' + monarch + ', you realize; you are in charge of an incredible number of lives. These people would die if you wished it so, and if your rule falters, may die if you don\'t.\n\nThe pressure begins to build during your days of quiet contemplation before, a year after that first day you refused to hold court, you held an official audience, formally abdicating the throne. Your subjects don\'t much mind; unbenownst to you, things went alright for them without any new laws being made for a while. Life moved on while you were trapped in your own mind, wrapped in the wires.\n\nThe reticent liege\'s number was 91.')
        self.sc3c_frame_label.pack(side='top')
        self.sc3c_frame_text.pack(side='top', anchor='w')
        self.sc3c_frame.pack(side='top')

        # Button frame
        self.button_frame = tkinter.Frame(self.scene3c)

        # buttons
        self.op1_button = tkinter.Button(self.button_frame, text='THE WIRES GOT THE BEST OF ' + pronoun.upper() + '.', command=self.transition1)

        self.op1_button.pack(side='left')

        self.button_frame.pack(side='bottom')

    def sc3c_op1(self):
        id1 = 1
        self.id[id1] = '91'
        tkinter.messagebox.showinfo('', 'END')

    def transition1(self):
        self.sc3c_op1()
        global conf
        conf += 1
        outfile = open('id_file.dat', 'wb')
        pickle.dump(self.id, outfile)
        outfile.close()
        self.scene3c.destroy()


class Scene4a:
    def __init__(self, master):
        try:
            id_file = open("id_file.dat", 'rb')
            self.id = pickle.load(id_file)
            id_file.close()
        except (FileNotFoundError, IOError):
            self.id = {}
        self.scene4a = tkinter.Toplevel(master)
        self.scene4a.title('AWAKE')

        # variables
        global conf
        global gend
        monarch = 0
        pronoun = 0
        heshethey = 0
        if gend == 1:
            monarch = 'KING'
            pronoun = 'him'
            heshethey = 'He'
        if gend == 2:
            monarch = 'QUEEN'
            pronoun = 'her'
            heshethey = 'She'
        if gend == 3:
            monarch = 'RULER'
            pronoun = 'them'
            heshethey = 'They'

        # text frame
        self.sc4a_frame = tkinter.Frame(self.scene4a)
        self.sc4a_frame_label = tkinter.Label(self.scene4a, text='-CONSEQUENCE-')
        self.sc4a_frame_text = tkinter.Label(self.scene4a, text='You solve problems as a good ' + monarch + ' does.\nYou listen patiently to your subjects, give thoughtful advice,\ndo your best to improve your kingdom.\n\nBut eventually, inevitably, you make a mistake.\n\nMonths after a solution for a routine problem\nabout grazing territory, the party who received\nthe lesser parcel becomes upset with the victor of the case.\nTheir tempers flare until one dies in a fit of passion.\nThis begins a torrent of hearings, trials, problems,\nconsidering who was at fault, who should have done what,\nuntil eventually, eyes turn on you.\n\n\'The ' + monarch + ' should have known better,\' they said.\n\n\'' + heshethey + ' can\'t be fit to lead if ' + heshethey.lower() + ' got this so wrong,\', came the whispers.\n\nAnd so your reign comes to an abrupt and undeserved end,\nvictim to nothing but a chain of events stemming from a good, fair judgment.\n\nThe people formed a tide, and try as you might to keep yourself above,\nthe wires pulled you under.\n\nThe faithful leader\'s number was 83.')
        self.sc4a_frame_label.pack(side='top')
        self.sc4a_frame_text.pack(side='top', anchor='w')
        self.sc4a_frame.pack(side='top')

        # Button frame
        self.button_frame = tkinter.Frame(self.scene4a)

        # buttons
        self.op1_button = tkinter.Button(self.button_frame, text='THE WIRES GOT THE BEST OF ' + pronoun.upper() + '.', command=self.transition1)

        self.op1_button.pack(side='left')

        self.button_frame.pack(side='bottom')

    def sc4a_op1(self):
        id1 = 1
        self.id[id1] = '83'
        tkinter.messagebox.showinfo('', 'END')

    def transition1(self):
        self.sc4a_op1()
        global conf
        conf += 1
        outfile = open('id_file.dat', 'wb')
        pickle.dump(self.id, outfile)
        outfile.close()
        self.scene4a.destroy()


class Scene4b:
    def __init__(self, master):
        try:
            id_file = open("id_file.dat", 'rb')
            self.id = pickle.load(id_file)
            id_file.close()
        except (FileNotFoundError, IOError):
            self.id = {}
        self.scene4b = tkinter.Toplevel(master)
        self.scene4b.title('AWAKE')

        # variables
        global conf
        global gend
        pronoun = 0
        if gend == 1:
            pronoun = 'him'
        if gend == 2:
            pronoun = 'her'
        if gend == 3:
            pronoun = 'them'

        # text frame
        self.sc4b_frame = tkinter.Frame(self.scene4b)
        self.sc4b_frame_label = tkinter.Label(self.scene4b, text='-TYRANNY-')
        self.sc4b_frame_text = tkinter.Label(self.scene4b, text='Eventually, you stop being able to stomach it all.\n\nThese petty squabbles, these tiny, insignificant issues, are so far beneath your notice.\nThe pressure to hear and solve all of these issues you care absolutely nothing for\nEventually comes to a head when a fight erupts in the markets when\none of your taxmen tried to take his due.\nThe taxman was taken hostage in exchange for more fair taxes, and you responded\n\nby having the whole of the market razed with the people trapped inside.\n\nThe rest of your populace, no longer able to deny your tyranny, took up the cause.\n\nYou aren\'t surprised when you find yourself on the guillotine.\n\nBy the time the day came, honestly, you were already so far beyond caring.\n\nThe wires had already wrapped your soul, squeezing tighter well before the dull blade\nseparated your head from the rest of you.\n\nThe tyrant\'s number was 77.')
        self.sc4b_frame_label.pack(side='top')
        self.sc4b_frame_text.pack(side='top', anchor='w')
        self.sc4b_frame.pack(side='top')

        # Button frame
        self.button_frame = tkinter.Frame(self.scene4b)

        # buttons
        self.op1_button = tkinter.Button(self.button_frame, text='THE WIRES GOT THE BEST OF ' + pronoun.upper() + '.', command=self.transition1)

        self.op1_button.pack(side='left')

        self.button_frame.pack(side='bottom')

    def sc4b_op1(self):
        id1 = 1
        self.id[id1] = '77'
        tkinter.messagebox.showinfo('', 'END')

    def transition1(self):
        self.sc4b_op1()
        global conf
        conf += 1
        self.scene4b.destroy()


class A2S1:
    def __init__(self, master):

        # variables
        global conf

        # text frame
        self.a2s1 = tkinter.Toplevel(master)
        self.a2s1.title("ASLEEP")

        self.a2s1_frame = tkinter.Frame(self.a2s1)
        self.a2s1_frame_label = tkinter.Label(self.a2s1, text='-ARGUING TO LIVE-\nYou\'ve been on the phone for hours now.\n\nYour insurance sent you a letter, letting you know that you\'d missed a payment, and unless it was delivered in full,\nyour insurance would be revoked.\n\nThe trouble is, you have DEFINITELY paid it.\n\nSo now, you\'re trying to navigate the phone system\nand make sure that you can keep getting your medication.\n\nTO DISCUSS A MEDICATION, PLEASE PRESS ONE.\nTO DISCUSS AN OUTSTANDING BILL, PLEASE PRESS TWO.\nTO MAKE A CLAIM, PLEASE PRESS THREE.\nTO CANCEL A CLAIM, PLEASE PRESS FOUR.\nAFTER YOU HAVE ENTERED YOUR SELECTION, PLEASE PRESS POUND.\n')

    # Button frame
        self.button_frame = tkinter.Frame(self.a2s1)

        # buttons
        self.choice_entry = tkinter.Entry(self.a2s1, width=1)
        self.conf_button = tkinter.Button(self.button_frame, text='#', command=self.transition)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.back)

        self.a2s1_frame_label.pack()
        self.choice_entry.pack()
        self.conf_button.pack()
        self.quit_button.pack(side='right')

        self.a2s1_frame.pack(side='top')
        self.button_frame.pack(side='bottom')

    # choice machine for phone menu
    def forward(self):
        sel = int(self.choice_entry.get())
        if sel == 1:
            _ = A2S2(self.a2s1)
        elif sel == 2:
            _ = A2S3(self.a2s1)
        elif sel == 3:
            _ = A2S4(self.a2s1)
        elif sel == 4:
            _ = A2S5(self.a2s1)
        elif sel == 0:
            _ = A2E(self.a2s1)
        else:
            tkinter.messagebox.showinfo('', 'PLEASE MAKE A VALID SELECTION.')

    def clear_window(self):
        self.a2s1.withdraw()

    def transition(self):
        self.forward()
        self.clear_window()

    def back(self):
        self.a2s1.destroy()


class A2S1r:
    def __init__(self, master):
        try:
            id_file = open("id_file.dat", 'rb')
            self.id = pickle.load(id_file)
            id_file.close()
        except (FileNotFoundError, IOError):
            self.id = {}
        # variables
        global conf

        # text frame
        self.a2s1r = tkinter.Toplevel(master)
        self.a2s1r.title("ASLEEP")

        self.a2s1_frame = tkinter.Frame(self.a2s1r)
        self.a2s1_frame_label = tkinter.Label(self.a2s1r, text='-#-\nTO DISCUSS A MEDICATION, PLEASE PRESS ONE.\nTO DISCUSS AN OUTSTANDING BILL, PLEASE PRESS TWO.\nTO FILL A PRESCRIPTION, PLEASE PRESS THREE.\nTO CANCEL A CLAIM, PLEASE PRESS FOUR.\n')

    # Button frame
        self.button_frame = tkinter.Frame(self.a2s1r)

        # buttons
        self.choice_entry = tkinter.Entry(self.a2s1r, width=1)
        self.conf_button = tkinter.Button(self.button_frame, text='#', command=self.transition)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.back)

        self.a2s1_frame_label.pack()
        self.choice_entry.pack()
        self.conf_button.pack()
        self.quit_button.pack(side='right')

        self.a2s1_frame.pack(side='top')
        self.button_frame.pack(side='bottom')

    # choice machine for phone menu
    def forward(self):
        sel = int(self.choice_entry.get())
        if sel == 1:
            _ = A2S2(self.a2s1r)
        elif sel == 2:
            _ = A2S3(self.a2s1r)
        elif sel == 3:
            _ = A2S4(self.a2s1r)
        elif sel == 4:
            _ = A2S5(self.a2s1r)
        elif sel == 0:
            _ = A2E(self.a2s1r)
        else:
            tkinter.messagebox.showinfo('', 'PLEASE MAKE A VALID SELECTION.')

    def clear_window(self):
        self.a2s1r.withdraw()

    def transition(self):
        self.forward()
        self.clear_window()

    def back(self):
        tkinter.messagebox.showinfo('', 'You hang up in frustration.\n\'I\'ll have to try to call again tomorrow,\' you think glumly, feeling the pull of the wires ever tighter.\nYour number is 31.\n')
        id2 = 2
        self.id[id2] = '31'
        outfile = open('id_file.dat', 'wb')
        pickle.dump(self.id, outfile)
        outfile.close()
        global conf
        conf += 1
        self.a2s1r.destroy()


class A2S2:
    def __init__(self, master):
        try:
            id_file = open("id_file.dat", 'rb')
            self.id = pickle.load(id_file)
            id_file.close()
        except (FileNotFoundError, IOError):
            self.id = {}
        # variables
        global conf

        # text frame
        self.a2s2 = tkinter.Toplevel(master)
        self.a2s2.title("ASLEEP")

        self.a2s2_frame = tkinter.Frame(self.a2s2)
        self.a2s2_frame_label = tkinter.Label(self.a2s2, text='-#-\nTO REQUEST A MEDICATION, PLEASE PRESS ONE.\nTO DISCUSS A BILL FOR MEDICATION, PLEASE PRESS TWO.\nTO FILL A PRESCRIPTION, PLEASE PRESS THREE.\nFOR GENERAL OPTIONS, PLEASE PRESS FOUR.\n')

    # Button frame
        self.button_frame = tkinter.Frame(self.a2s2)

        # buttons
        self.choice_entry = tkinter.Entry(self.a2s2, width=1)
        self.conf_button = tkinter.Button(self.button_frame, text='#', command=self.transition)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.back)

        self.a2s2_frame_label.pack()
        self.choice_entry.pack()
        self.conf_button.pack()
        self.quit_button.pack(side='right')

        self.a2s2_frame.pack(side='top')
        self.button_frame.pack(side='bottom')

    # choice machine for phone menu
    def forward(self):
        sel = int(self.choice_entry.get())
        if sel == 1:
            _ = A2S6(self.a2s2)
        elif sel == 2:
            _ = A2S3(self.a2s2)
        elif sel == 3:
            _ = A2S4(self.a2s2)
        elif sel == 4:
            _ = A2S1r(self.a2s2)
        elif sel == 0:
            _ = A2E(self.a2s2)
        else:
            tkinter.messagebox.showinfo('', 'PLEASE MAKE A VALID SELECTION.')

    def clear_window(self):
        self.a2s2.withdraw()

    def transition(self):
        self.forward()
        self.clear_window()

    def back(self):
        tkinter.messagebox.showinfo('', 'You hang up in frustration.\n\'I\'ll have to try to call again tomorrow,\' you think glumly, feeling the pull of the wires ever tighter.\nYour number is 31.\n')
        id2 = 2
        self.id[id2] = '31'
        outfile = open('id_file.dat', 'wb')
        pickle.dump(self.id, outfile)
        outfile.close()
        global conf
        conf += 1
        self.a2s2.destroy()


class A2S3:
    def __init__(self, master):
        try:
            id_file = open("id_file.dat", 'rb')
            self.id = pickle.load(id_file)
            id_file.close()
        except (FileNotFoundError, IOError):
            self.id = {}
        # variables
        global conf

        # text frame
        self.a2s3 = tkinter.Toplevel(master)
        self.a2s3.title("ASLEEP")

        self.a2s3_frame = tkinter.Frame(self.a2s3)
        self.a2s3_frame_label = tkinter.Label(self.a2s3, text='-#-\nTO REQUEST A MEDICATION, PLEASE PRESS ONE.\nTO DISCUSS A BILL FOR MEDICATION, PLEASE PRESS TWO.\nTO FILL A PRESCRIPTION, PLEASE PRESS THREE.\nFOR GENERAL OPTIONS, PLEASE PRESS FOUR.\n')

    # Button frame
        self.button_frame = tkinter.Frame(self.a2s3)

        # buttons
        self.choice_entry = tkinter.Entry(self.a2s3, width=1)
        self.conf_button = tkinter.Button(self.button_frame, text='#', command=self.transition)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.back)

        self.a2s3_frame_label.pack()
        self.choice_entry.pack()
        self.conf_button.pack()
        self.quit_button.pack(side='right')

        self.a2s3_frame.pack(side='top')
        self.button_frame.pack(side='bottom')

    # choice machine for phone menu
    def forward(self):
        sel = int(self.choice_entry.get())
        if sel == 1:
            _ = A2S6(self.a2s3)
        elif sel == 2:
            _ = A2S3(self.a2s3)
        elif sel == 3:
            _ = A2S4(self.a2s3)
        elif sel == 4:
            _ = A2S1r(self.a2s3)
        elif sel == 0:
            _ = A2E(self.a2s3)
        else:
            tkinter.messagebox.showinfo('', 'PLEASE MAKE A VALID SELECTION.')

    def clear_window(self):
        self.a2s3.withdraw()

    def transition(self):
        self.forward()
        self.clear_window()

    def back(self):
        tkinter.messagebox.showinfo('', 'You hang up in frustration.\n\'I\'ll have to try to call again tomorrow,\' you think glumly, feeling the pull of the wires ever tighter.\nYour number is 31.\n')
        id2 = 2
        self.id[id2] = '31'
        outfile = open('id_file.dat', 'wb')
        pickle.dump(self.id, outfile)
        outfile.close()
        global conf
        conf += 1
        self.a2s3.destroy()


class A2S4:
    def __init__(self, master):
        try:
            id_file = open("id_file.dat", 'rb')
            self.id = pickle.load(id_file)
            id_file.close()
        except (FileNotFoundError, IOError):
            self.id = {}
        # variables
        global conf

        # text frame
        self.a2s4 = tkinter.Toplevel(master)
        self.a2s4.title("ASLEEP")

        self.a2s2_frame = tkinter.Frame(self.a2s4)
        self.a2s2_frame_label = tkinter.Label(self.a2s4, text='-#-\nTO REQUEST A MEDICATION, PLEASE PRESS ONE.\nTO DISCUSS A BILL FOR MEDICATION, PLEASE PRESS TWO.\nTO FILL A PRESCRIPTION, PLEASE PRESS THREE.\nFOR GENERAL OPTIONS, PLEASE PRESS FOUR.\n')

    # Button frame
        self.button_frame = tkinter.Frame(self.a2s4)

        # buttons
        self.choice_entry = tkinter.Entry(self.a2s4, width=1)
        self.conf_button = tkinter.Button(self.button_frame, text='#', command=self.transition)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.back)

        self.a2s2_frame_label.pack()
        self.choice_entry.pack()
        self.conf_button.pack()
        self.quit_button.pack(side='right')

        self.a2s2_frame.pack(side='top')
        self.button_frame.pack(side='bottom')

    # choice machine for phone menu
    def forward(self):
        sel = int(self.choice_entry.get())
        if sel == 1:
            _ = A2S6(self.a2s4)
        elif sel == 2:
            _ = A2S3(self.a2s4)
        elif sel == 3:
            _ = A2S4(self.a2s4)
        elif sel == 4:
            _ = A2S1r(self.a2s4)
        elif sel == 0:
            _ = A2E(self.a2s4)
        else:
            tkinter.messagebox.showinfo('', 'PLEASE MAKE A VALID SELECTION.')

    def clear_window(self):
        self.a2s4.withdraw()

    def transition(self):
        self.forward()
        self.clear_window()

    def back(self):
        tkinter.messagebox.showinfo('', 'You hang up in frustration.\n\'I\'ll have to try to call again tomorrow,\' you think glumly, feeling the pull of the wires ever tighter.\nYour number is 31.\n')
        id2 = 2
        self.id[id2] = '31'
        outfile = open('id_file.dat', 'wb')
        pickle.dump(self.id, outfile)
        outfile.close()
        global conf
        conf += 1
        self.a2s4.destroy()


class A2S5:
    def __init__(self, master):
        try:
            id_file = open("id_file.dat", 'rb')
            self.id = pickle.load(id_file)
            id_file.close()
        except (FileNotFoundError, IOError):
            self.id = {}
        # variables
        global conf

        # text frame
        self.a2s5 = tkinter.Toplevel(master)
        self.a2s5.title("ASLEEP")

        self.a2s5_frame = tkinter.Frame(self.a2s5)
        self.a2s5_frame_label = tkinter.Label(self.a2s5, text='-#-\nTO REQUEST A MEDICATION, PLEASE PRESS ONE.\nTO DISCUSS A BILL FOR MEDICATION, PLEASE PRESS TWO.\nTO FILL A PRESCRIPTION, PLEASE PRESS THREE.\nFOR GENERAL OPTIONS, PLEASE PRESS FOUR.\n')

    # Button frame
        self.button_frame = tkinter.Frame(self.a2s5)

        # buttons
        self.choice_entry = tkinter.Entry(self.a2s5, width=1)
        self.conf_button = tkinter.Button(self.button_frame, text='#', command=self.transition)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.back)

        self.a2s5_frame_label.pack()
        self.choice_entry.pack()
        self.conf_button.pack()
        self.quit_button.pack(side='right')

        self.a2s5_frame.pack(side='top')
        self.button_frame.pack(side='bottom')

    # choice machine for phone menu
    def forward(self):
        sel = int(self.choice_entry.get())
        if sel == 1:
            _ = A2S6(self.a2s5)
        elif sel == 2:
            _ = A2S3(self.a2s5)
        elif sel == 3:
            _ = A2S4(self.a2s5)
        elif sel == 4:
            _ = A2S1r(self.a2s5)
        elif sel == 0:
            _ = A2E(self.a2s5)
        else:
            tkinter.messagebox.showinfo('', 'PLEASE MAKE A VALID SELECTION.')

    def clear_window(self):
        self.a2s5.withdraw()

    def transition(self):
        self.forward()
        self.clear_window()

    def back(self):
        tkinter.messagebox.showinfo('', 'You hang up in frustration.\n\'I\'ll have to try to call again tomorrow,\' you think glumly, feeling the pull of the wires ever tighter.\nYour number is 31.\n')
        id2 = 2
        self.id[id2] = '31'
        outfile = open('id_file.dat', 'wb')
        pickle.dump(self.id, outfile)
        outfile.close()
        global conf
        conf += 1
        self.a2s5.destroy()


class A2S6:
    def __init__(self, master):
        try:
            id_file = open("id_file.dat", 'rb')
            self.id = pickle.load(id_file)
            id_file.close()
        except (FileNotFoundError, IOError):
            self.id = {}
        # variables
        global conf

        # text frame
        self.a2s6 = tkinter.Toplevel(master)
        self.a2s6.title("ASLEEP")

        self.a2s6_frame = tkinter.Frame(self.a2s6)
        self.a2s6_frame_label = tkinter.Label(self.a2s6, text='-#-\nTO REQUEST A MEDICATION, PLEASE PRESS ONE.\nTO DISCUSS A BILL FOR MEDICATION, PLEASE PRESS TWO.\nTO FILL A PRESCRIPTION, PLEASE PRESS THREE.\nFOR GENERAL OPTIONS, PLEASE PRESS FOUR.\n')

    # Button frame
        self.button_frame = tkinter.Frame(self.a2s6)

        # buttons
        self.choice_entry = tkinter.Entry(self.a2s6, width=1)
        self.conf_button = tkinter.Button(self.button_frame, text='#', command=self.transition)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.back)

        self.a2s6_frame_label.pack()
        self.choice_entry.pack()
        self.conf_button.pack()
        self.quit_button.pack(side='right')

        self.a2s6_frame.pack(side='top')
        self.button_frame.pack(side='bottom')

    # choice machine for phone menu
    def forward(self):
        sel = int(self.choice_entry.get())
        if sel == 1:
            _ = A2S6(self.a2s6)
        elif sel == 2:
            _ = A2S3(self.a2s6)
        elif sel == 3:
            _ = A2S4(self.a2s6)
        elif sel == 4:
            _ = A2S1r(self.a2s6)
        elif sel == 0:
            _ = A2E(self.a2s6)
        else:
            tkinter.messagebox.showinfo('', 'PLEASE MAKE A VALID SELECTION.')

    def clear_window(self):
        self.a2s6.withdraw()

    def transition(self):
        self.forward()
        self.clear_window()

    def back(self):
        tkinter.messagebox.showinfo('', 'You hang up in frustration.\n\'I\'ll have to try to call again tomorrow,\' you think glumly, feeling the pull of the wires ever tighter.\nYour number is 31.\n')
        id2 = 2
        self.id[id2] = '31'
        outfile = open('id_file.dat', 'wb')
        pickle.dump(self.id, outfile)
        outfile.close()
        global conf
        conf += 1
        self.a2s6.destroy()


class A2E:
    def __init__(self, master):
        try:
            id_file = open("id_file.dat", 'rb')
            self.id = pickle.load(id_file)
            id_file.close()
        except (FileNotFoundError, IOError):
            self.id = {}
        # variables
        global conf

        # text frame
        self.a2e = tkinter.Toplevel(master)
        self.a2e.title("ASLEEP")

        self.a2e_frame = tkinter.Frame(self.a2e)
        self.a2e_frame_label = tkinter.Label(self.a2e, text='-#-\nPLEASE HOLD WHILE WE CONNECT YOU TO A REPRESENTATIVE.\nYOUR NUMBER IS 15.')

    # Button frame
        self.button_frame = tkinter.Frame(self.a2e)

        # buttons
        self.conf_button = tkinter.Button(self.button_frame, text='Okay', command=self.transition)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.back)

        self.a2e_frame_label.pack()
        self.conf_button.pack()
        self.quit_button.pack(side='right')

        self.a2e_frame.pack(side='top')
        self.button_frame.pack(side='bottom')

    # choice machine for phone menu
    def forward(self):
        id2 = 2
        self.id[id2] = '15'
        outfile = open('id_file.dat', 'wb')
        pickle.dump(self.id, outfile)
        outfile.close()
        global conf
        conf += 1

    def clear_window(self):
        self.a2e.withdraw()

    def transition(self):
        self.forward()
        self.clear_window()

    def back(self):
        self.a2e.destroy()


class A3S1:
    def __init__(self, master):

        self.a3s1 = tkinter.Toplevel(master)
        self.a3s1.title('AFRAID')
        self.itera = 0

        # variables
        global conf
        global age
        global gend
        gen = 0
        if gend == 1:
            gen = 'man'
        if gend == 2:
            gen = 'woman'
        if gend == 3:
            gen = 'person'

        # text frame
        self.a3s1_frame = tkinter.Frame(self.a3s1)
        self.a3s1_frame_label = tkinter.Label(self.a3s1, text='-THE ASSASSIN-')
        self.a3s1_frame_text = tkinter.Label(self.a3s1, text='The sight shows your target clear as day.\n\nYou never considered yourself to be an assassin.\nIt would have been ludicrous to,\nconsidering you\'re a ' + age + ' year old ' + gen + ' who just got pushed into doing this by a friend.\nYou\'ve never even BEEN to South America,\nbut now here you are, about to assassinate the Brazilian President because\nyour best friend gave a VERY good speech a few years ago about\ntheir evils and how they must be stopped.\n\nAnd now you\'re on the verge of actually doing it.\n\nYour finger begins to curl around the trigger. Your aim is true, and the shot is yours.\n')

        # Button frame
        self.button_frame = tkinter.Frame(self.a3s1)

        # buttons
        self.op1_button = tkinter.Button(self.button_frame, text='SHOOT', command=self.transition)
        self.op2_button = tkinter.Button(self.button_frame, text='DON\'T', command=self.fail)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.back)

        self.op1_button.pack(side='left')
        self.op2_button.pack(side='left')
        self.quit_button.pack(side='right')

        self.a3s1_frame_label.pack(side='top')
        self.a3s1_frame_text.pack(side='top', anchor='w')
        self.a3s1_frame.pack(side='top')
        self.button_frame.pack(side='bottom')

    def transition(self):
        if self.itera == 2:
            _ = A3E(self.a3s1)
            self.clear_window()
        else:
            while self.itera == 0:
                if tkinter.messagebox.askyesno('', 'Are you sure?'):  # http://effbot.org/tkinterbook/tkinter-standard-dialogs.htm
                    self.itera += 1
            while self.itera == 1:
                if tkinter.messagebox.askyesno('', 'Are you absolutely certain?'):
                    self.itera += 1
                    self.transition()

    def fail(self):
        _ = A3F(self.a3s1)
        self.clear_window()

    def clear_window(self):
        self.a3s1.withdraw()

    def back(self):
        self.a3s1.destroy()


class A3E:
    def __init__(self, master):
        try:
            id_file = open("id_file.dat", 'rb')
            self.id = pickle.load(id_file)
            id_file.close()
        except (FileNotFoundError, IOError):
            self.id = {}
        self.a3e = tkinter.Toplevel(master)
        self.a3e.title('AFRAID')

        # variables
        global conf
        global age
        global gend
        gen = 0
        pronoun = 0
        if gend == 1:
            gen = 'man'
            pronoun = 'him'
        if gend == 2:
            gen = 'woman'
            pronoun = 'her'
        if gend == 3:
            gen = 'person'
            pronoun = 'them'

        # text frame
        self.a3e_frame = tkinter.Frame(self.a3e)
        self.a3e_frame_label = tkinter.Label(self.a3e, text='-A CLEAN KILL-')
        self.a3e_frame_text = tkinter.Label(self.a3e, text='The trigger is pulled, and your target crumples.\n\nYou pack up as you were trained to do and leave immediately,\nrushing to avoid the diligent security now on your trail.\n\nYou rush out of the city and into the wilderness, search lights shining from helicopters and panic running through your mind.\n\nYou were just a normal ' + gen + '.\n\nYou didn\'t want this.\n\nBut your friend\'s idealism let the wires into you, and now you belong to them.\nThe assassin\'s number is 52.')

        # Button frame
        self.button_frame = tkinter.Frame(self.a3e)

        # buttons
        self.op1_button = tkinter.Button(self.button_frame, text='THE WIRES GOT THE BEST OF ' + pronoun.upper() + '.', command=self.transition1)

        self.op1_button.pack(side='left')

        self.a3e_frame_label.pack(side='top')
        self.a3e_frame_text.pack(side='top', anchor='w')
        self.a3e_frame.pack(side='top')
        self.button_frame.pack(side='bottom')

    def end(self):
        id3 = 3
        self.id[id3] = '52'
        outfile = open('id_file.dat', 'wb')
        pickle.dump(self.id, outfile)
        outfile.close()
        tkinter.messagebox.showinfo('', 'END')

    def transition1(self):
        self.end()
        global conf
        conf += 1
        self.a3e.destroy()

    def fail(self):
        _ = A3F(self.a3e)
        self.clear_window()

    def clear_window(self):
        self.a3e.withdraw()

    def back(self):
        self.a3e.destroy()


class A3F:
    def __init__(self, master):
        try:
            id_file = open("id_file.dat", 'rb')
            self.id = pickle.load(id_file)
            id_file.close()
        except (FileNotFoundError, IOError):
            self.id = {}
        self.a3f = tkinter.Toplevel(master)
        self.a3f.title('AFRAID')

        # variables
        global conf
        global age
        global gend
        gen = 0
        if gend == 1:
            gen = 'man'
        if gend == 2:
            gen = 'woman'
        if gend == 3:
            gen = 'person'

        # text frame
        self.a3f_frame = tkinter.Frame(self.a3f)
        self.a3f_frame_label = tkinter.Label(self.a3f, text='-ESCAPE-')
        self.a3f_frame_text = tkinter.Label(self.a3f, text='This... is insane. You aren\'t meant to do this. This isn\'t any of your business.\nYou turn to flee, and don\'t get far before the rebel assigned to watch you catches up.\nThe President may live, but as the bag descends over your head and your arms are bound in wire,\nyou know you\'re on the way out.\nThe coward\'s number is 28.')

        # Button frame
        self.button_frame = tkinter.Frame(self.a3f)

        # buttons
        self.op1_button = tkinter.Button(self.button_frame, text='THE WIRES GOT THE BEST OF ' + gen + '.', command=self.transition1)

        self.op1_button.pack(side='left')

        self.a3f_frame_label.pack(side='top')
        self.a3f_frame_text.pack(side='top', anchor='w')
        self.a3f_frame.pack(side='top')
        self.button_frame.pack(side='bottom')

    def end(self):
        id3 = 3
        self.id[id3] = '28'
        outfile = open('id_file.dat', 'wb')
        pickle.dump(self.id, outfile)
        outfile.close()
        tkinter.messagebox.showinfo('', 'END')

    def transition1(self):
        self.end()
        global conf
        conf += 1
        self.a3f.destroy()

    def fail(self):
        _ = A3F(self.a3f)
        self.clear_window()

    def clear_window(self):
        self.a3f.withdraw()

    def back(self):
        self.a3f.destroy()


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
