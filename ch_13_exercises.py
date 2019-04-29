"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""
import tkinter
import tkinter.messagebox

# TODO 13.2 Using the tkinter Module
print("=" * 10, "Section 13.2 using tkinter", "=" * 10)


# Write the code from program 13-2 to display an empty window, no need
# to re-import tkinter. Use the class name MyGUI2


class MyGUI2:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.label = tkinter.Label(self.main_window, text='Crimes Optional')
        self.label.pack()

        tkinter.mainloop()


# TODO 13.3 Adding a label widget
print("=" * 10, "Section 13.3 adding a label widget", "=" * 10)
# Add a label to MyGUI2 (above) that prints your first and last name; pack the label
# Create an instance of MyGUI2

sampleGUI1 = MyGUI2()

# TODO 13.4 Organizing Widgets with Frames
print("=" * 10, "Section 13.4 using frames", "=" * 10)


# Create a MyGUI3 class that creates a window with two frames
# In the top Frame add labels with your name and major
# In the bottom frame add labels with the classes you are taking this semester
# Create an instance of MyGUI3


class MyGUI3:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.top_frame, text='CrimesOptional')
        self.label2 = tkinter.Label(self.top_frame, text='Mischief and Schemes')
        self.label3 = tkinter.Label(self.bottom_frame, text='Killin\' It 101')
        self.label4 = tkinter.Label(self.bottom_frame, text='Pranks 305')
        self.label5 = tkinter.Label(self.bottom_frame, text='Cool Dudeing 999')

        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.label3.pack(side='left')
        self.label4.pack(side='left')
        self.label5.pack(side='left')

        self.top_frame.pack(side='top')
        self.bottom_frame.pack(side='bottom')

        tkinter.mainloop()


sample = MyGUI3()

# TODO 13.5 Button Widgets and info Dialog Boxes
print("=" * 10, "Section 13.5 button widgets and info dialogs", "=" * 10)
# Create a GUI that will tell a joke
# Use a button to show the punch line, which should appear in a dialog box
# Create an instance of the GUI


class MyGUI4:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.label1 = tkinter.Label(text='Why couldn\'t the bicycle stand up by itself?')
        self.button = tkinter.Button(self.main_window, text='what', command=self.wakkawakka)

        self.label1.pack(side='top')
        self.button.pack(side='top')

        tkinter.mainloop()

    def wakkawakka(self):
        tkinter.messagebox.showinfo('Answer', 'Because it was two tired')


fozzi = MyGUI4()

# TODO 13.6 getting input / 13.7 Using Labels as output fields
print("=" * 10, "Section 13.6-13.7 input and output using Entry and Label", "=" * 10)


# Using the program in 13.10 kilo converter as a sample,
# create a program to convert inches to centimeters


class MyGUI5:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.prompt_label = tkinter.Label(self.top_frame, text='Enter a measurement in inches:')
        self.inch_entry = tkinter.Entry(self.top_frame, width=20)

        self.prompt_label.pack(side='left')
        self.inch_entry.pack(side='left')

        self.calc_button = tkinter.Button(self.bottom_frame, text='Calculate', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.Destroy())

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()

    def convert(self):
        inch = float(self.inch_entry.get())
        centi = inch * 2.54
        tkinter.messagebox.showinfo('Results', str(inch) + ' inches = ' + str(centi) + ' centimeters!')


inches = MyGUI5()
