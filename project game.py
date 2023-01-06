from random import randrange
from tkinter import *
from tkinter import Tk
import random
from turtle import *
from freegames import square, vector

tkWindow = Tk()
tkWindow.geometry('500x400')
tkWindow.title('Python Game Center')
label1 = Label(tkWindow,
               text="Snake Game",
               font="normal 20 bold",
               fg="green").pack(pady=60)
label2 = Label(tkWindow,
               text="Rock Paper Scissor",
               font="normal 20 bold",
               fg="blue").pack(pady=60)


def showMsg1():
    food = vector(0, 0)
    snake = [vector(10, 0)]
    aim = vector(0, -10)

    def change(x, y):
        """Change snake direction."""
        aim.x = x
        aim.y = y

    def inside(head):
        """Return True if head inside boundaries."""
        return -200 < head.x < 190 and -200 < head.y < 190

    def move():
        """Move snake forward one segment."""
        head = snake[-1].copy()
        head.move(aim)

        if not inside(head) or head in snake:
            square(head.x, head.y, 9, 'red')
            update()
            return

        snake.append(head)

        if head == food:
            print('Snake:', len(snake))
            food.x = randrange(-15, 15) * 10
            food.y = randrange(-15, 15) * 10
        else:
            snake.pop(0)

        clear()

        for body in snake:
            square(body.x, body.y, 9, 'black')

        square(food.x, food.y, 9, 'green')
        update()
        ontimer(move, 100)

    setup(420, 420, 370, 0)
    hideturtle()
    tracer(False)
    listen()
    onkey(lambda: change(10, 0), 'Right')
    onkey(lambda: change(-10, 0), 'Left')
    onkey(lambda: change(0, 10), 'Up')
    onkey(lambda: change(0, -10), 'Down')
    move()
    done()


def showMsg2():
    # Create Object
    root = Tk()

    # Set geometry
    root.geometry("1000x500")

    # Set title
    root.title("Rock Paper Scissor Game")

    # Computer Value
    computer_value = {
        "0": "Rock",
        "1": "Paper",
        "2": "Scissor"
    }

    # Reset The Game
    def reset_game():
        b1["state"] = "active"
        b2["state"] = "active"
        b3["state"] = "active"
        l1.config(text="Player			 ")
        l3.config(text="Computer")
        l4.config(text="")

    # Disable the Button
    def button_disable():
        b1["state"] = "disable"
        b2["state"] = "disable"
        b3["state"] = "disable"

    # If player selected rock
    def isrock():
        c_v = computer_value[str(random.randint(0, 2))]
        if c_v == "Rock":
            match_result = "Match Draw"
        elif c_v == "Scissor":
            match_result = "Player Win"
        else:
            match_result = "Computer Win"
        l4.config(text=match_result)
        l1.config(text="Rock		 ")
        l3.config(text=c_v)
        button_disable()

    # If player selected paper
    def ispaper():
        c_v = computer_value[str(random.randint(0, 2))]
        if c_v == "Paper":
            match_result = "Match Draw"
        elif c_v == "Scissor":
            match_result = "Computer Win"
        else:
            match_result = "Player Win"
        l4.config(text=match_result)
        l1.config(text="Paper		 ")
        l3.config(text=c_v)
        button_disable()

    # If player selected scissor
    def isscissor():
        c_v = computer_value[str(random.randint(0, 2))]
        if c_v == "Rock":
            match_result = "Computer Win"
        elif c_v == "Scissor":
            match_result = "Match Draw"
        else:
            match_result = "Player Win"
        l4.config(text=match_result)
        l1.config(text="Scissor		 ")
        l3.config(text=c_v)
        button_disable()

    # Add Labels, Frames and Button
    Label(root,
          text="Rock Paper Scissor",
          font="normal 20 bold",
          fg="blue").pack(pady=20)

    frame = Frame(root)
    frame.pack()

    l1 = Label(frame,
               text="Player			 ",
               font=10)

    l2 = Label(frame,
               text="VS			 ",
               font="normal 10 bold")

    l3 = Label(frame, text="Computer", font=10)

    l1.pack(side=LEFT)
    l2.pack(side=LEFT)
    l3.pack()

    l4 = Label(root,
               text="",
               font="normal 20 bold",
               bg="white",
               width=15,
               borderwidth=2,
               relief="solid")
    l4.pack(pady=20)

    frame1 = Frame(root)
    frame1.pack()

    b1 = Button(frame1, text="Rock",
                font=10, width=7,
                command=isrock)

    b2 = Button(frame1, text="Paper ",
                font=10, width=7,
                command=ispaper)

    b3 = Button(frame1, text="Scissor",
                font=10, width=7,
                command=isscissor)

    b1.pack(side=LEFT, padx=10)
    b2.pack(side=LEFT, padx=10)
    b3.pack(padx=10)

    Button(root, text="Reset Game",
           font=10, fg="red",
           bg="black", command=reset_game).pack(pady=20)

    # Execute Tkinter
    root.mainloop()


button1 = Button(tkWindow,
                 text='Click to Start',
                 command=showMsg2)
button2 = Button(tkWindow,
                 text='Click to Start',
                 command=showMsg1).place(x=200, y=120)
button1.pack()

tkWindow.mainloop()
