import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Label, Entry
from datetime import datetime
from tkinter import Tk, Text
from tkinter import *
from Person import Person
import pickle
import os

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('Information manager')
        self.geometry('1280x1080')

        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)


        # label first name
        self.fname_label = ttk.Label(self, text='First name')
        self.fname_label.grid(column=0, row=0)
        
        # label second name
        self.sname_label = ttk.Label(self, text='Second name')
        self.sname_label.grid(column=0, row=1)
        
        # label  bday
        self.bday_label = ttk.Label(self, text='Birthday, in dd/mm/yyyy')
        self.bday_label.grid(column=0, row=2)

        # label email
        self.email_label = ttk.Label(self, text='Email')
        self.email_label.grid(column=0, row=3)


        # entry first name
        self.fn = tk.StringVar()
        self.fname_entry = ttk.Entry(self, textvariable=self.fn)
        self.fname_entry.grid(column=1, row=0,)
        
        # entry surname 
        self.sn = tk.StringVar()
        self.sname_entry = ttk.Entry(self, textvariable=self.sn)
        self.sname_entry.grid(column=1, row=1)
        
        # entry  bd
        self.bd = tk.StringVar()
        self.bday_entry = ttk.Entry(self, textvariable=self.bd)
        self.bday_entry.grid(column=1, row=2)

        # label email
        self.em = tk.StringVar()
        self.email_entry = ttk.Entry(self, textvariable=self.em)
        self.email_entry.grid(column=1, row=3)


        # Add new person
        self.add_button = ttk.Button(self, text='Add ')
        self.add_button['command'] = self.Add_Dude
        self.add_button.grid(column=3, row=0)
        
        
        # Delete last person
        self.del_button = ttk.Button(self, text='Delete ')
        self.del_button['command'] = self.Del_Dude
        self.del_button.grid(column=3, row=1)

        # Save all
        self.save_button = ttk.Button(self, text='Save ')
        self.save_button['command'] =  self.Save_Dudes
        self.save_button.grid(column=3, row=2)
        
        # Upload binary
        self.upl_button = ttk.Button(self, text='Upload binary ')
        self.upl_button['command'] =  self.Upload_Dudes
        self.upl_button.grid(column=3, row=3 )

        # Create a treeview
        # define columns
        columns = ('First_name', 'Surname', 'Birthday','Email')

        self.tree = ttk.Treeview(self, columns=columns, show='headings')
        # define headings
        self.tree.heading('First_name', text='First Name')
        self.tree.heading('Surname', text='Surname')
        self.tree.heading('Birthday', text='Birthday')
        self.tree.heading('Email', text='Email')
        self.tree.grid(column=2, row=1, sticky=E)
    
   
    def Add_Dude(self):
        """Append a new entry"""
        global dudes
        # Create a new instance
        dude = Person(
            self.fname_entry.get(),
            self.sname_entry.get(),
            datetime.strptime(self.bday_entry.get(), '%d/%m/%Y').date(),
            self.email_entry.get()
            )  
        # append to list
        dudes.append(dude)
        
        # Display the text 
        self.tree.update()
        self.tree.insert('', tk.END, values=(dude.Fname, dude.Surname, dude.Birthday,dude.Email ))
        self.tree.update() 
    
     

    def Del_Dude(self):
       """Delete the last entry"""
       global dudes

      
       selected_item = self.tree.selection()[0] ## get selected item
       
       dudes.pop(self.tree.index(selected_item))
       self.tree.delete(selected_item)
       self.tree.update()
       

    def Save_Dudes(self):
        """Save results"""
        global dudes

        # save txt
        with open('data.txt', 'w') as f:
                  for dude in dudes:
                        f.write(str(dude))
                        f.write('\n')
        # save binary                      
        with open('dudes.bin', 'wb') as fid:
           pickle.dump(dudes, fid)  
    
    def Upload_Dudes(self):
        """ Upload the saved binary  """
        #check if binary exists
        if os.path.isfile('dudes.bin'):
            global dudes
            with open('dudes.bin', 'rb') as fid:
                    databin = pickle.load(fid)
            dudes = databin
            # Display the text
            self.tree.delete(*self.tree.get_children())
            self.tree.update()
            for i in range(len(databin)):
                self.tree.insert('', tk.END, values=(databin[i].Fname, databin[i].Surname, databin[i].Birthday,databin[i].Email ))
            self.tree.update()  

    
#  Create an empty list to store the data(global)
dudes = []
 
  
# Uncomment lines below to call App within this script.
    
#if __name__ == "__main__":
  #Create an empty list
 # dudes = []
 # app = App()
  #app.mainloop()



