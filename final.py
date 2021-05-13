from tkinter import *
from tkinter import messagebox
import random
import os
import pickle
import player
import random
from tkinter import font as tkFont

game_Play = []
question = []
answer = []
index = 0
attempts = 5

userName = ""

def start_Program():
    global attempts
    global userName
    if button1.cget('text') == "Start":
        #print("It is Start")
        if entry.get() == "":
            start_clicker()
            print("Error: Name field empty")
            return
        else:
            userName = entry.get()
            load_User(entry.get())
            button3.pack(pady=2)
            label_Name.config(text = "Hello, "+ entry.get())
            load_File()
            #print(len(question))
            load_Question()
            button1.config(text = "Submit")
        
    elif button1.cget('text') == "Submit":
        #print("It is Submit")
        if answer[index].lower() == (" "+entry.get().lower()+"\n"):
            #print("True")
            for match in game_Play:
                match.set_wins()
            label_RW.config(text = "Correct", bg="green")
        else:
            for match in game_Play:
                match.set_loses()
            attempts = attempts - 1
            label_Lives.config(text= str(attempts))
            label_RW.config(text = ("Incorrect. Answer: " + answer[index]), bg="red")

        if attempts <=0:
            root.destroy()
            
        load_Question()

def load_Question():
    global index
    entry.delete(0,END)
    entry.insert(0,"")
    index = random.randint(0,17)
    label_Q.config(text= question[index])
    
def load_File():
    file1 = open('questions.txt', 'r')
    Lines = file1.readlines()
    for line in Lines:
        trivia = line.split(",")
        question.append(trivia[0])
        answer.append(trivia[1])
    
def load_User(name):
    file = str(name)+ ".rps"
    if (os.path.exists(file)):
        f = open(file,"rb")
        load_User = pickle.load(f)
        #print("Loaded -> " + str(load_User.get_name()) + str(load_User.get_wins()))
        game_Play.append(load_User)
        f.close()
        print("Success")
    else:
        user = player.player(name)
        game_Play.append(user)
        f = open(file,"x")
        f.close()

        f = open(file, "wb")
        pickle.dump(user, f)
        f.close()
   
root = Tk()

root.geometry("600x450")

photo = PhotoImage(file = "background.png") 

theLabel = Label(root, image=photo)
theLabel.place(x = 0, y = 0)
#theLabel.loop()

title_Font = tkFont.Font(family='Helvetica', size=28, weight=tkFont.BOLD)

myFont = tkFont.Font(size=10)

label_Title = Label( root, text = "Random Trivia.", font = title_Font, fg="#b5179e")
label_Title.pack(pady = 40)

label_Name = Label( root, font = myFont)
label_Name.pack(pady = 10)

frame = Frame(root)
frame.pack(pady = 20 )


label_Q = Label(root, text = "Name: ")
label_Q.pack(pady = 10)

entry = Entry(root)
entry.pack(pady = 10)

button1 = Button(frame,text="Start",command=start_Program, width = 5, height = 1, font = myFont)
button1.pack(pady = 3)

def start_choice(option):
    if option == "cancel":
        save_Player_Game()
        start_pop.destroy()
        root.destroy()
    elif option == "ok":
        start_pop.destroy()
        return

def start_clicker():
    global start_pop
    start_pop = Toplevel(root)
    start_pop.title("Missing Name")
    start_pop.geometry("250x150")
    start_pop.config(bg="#b5179e")

    pop_Label = Label(start_pop, text="You need to enter your name", bg="#b5179e", fg="black" )
    pop_Label.pack(pady=10)

    start_Frame = Frame(start_pop, bg="#b5179e")
    start_Frame.pack(pady=5)

    ok = Button(start_Frame, text="OK", command= lambda: start_choice("ok"), bg="#a01a58")
    ok.grid(row=0,column=1)
    cancel = Button(start_Frame, text="Cancel", command= lambda: start_choice("cancel"), bg="#5f0f40")
    cancel.grid(row=0, column=2)

label_Lives = Label(root, text = "5")
label_Lives.pack(pady = 5)

label_RW = Label(root)
label_RW.pack(pady = 5)


#Source code: https://www.youtube.com/watch?v=tpwu5Zb64IQ&ab_channel-Codemy.com
def choice(option):
    if option == "yes":
        save_Player_Game()
        pop.destroy()
        root.destroy()
    elif option == "no":
        pop.destroy()
        return

def clicker():
    global pop
    pop = Toplevel(root)
    pop.title("EXIT")
    pop.geometry("250x150")
    pop.config(bg="#b5179e")

    pop_Label = Label(pop, text="Would you like to proceed?", bg="#b5179e", fg="black" )
    pop_Label.pack(pady=10)

    my_Frame = Frame(pop, bg="#b5179e")
    my_Frame.pack(pady=5)

    yes = Button(my_Frame, text="Yes", command= lambda: choice("yes"), bg="#a01a58")
    yes.grid(row=0,column=1)
    no = Button(my_Frame, text="No", command= lambda: choice("no"), bg="#5f0f40")
    no.grid(row=0, column=2)

def close_Window():
    pop_Stats.destroy()

def my_Stats():
    wins = ""
    loses = ""
    for match in game_Play:
        wins = wins + "Correct: " + str(match.get_wins())
        loses = loses + "Incorrect: " + str(match.get_loses())

    global pop_Stats
    pop_Stats = Toplevel(root)
    pop_Stats.title("EXIT")
    pop_Stats.geometry("250x150")
    pop_Stats.config(bg="#b5179e")

    pop_Stats_Label1 = Label(pop_Stats, text= wins, bg="#b5179e", fg="black" )
    pop_Stats_Label1.pack(pady=10)


    pop_Stats_Label2 = Label(pop_Stats, text= loses, bg="#b5179e", fg="black" )
    pop_Stats_Label2.pack(pady=10)
    
    stats_Frame = Frame(pop_Stats, bg="#b5179e")
    stats_Frame.pack(pady=5)
    
    close = Button(stats_Frame, text="Close", command= close_Window, bg="#a01a58")
    close.grid(row=0,column=1)

    
button2 = Button(frame,text="End",command=clicker, width = 5, height = 1, font = myFont)
button2.pack(pady=2)

button3 = Button(frame,text="Stats",command=my_Stats, width = 5, height = 1, font = myFont)

def save_Player_Game():
    file = str(userName)+ ".rps"
    for match in game_Play:
        f = open(file, "wb")
        pickle.dump(match, f)
        f.close()
        
root.mainloop()   
