import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        # Create main window
        self.main_window = tkinter.Tk()

        # Message string
        self.message = 'YOU HAVE CHOSEN:\n'

        # total variable
        self.total = tkinter.StringVar()

        # Two frames; Radiobutton + regular buttons
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Labels
        self.form_label = tkinter.Label(self.top_frame, text='DEAD FORMAT ORDER FORM')
        self.inst_label = tkinter.Label(self.top_frame,
                                        text='Some of these are games, some are services. Choose Wisely!')

        # Packin' Labels
        self.form_label.pack()
        self.inst_label.pack()

        # Create IntVar objects; used with check buttons
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        self.cb_var6 = tkinter.IntVar()
        self.cb_var7 = tkinter.IntVar()
        self.cb_var8 = tkinter.IntVar()

        # Set IntVar objects to 0
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.cb_var6.set(0)
        self.cb_var7.set(0)
        self.cb_var8.set(0)

        # Create radiobutton widgets in top frame
        self.cb1 = tkinter.Checkbutton(self.top_frame, text='TeleGhast: $30', variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame, text='The Swift Release of Death: $10', variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame, text='Cathode Carl Wants Me Dead: $20', variable=self.cb_var3)
        self.cb4 = tkinter.Checkbutton(self.top_frame, text='Ten Thousand Bees: $5', variable=self.cb_var4)
        self.cb5 = tkinter.Checkbutton(self.top_frame, text='Lunar Year: $30', variable=self.cb_var5)
        self.cb6 = tkinter.Checkbutton(self.top_frame, text='Ecliptic Year: $30', variable=self.cb_var6)
        self.cb7 = tkinter.Checkbutton(self.top_frame, text='Your Longest Year: $30', variable=self.cb_var7)
        self.cb8 = tkinter.Checkbutton(self.top_frame, text='Quell The Plague: $30', variable=self.cb_var8)

        # pack them buttons
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()
        self.cb8.pack()

        # Create total and Quit buttons
        self.total_button = tkinter.Button(self.bottom_frame, text='Total', command=self.total)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        # pack buttons
        self.total_button.pack(side='left')
        self.quit_button.pack(side='right')

        # pack frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # start mainloop
        tkinter.mainloop()

    def total(self):
        # Determine checkboxes, display accordingly
        if self.cb_var1.get() == 1:
            self.message = self.message + 'Teleghast ($30)\n'
            self.total = self.total + 30
        if self.cb_var2.get() == 1:
            self.message = self.message + 'The Swift Release of Death ($10)\n'
            self.total = self.total + 10
        if self.cb_var3.get() == 1:
            self.message = self.message + 'Cathode Carl Wants Me Dead ($20)\n'
            self.total = self.total + 20
        if self.cb_var4.get() == 1:
            self.message = self.message + 'Ten Thousand Bees ($5)\n'
            self.total = self.total + 5
        if self.cb_var5.get() == 1:
            self.message = self.message + 'Lunar Year ($30)\n'
            self.total = self.total + 30
        if self.cb_var6.get() == 1:
            self.message = self.message + 'Ecliptic Year ($30)\n'
            self.total = self.total + 30
        if self.cb_var7.get() == 1:
            self.message = self.message + 'Your Longest Year ($30)\n'
            self.total = self.total + 30
        if self.cb_var8.get() == 1:
            self.message = self.message + 'Quell The Plague ($30)\n'
            self.total = self.total + 30

        # Display message in a dialog
        tkinter.messagebox.showinfo(self.message + '\n' + 'AMOUNTING TO $' + str(
            self.total) + '!\nWE HOPE YOU ENJOY/SURVIVE YOUR PURCHASES!')


my_gui = MyGUI()
