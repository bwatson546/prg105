import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        # Create main window
        self.main_window = tkinter.Tk()

        # Create StringVar for mpg
        self.mpg = tkinter.StringVar()

        # Create two frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create widgets for top frame
        self.prompt_label = tkinter.Label(self.top_frame, text='Enter how many gallons your car holds:')
        self.gallon_entry = tkinter.Entry(self.top_frame, width=10)
        self.prompt2_label = tkinter.Label(self.top_frame, text='Enter how many miles you can travel on a full tank:')
        self.mile_entry = tkinter.Entry(self.top_frame, width=10)

        # create label for mpg
        self.mpg_label = tkinter.Label(self.top_frame, textvariable=self.mpg)

        # Pack top widgets; 'top' puts them all on top of each other, instead of all in a horizontal line
        self.prompt_label.pack(side='top')
        self.gallon_entry.pack(side='top')
        self.prompt2_label.pack(side='top')
        self.mile_entry.pack(side='top')
        self.mpg_label.pack(side='bottom')

        # Create buttons for bottom frame
        self.calc_button = tkinter.Button(self.bottom_frame, text='Convert', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        # Pack buttons
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='right')

        # Pack Frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Enter tkinter main loop
        tkinter.mainloop()

    def convert(self):
        # get the value entered by user into gallon_entry and mile_entry
        gallons = float(self.gallon_entry.get())
        miles = float(self.mile_entry.get())

        mpg = miles/gallons

        # Display results in the message box
        self.mpg.set('Converted to miles per gallons: ' + str(mpg))


my_gui = MyGUI()
