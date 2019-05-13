import tkinter
import tkinter.messagebox
import pickle


# main (root) GUI menu
class CrudGUI:
    def __init__(self, master):
        self.master = master
        self.master.title('Welcome Menu')

        self.top_frame = tkinter.Frame(self.master)
        self.bottom_frame = tkinter.Frame(self.master)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        # create the radio buttons
        self.look = tkinter.Radiobutton(self.top_frame, text='Look up customer',
                                        variable=self.radio_var, value=1)
        self.add = tkinter.Radiobutton(self.top_frame, text='Add Customer',
                                       variable=self.radio_var, value=2)
        self.change = tkinter.Radiobutton(self.top_frame, text='Change customer email',
                                          variable=self.radio_var, value=3)
        self.delete = tkinter.Radiobutton(self.top_frame, text='Delete customer',
                                          variable=self.radio_var, value=4)

        # pack the radio buttons
        self.look.pack(anchor='w', padx=20)
        self.add.pack(anchor='w', padx=20)
        self.change.pack(anchor='w', padx=20)
        self.delete.pack(anchor='w', padx=20)

        # create ok and quit buttons
        self.ok_button = tkinter.Button(self.bottom_frame, text='OK', command=self.open_menu)
        self.quit_button = tkinter.Button(self.bottom_frame, text='QUIT', command=self.master.destroy)

        # pack the buttons
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

    def open_menu(self):
        if self.radio_var.get() == 1:
            _ = LookGUI(self.master)
        elif self.radio_var.get() == 2:
            _ = AddGUI(self.master)
        elif self.radio_var.get() == 3:
            _ = ChangeGUI(self.master)
        elif self.radio_var.get() == 4:
            _ = DeleteGUI(self.master)
        else:
            tkinter.messagebox.showinfo('Function', 'still under construction')


class DeleteGUI:
    def __init__(self, master):
        try:
            input_file = open("customer_file.dat", 'rb')
            self.customers = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.customers = {}

        self.delete = tkinter.Toplevel(master)
        self.delete.title('Delete Customer Email')

        # Variables
        self.statusVar = tkinter.StringVar()
        self.statusVar.set('Unchecked')
        self.currentVar = tkinter.StringVar()
        self.currentVar.set('Empty')
        self.currentName = tkinter.StringVar()
        self.currentName.set('Empty')

        # Search Frame
        self.search_frame = tkinter.Frame(self.delete)
        self.search_frame_label = tkinter.Label(self.delete, text='Enter customer name to delete.')
        self.search_frame_entry = tkinter.Entry(self.delete, width=25)
        self.search_frame_label.pack(side='top')
        self.search_frame_entry.pack(side='top')
        self.search_frame.pack(side='top')

        # Search Button Frame
        self.search_button_frame = tkinter.Frame(self.delete)
        self.search_button = tkinter.Button(self.search_button_frame, text='Locate', command=self.check)
        self.search_button.pack(side='bottom')
        self.search_button_frame.pack(side='bottom')

        # Locate Frame
        self.locate_frame = tkinter.Frame(self.delete)
        self.result_label = tkinter.Label(self.locate_frame, text='Record Status: ')
        self.status_label = tkinter.Label(self.locate_frame, textvariable=self.statusVar)
        self.result_label.pack(side='left')
        self.status_label.pack(side='left')
        self.locate_frame.pack(side='bottom')

        # current record frame
        self.current_frame = tkinter.Frame(self.delete)
        self.current_label = tkinter.Label(self.current_frame, text='Current Entry: ')
        self.current_name_label = tkinter.Label(self.current_frame, textvariable=self.currentName)
        self.current_data_label = tkinter.Label(self.current_frame, textvariable=self.currentVar)
        self.current_label.pack(side='top')
        self.current_name_label.pack(side='left')
        self.current_data_label.pack(side='right')
        self.current_frame.pack(side='top')

        # Button frame
        self.button_frame = tkinter.Frame(self.delete)
        self.delete_button = tkinter.Button(self.button_frame, text='Delete', command=self.deleteBut)
        self.back_button = tkinter.Button(self.button_frame, text='Main Menu', command=self.back)
        self.delete_button.pack(side='left')
        self.back_button.pack(side='right')
        self.button_frame.pack(side='top')

    def check(self):
        name = self.search_frame_entry.get()
        result = self.customers.get(name, 'Not Found')

        if result == 'Not Found':
            self.statusVar.set('Not Found')
            self.currentVar.set('Not Found')
            self.currentName.set('Not Found')

        else:
            self.statusVar.set('Record Located')
            self.currentName.set(name)
            self.currentVar.set(result)

    def deleteBut(self):
        name = self.search_frame_entry.get()
        try:
            del self.customers[name]
            self.statusVar.set('RECORD DELETED')
            self.currentVar.set('DELETED')
            self.currentName.set('DELETED')
            tkinter.messagebox.showinfo('Deleted', 'Record deleted.')
        except KeyError:
            tkinter.messagebox.showinfo('ERROR', 'RECORD NOT FOUND')

    def back(self):
        outfile = open('customer_file.dat', 'wb')
        pickle.dump(self.customers, outfile)
        outfile.close()
        self.delete.destroy()


class ChangeGUI:
    def __init__(self, master):
        try:
            input_file = open("customer_file.dat", 'rb')
            self.customers = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.customers = {}

        self.change = tkinter.Toplevel(master)
        self.change.title('Change Customer Email')

        # Variables
        self.statusVar = tkinter.StringVar()
        self.statusVar.set('Unchecked')
        self.currentVar = tkinter.StringVar()
        self.currentVar.set('Empty')
        self.currentName = tkinter.StringVar()
        self.currentName.set('Empty')

        # Search Frame
        self.search_frame = tkinter.Frame(self.change)
        self.search_frame_label = tkinter.Label(self.change, text='Enter customer name to change.')
        self.search_frame_entry = tkinter.Entry(self.change, width=25)
        self.search_frame_label.pack(side='top')
        self.search_frame_entry.pack(side='top')
        self.search_frame.pack(side='top')

        # Search Button Frame
        self.search_button_frame = tkinter.Frame(self.change)
        self.search_button = tkinter.Button(self.search_button_frame, text='Check', command=self.check)
        self.search_button.pack(side='bottom')
        self.search_button_frame.pack(side='bottom')

        # Locate Frame
        self.locate_frame = tkinter.Frame(self.change)
        self.result_label = tkinter.Label(self.locate_frame, text='Record Status: ')
        self.status_label = tkinter.Label(self.locate_frame, textvariable=self.statusVar)
        self.result_label.pack(side='left')
        self.status_label.pack(side='left')
        self.locate_frame.pack(side='bottom')

        # current record frame
        self.current_frame = tkinter.Frame(self.change)
        self.current_label = tkinter.Label(self.current_frame, text='Current Entry: ')
        self.current_name_label = tkinter.Label(self.current_frame, textvariable=self.currentName)
        self.current_data_label = tkinter.Label(self.current_frame, textvariable=self.currentVar)
        self.current_label.pack(side='top')
        self.current_name_label.pack(side='left')
        self.current_data_label.pack(side='right')
        self.current_frame.pack(side='top')

        # Change Frame
        self.change_frame = tkinter.Frame(self.change)
        self.change_label = tkinter.Label(self.change_frame, text='New Email: ')
        self.change_entry = tkinter.Entry(self.change_frame, width=25)
        self.change_label.pack(side='left')
        self.change_entry.pack(side='right')
        self.change_frame.pack(side='top')

        # Button frame
        self.button_frame = tkinter.Frame(self.change)
        self.change_button = tkinter.Button(self.button_frame, text='Change', command=self.changeBut)
        self.back_button = tkinter.Button(self.button_frame, text='Back', command=self.back)
        self.change_button.pack(side='left')
        self.back_button.pack(side='right')
        self.button_frame.pack(side='top')

    def check(self):
        name = self.search_frame_entry.get()
        result = self.customers.get(name, 'Not Found')

        if result == 'Not Found':
            self.statusVar.set('Not Found')
            self.currentVar.set('Not Found')
            self.currentName.set('Not Found')

        else:
            self.statusVar.set('Record Located')
            self.currentName.set(name)
            self.currentVar.set(result)

    def changeBut(self):
        new = self.change_entry.get()
        name = self.search_frame_entry.get()
        self.customers[name] = new
        self.statusVar.set('Changed')
        self.currentVar.set(new)

    def back(self):
        outfile = open('customer_file.dat', 'wb')
        pickle.dump(self.customers, outfile)
        outfile.close()
        self.change.destroy()


class AddGUI:
    def __init__(self, master):
        try:
            input_file = open("customer_file.dat", 'rb')
            self.customers = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.customers = {}

        self.addGUI = tkinter.Toplevel(master)
        self.addGUI.title('Add Customer Data')

        self.name_frame = tkinter.Frame(self.addGUI)
        self.email_frame = tkinter.Frame(self.addGUI)
        self.button_frame = tkinter.Frame(self.addGUI)

        self.add_name_label = tkinter.Label(self.name_frame, text='Customer Name: ')
        self.add_name_entry = tkinter.Entry(self.name_frame, width=25)

        self.add_name_label.pack(side='left')
        self.add_name_entry.pack(side='right')
        self.name_frame.pack(side='top')

        self.add_email_label = tkinter.Label(self.email_frame, text="Customer Email: ")
        self.add_email_entry = tkinter.Entry(self.email_frame, width=25)

        self.add_email_label.pack(side='left')
        self.add_email_entry.pack(side='right')
        self.email_frame.pack(side='top')

        self.add_button = tkinter.Button(self.button_frame, text='Add', command=self.addbut)
        self.back_button = tkinter.Button(self.button_frame, text='Main Menu', command=self.back)

        self.add_button.pack(side='left')
        self.back_button.pack(side='right')
        self.button_frame.pack(side='top')

    def addbut(self):
        name = self.add_name_entry.get()
        email = self.add_email_entry.get()
        self.customers[name] = email
        tkinter.messagebox.showinfo('Success', 'Data Entered')

    def back(self):

        outfile = open('customer_file.dat', 'wb')
        pickle.dump(self.customers, outfile)
        outfile.close()
        self.addGUI.destroy()


class LookGUI:
    def __init__(self, master):

        # open the file, load to customers, close file. Do in each class
        try:
            input_file = open("customer_file.dat", 'rb')
            self.customers = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.customers = {}

        # tkinter.Toplevel() is like tkinter.Frame() but it opens in a new window
        self.look = tkinter.Toplevel(master)
        self.look.title('Search for customer')

        # create Frames for this Toplevel window
        self.top_frame = tkinter.Frame(self.look)
        self.middle_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)

        # widgets for top frame - label and entry box for name
        self.search_label = tkinter.Label(self.top_frame, text='Enter customer name to look for: ')
        self.search_entry = tkinter.Entry(self.top_frame, width=15)

        # pack top frame
        self.search_label.pack(side='left')
        self.search_entry.pack(side='left')

        # middle frame - label for results
        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame, text='Results: ')
        self.result_label = tkinter.Label(self.middle_frame, textvariable=self.value)

        # pack Middle frame
        self.info.pack(side='left')
        self.result_label.pack(side='left')

        # buttons for bottom frame
        self.search_button = tkinter.Button(self.bottom_frame, text='Search', command=self.search)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        # pack bottom frame
        self.search_button.pack(side='left')
        self.back_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def search(self):
        name = self.search_entry.get()
        result = self.customers.get(name, 'Not Found')
        self.value.set(result)

    def back(self):
        self.look.destroy()


def main():
    # create a window
    root = tkinter.Tk()
    # call the GUI and send it the root menu
    # use _ as variable name because the variable will not be needed after instantiating GUI
    # the GUI itself will handles the remaining program logic
    _ = CrudGUI(root)
    # control the mainloop from main instead of the class
    root.mainloop()


main()
