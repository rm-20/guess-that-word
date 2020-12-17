# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.simpledialog import askstring
import time
from IPython.display import clear_output

class NewGame:
    def __init__(self,master):
        self.master = master #makes window
        self.master.geometry("500x500+0+0")
        self.new_frame = Frame(self.master, height = 10, width = 10)
        self.welcome_msg()    
        
    def start_game(self):
        self.new_frame.destroy()
        name1 = Label(self.master, text = "Player 1 name: ")
        name1.grid(row = 1, column= 1, sticky = W, pady = 2) 
        
        self.n1 = Entry(self.master)
        self.n1.grid(row = 1, column = 2, sticky = W, pady = 2)
        
        name2 = Label(self.master, text = "Player 2 name: ")
        name2.grid(row = 2, column= 1, sticky = W, pady = 2)
        
        self.n2 = Entry(self.master)
        self.n2.grid(row = 2, column = 2, sticky = W, pady = 2)
        
        name_btn = Button(self.master,text = "Submit Name",command = self.get_name)
        name_btn.grid(row = 4, column = 1, sticky = W, pady = 2)       
        
    def get_name(self): 
        greeting = Label(self.master,text = "Hello {} and {}".format(self.n1.get(),self.n2.get()))
        greeting.grid(row = 5, column = 1, sticky = W, pady = 2)
        
        self.get_word()
        
    def get_word(self):      
        word_request = Label(self.master, text = "{} please enter word: ".format(self.n1.get()))
        word_request.grid(row = 6 , column= 1, sticky = W, pady = 2)
        
        self.word_entry = Entry(self.master)
        self.word_entry.grid(row = 6, column = 2, sticky = W, pady = 2)
        
        word_btn = Button(self.master, text = "Submit word", command = self.guess_word)
        word_btn.grid(row = 6, column = 3,sticky = W, pady = 2)

    def guess_word(self):
        self.stored_word = self.word_entry.get()
        self.word_entry.delete(0,END)
        
        guess_command =  "Okay {}, guess {}'s word".format(self.n2.get(),self.n1.get())
        
        turns = len(self.stored_word) + 1
        
        for x in range(turns):       
            self.guess_entry = simpledialog.askstring(guess_command, 'Enter letters', parent = self.master)

            if self.guess_entry in self.stored_word:
                print(self.guess_entry)
                print("good")
            elif self.guess_entry not in self.stored_word:
                print("bad")
        
    def welcome_msg(self):
        self.new_frame
        self.new_frame.grid(row=0,column = 0,sticky = W, pady = 2)
        welcome_msg = Label(self.new_frame, text = "Welcome to Guess that Word")
        welcome_msg.grid(row = 1, column = 1, sticky = W, pady = 2)
        
        begin_btn = Button(self.new_frame,text = "Begin",command = self.start_game)
        begin_btn.grid(row = 2, column = 1, sticky = W, pady = 2)

window = Tk()
newgame = NewGame(window)
window.mainloop()        


    
    

    

