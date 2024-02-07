''' tkinter GUI Module'''
from distutils.cmd import Command
from tkinter import *                        # * represent import tkinter all function.
from turtle import width            
def tkinter_test():    
    
    def show_msg():
        print("Touch button.")
        data1['text'] = entry1.get() + ' ' + entry2.get() + ' ' + entry3.get()
        data1['fg'] = 'red'
    
    windows = Tk()                           # Tk()       function is cell GUI windows.
    windows.geometry('600x400')              # geometry() function is windows size,but need to use 'x'.    
    windows.title('VIP information system')  # title()    function is windows title.

    #label() is field function.
    # All the element need pack or grid.
    label1 = Label(windows, text = 'VIP information system', font = 'Arial 15', fg = 'green', bg = 'light green')  
    label1.grid(column = 0, row = 0)                                               

    id1 = Label(windows, text = 'ID', font = 'Arial 15', width = '10', bg = 'light yellow')
    id1.grid(column = 0, row = 1 ) 
    entry1 = Entry(windows, fg = 'green')
    entry1.grid(column = 1, row = 1)
    
    name1 = Label(windows, text = 'Name', font = 'Arial 15', width = '10', bg = 'light yellow')
    name1.grid(column = 0, row = 2 ) 
    entry2 = Entry(windows, fg = 'green')
    entry2.grid(column = 1, row = 2)
    
    tel1 = Label(windows, text = 'Tel', font = 'Arial 15', width = '10', bg = 'light yellow')
    tel1.grid(column = 0, row = 3 ) 
    entry3 = Entry(windows, fg = 'green')
    entry3.grid(column = 1 ,row = 3)
    
    data1 = Label(windows, text = 'Your data', font = 'Arial 15', width = '20', bg = 'light yellow')
    data1.grid(column = 1, row = 4 ) 


    button1 = Button(windows, text = 'Confirm', font = 'Arial 15', width = '10', command = show_msg)
    button1.grid(column = 2, row = 1)
    button2 = Button(windows, text = 'Cancel', font = 'Arial 15', width = '10')
    button2.grid(column = 2, row = 2)
    button3 = Button(windows, text = 'Exit', font = 'Arial 15', width = '10', command = windows.destroy)
    button3.grid(column = 2, row = 3)
    
    windows.mainloop()  # mainloop() function is GUI windows loop.
    
tkinter_test()