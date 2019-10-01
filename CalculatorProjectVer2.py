#!/usr/bin/python3
from tkinter import *

class Application(Frame):
    """Build the basic window frame template"""
    
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        
        self.entry1 = Entry(self, width= 30, borderwidth=10)
        self.entry1.grid(row=0, column = 0, columnspan = 5, padx=5, pady=5)
        
        ######defined Buttons######
        
        #Bottom row of button
        self.button1 = Button(self, text='1',padx= 30, pady= 15, command=lambda:self.display(1))
        self.button1.grid(row=3, column=0)
        self.button2 = Button(self, text='2',padx= 30, pady= 15, command=lambda:self.display(2))
        self.button2.grid(row=3, column=1)
        self.button3 = Button(self, text='3',padx= 30, pady= 15, command=lambda:self.display(3))
        self.button3.grid(row=3, column=2)
        
        #Mid row of Buttons
        self.button4 = Button(self, text='4',padx= 30, pady= 15, command=lambda:self.display(4))
        self.button4.grid(row=2, column=0, sticky=NE)
        self.button5 = Button(self, text='5',padx= 30, pady= 15, command=lambda:self.display(5))
        self.button5.grid(row=2, column=1, sticky=N)
        self.button6 = Button(self, text='6',padx= 30, pady= 15, command=lambda:self.display(6))
        self.button6.grid(row=2, column=2, sticky=NW)
        
        #TOP row of buttons
        self.button7 = Button(self, text='7',padx= 30, pady= 15, command=lambda:self.display(7))
        self.button7.grid(row=1, column=0)
        self.button8 = Button(self, text='8',padx= 30, pady= 15, command=lambda:self.display(8))
        self.button8.grid(row=1, column=1)
        self.button9 = Button(self, text='9',padx= 30, pady= 15, command=lambda: self.display(9))
        self.button9.grid(row=1, column=2)
        
        self.button0 = Button(self, text='0',padx= 30, pady= 15, command=lambda:self.display(0))
        self.button0.grid(row=4, column=0, sticky=SW)
        
        ########Adding subtracting Division & Multiply########
        self.button_add = Button(self, text='+',padx= 30, pady= 15, command=self.button_add)
        self.button_subtract = Button(self, text='-',padx= 30, pady= 15, command=self.button_subtract)
        self.button_divison = Button(self, text='/',padx= 30, pady= 15, command=self.button_divison)
        self.button_multi = Button(self, text='x',padx= 30, pady= 15, command=self.button_multi)
        
        self.button_add.grid(row=3, column= 3)
        self.button_subtract.grid(row=2, column= 3)
        self.button_divison.grid(row=4, column= 3)
        self.button_multi.grid(row=1, column= 3)
        
        ########Removal of numbers and Equals###########
        self.button_clear = Button(self, text='C',padx= 30, pady= 15, command=self.button_clear)
        self.button_equals = Button(self, text='=',padx= 30, pady= 15, command=self.button_equals)
        
        self.button_clear.grid(row=4, column= 1)
        self.button_equals.grid(row=4, column= 2)
        
        
    ####Removes and number so it doesnt add the previous number into the applcation########
        
    def display(self, number):
        current = self.entry1.get()
        self.entry1.delete(0, END)
        self.entry1.insert(0, str(current) + str(number))
        
        
    def button_clear(self):
        self.entry1.delete(0, END)
        
        
    def button_add(self):
        first_number = self.entry1.get()
        global f_num
        global math
        math = "addition"
        f_num = int(first_number)
        self.entry1.delete(0, END)
        
    def button_equals(self):
        second_number = self.entry1.get()
        self.entry1.delete(0, END)
        
        if math == "addition":
            self.entry1.insert(0, f_num +int(second_number))       
        
        if math == "subtraction":
            self.entry1.insert(0, f_num -int(second_number))
            
        if math == "multiplication":
            self.entry1.insert(0, f_num *int(second_number))
            
        if math == "division":
            self.entry1.insert(0, f_num /int(second_number))


    ####### Buttons used to either add, subtract, multiply or divide #######
    
    
    def button_subtract(self):
        first_number = self.entry1.get()
        global f_num
        global math
        math = "subtraction"
        f_num = int(first_number)
        self.entry1.delete(0, END)
    
    def button_multi(self):
        first_number = self.entry1.get()
        global f_num
        global math
        math = "multiplication"
        f_num = int(first_number)
        self.entry1.delete(0, END)
    
    def button_divison(self):
        first_number = self.entry1.get()
        global f_num
        global math
        math = "division"
        f_num = int(first_number)
        self.entry1.delete(0, END)

root = Tk()
root.title('Basic Calculator')
root.geometry('305x310')
app = Application(root)
app.mainloop()