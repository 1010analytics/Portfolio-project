from tkinter import *

root= Tk()
root.geometry("500x500")
root.title("Tic Tac Toe")

frame1=Frame(root)
frame1.pack()
titleLabel=Label(frame1, text= "Tic Tac Toe", font=("Arial",30), bg="yellow")
titleLabel.pack()

frame2=Frame(root)
frame2.pack()

img= PhotoImage(file="C:\\Users\\shakshi ji\\Desktop\\web_scrap\\i1.png")
root.iconphoto(False, img)

## storing the turn of the player to judge the winner:
testboard={1:" ", 2:" ", 3:" ",
           4:" ", 5:" ", 6:" ",
           7:" ", 8:" ", 9:" "}

turn="x"

def CheckForWin(player):

## for rows
    if testboard[1]==testboard[2] and testboard[2]==testboard[3] and testboard[3]==player:
        return True
    elif testboard[4]==testboard[5] and testboard[5]==testboard[6] and testboard[6]==player:
        return True
    elif testboard[7]==testboard[8] and testboard[8]==testboard[9] and testboard[9]==player:
        return True
    
## for columns
    elif testboard[1]==testboard[4] and testboard[4]==testboard[7] and testboard[7]==player:
        return True
    elif testboard[2]==testboard[5] and testboard[5]==testboard[8] and testboard[8]==player:
        return True
    elif testboard[3]==testboard[6] and testboard[6]==testboard[9] and testboard[9]==player:
        return True
    
## diagonals    
    elif testboard[1]==testboard[5] and testboard[5]==testboard[9] and testboard[9]==player:
        return True
    elif testboard[3]==testboard[5] and testboard[5]==testboard[7] and testboard[7]==player:
        return True
    
    return False
    
def play(event):
    global turn

    button= event.widget
    button_tracing= str(button)
    clicked_button= button_tracing[-1]
    print(clicked_button)
    if clicked_button=="n":
        clicked_button=1
    else:
        clicked_button=int(clicked_button)


    if button["text"]==" ":
        if turn== "x" :
            button['text']= "x"
            testboard[clicked_button]=turn
            if CheckForWin(turn):
                winningLabel = Label(frame2, text=f"{turn} wins the game", bg="orange", font=("Arial", 35))
                winningLabel.grid(row= 3, column=0, columnspan=3)
            turn="o"

        else:
            button["text"]="o"
            testboard[clicked_button]=turn
            if CheckForWin(turn):
                winningLabel = Label(frame2, text=f"{turn} wins the game", bg="orange", font=("Arial", 35))
                winningLabel.grid(row= 3, column=0, columnspan=3)
            turn="x"

    print(testboard)
    


# Tic Tac Toe buttons:
# first row
button1= Button(frame2, text=" ", width=4 , height=2, font=("Arial", 30), bg="green", relief= RAISED, borderwidth=5)
button1.grid(row=0, column=0)
button1.bind("<Button-1>", play)

button2= Button(frame2, text=" ", width=4 , height=2, font=("Arial", 30), bg="green", relief= RAISED, borderwidth=5)
button2.grid(row=0, column=1)
button2.bind("<Button-1>", play)

button3= Button(frame2, text=" ",  width=4 , height=2, font=("Arial", 30), bg="green", relief= RAISED, borderwidth=5)
button3.grid(row=0, column=2)
button3.bind("<Button-1>", play)
# second row
button4= Button(frame2, text=" ",  width=4 , height=2, font=("Arial", 30), bg="green", relief= RAISED, borderwidth=5)
button4.grid(row=1, column=0)
button4.bind("<Button-1>", play)

button5= Button(frame2, text=" ",  width=4 , height=2, font=("Arial", 30), bg="green", relief= RAISED, borderwidth=5)
button5.grid(row=1, column=1)
button5.bind("<Button-1>", play)

button6= Button(frame2, text=" ", width=4 , height=2, font=("Arial", 30), bg="green", relief= RAISED, borderwidth=5)
button6.grid(row=1, column=2)
button6.bind("<Button-1>", play)

# third row
button7= Button(frame2, text=" ", width=4 , height=2, font=("Arial", 30), bg="green", relief= RAISED, borderwidth=5)
button7.grid(row=2, column=0)
button7.bind("<Button-1>", play)

button8= Button(frame2, text=" ",  width=4 , height=2, font=("Arial", 30), bg="green", relief= RAISED, borderwidth=5)
button8.grid(row=2, column=1)
button8.bind("<Button-1>", play)

button9= Button(frame2, text=" ", width=4 , height=2, font=("Arial", 30), bg="green", relief= RAISED, borderwidth=5)
button9.grid(row=2, column=2)
button9.bind("<Button-1>", play)








root.mainloop()