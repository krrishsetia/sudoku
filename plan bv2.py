import tkinter
import tkinter.ttk
import tkinter
from random import *
import numpy as np
from PIL import Image, ImageTk

window = tkinter.Tk()
window.geometry("1200x1200")

numList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
textfont = ('Courier New', '15')
window.option_add('*TCombobox*Listbox.font', textfont)


label = tkinter.Label(window,text="welcome to sudoku press start to play",font=('Calibri','30'))
label.pack(pady=20)
image = Image.open("sudoku-Mobile-hero-asset@2x.png")
img_resize = image.resize((500,500))
img = ImageTk.PhotoImage(image=img_resize)
image_label = tkinter.Label(window,image=img)
image_label.pack()

top = tkinter.Frame(window)
top.pack(pady=20)


def start():
    label.destroy()
    image_label.destroy()
    a.destroy()
    b = tkinter.Button(window, text="finish", width=30, height=5, command=retrieve_values)
    b.pack(in_=top, side=tkinter.LEFT)
    button()

def button():
    global values
    global num
    global num2
    global num3
    num = []
    num2 = []
    num3 = []
    values = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]])
    global grid
    grid = tkinter.Canvas(background="white", height=800, width=800)
    grid.pack()
    values_row = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for row in range(0, 3):
        for col in range(0, 3):
            b = randint(1, 2)
            grid.create_rectangle(0 + (row * 90), 0 + (col * 90), 90 + (row * 90), 90 + (col * 90), outline="black")
            if b == 1:
                grid.create_rectangle(0 + (row * 90), 0 + (col * 90), 90 + (row * 90), 90 + (col * 90), outline="black")
                a = tkinter.ttk.Combobox(grid, values=numList, width=4, font=textfont, height=7)
                a.place(y=0 + (row * 90), x=0 + (col * 90))
                num.append(a)
                num2.append(row)
                num3.append(col)

            else:

                grid.create_rectangle(0 + (row * 90), 0 + (col * 90), 90 + (row * 90), 90 + (col * 90), outline="black")
                rand = choice(values_row)
                a = tkinter.Label(grid, text=rand, background='white', font=textfont)
                a.place(y=5 + (row * 90), x=5 + (col * 90))
                values_row.remove(rand)
                values[col, row] = rand


    values_row = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for row in range(3, 6):
        for col in range(3, 6):
            b = randint(1, 2)
            grid.create_rectangle(0 + (row * 90), 0 + (col * 90), 90 + (row * 90), 90 + (col * 90), outline="black")
            if b == 1:
                grid.create_rectangle(0 + (row * 90), 0 + (col * 90), 90 + (row * 90), 90 + (col * 90), outline="black")
                a = tkinter.ttk.Combobox(grid, values=numList, width=4, font=textfont, height=7)
                a.place(y=0 + (row * 90), x=0 + (col * 90))
                num.append(a)
                num2.append(row)
                num3.append(col)

            else:

                grid.create_rectangle(0 + (row * 90), 0 + (col * 90), 90 + (row * 90), 90 + (col * 90), outline="black")
                rand = choice(values_row)
                a = tkinter.Label(grid, text=rand, background='white', font=textfont)
                a.place(y=5 + (row * 90), x=5 + (col * 90))
                values_row.remove(rand)
                values[col, row] = rand

    values_row = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for row in range(6, 9):
        for col in range(6, 9):
            b = randint(1, 2)
            grid.create_rectangle(0 + (row * 90), 0 + (col * 90), 90 + (row * 90), 90 + (col * 90), outline="black")
            if b == 1:
                grid.create_rectangle(0 + (row * 90), 0 + (col * 90), 90 + (row * 90), 90 + (col * 90), outline="black")
                a = tkinter.ttk.Combobox(grid, values=numList, width=4, font=textfont, height=7)
                a.place(y=0 + (row * 90), x=0 + (col * 90))
                num.append(a)
                num2.append(row)
                num3.append(col)

            else:

                grid.create_rectangle(0 + (row * 90), 0 + (col * 90), 90 + (row * 90), 90 + (col * 90), outline="black")
                rand = choice(values_row)
                a = tkinter.Label(grid, text=rand, background='white', font=textfont)
                a.place(y=5 + (row * 90), x=5 + (col * 90))
                values_row.remove(rand)
                values[col, row] = rand

    for i in range(6):
        values_row = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        place_col = 0
        place_row = 0
        if i == 0:
            place_col += 3
            place_row = 0
        elif i == 1:
            place_col += 6
            place_row = 0
        elif i == 2:
            place_col = 0
            place_row += 3
        elif i == 3:
            place_col += 6
            place_row += 3
        elif i == 4:
            place_col = 0
            place_row += 6
        elif i == 5:
            place_col += 3
            place_row += 6

        for row in range(3):
            for col in range(3):
                b = randint(1, 2)
                grid.create_rectangle(0 + ((col + place_col) * 90), 0 + ((row + place_row) * 90),
                                      90 + ((col + place_col) * 90), 90 + ((row + place_row) * 90), outline="black")
                if b == 1:
                    grid.create_rectangle(0 + ((col + place_col) * 90), 0 + ((row + place_row) * 90),
                                          90 + ((col + place_col) * 90), 90 + ((row + place_row) * 90), outline="black")
                    a = tkinter.ttk.Combobox(grid, values=numList, width=4, font=textfont, height=7)
                    a.place(y=0 + ((row + place_row) * 90), x=0 + ((col + place_col) * 90))
                    num.append(a)
                    num2.append((row + place_row))
                    num3.append((col + place_col))

                else:

                    grid.create_rectangle(0 + ((col + place_col) * 90), 0 + ((row + place_row) * 90),
                                          90 + ((col + place_col) * 90), 90 + ((row + place_row) * 90), outline="black")
                    if len(values_row) == 0:
                        a = tkinter.ttk.Combobox(grid, values=numList, width=4, font=textfont, height=7)
                        a.place(y=0 + ((row + place_row) * 90), x=0 + ((col + place_col) * 90))
                        num.append(a)
                        num2.append((row + place_row))
                        num3.append((col + place_col))
                    else:
                        rand = choice(values_row)
                        no_values_possible = False
                        values_grid = values_row
                        for k in range(9):
                            for x in range(9):
                                check_row = values[:, k]
                                check_col = values[x, :]
                                for l in range(len(values_grid)):
                                    if values_grid[l] == check_row[k]:
                                        values_grid.remove(check_row[k])
                                        break
                                for o in range(len(values_grid)):
                                    if values_grid[o] == check_col[k]:
                                        values_grid.remove(check_col[k])
                                        break
                                if len(values_grid) == 0 :
                                    no_values_possible = True
                                elif k == 8:
                                    rand = choice(values_grid)
                        if no_values_possible == True:
                            a = tkinter.ttk.Combobox(grid, values=numList, width=4, font=textfont, height=7)
                            a.place(y=0 + ((row + place_row) * 90), x=0 + ((col + place_col) * 90))
                            num.append(a)
                            num2.append((row + place_row))
                            num3.append((col + place_col))
                        else:
                            a = tkinter.Label(grid, text=rand, background='white', font=textfont)
                            a.place(y=5 + ((row + place_row) * 90), x=5 + ((col + place_col) * 90))
                            for o in range(len(values_row)):
                                if values_row[o] == rand:
                                    values_row.remove(rand)
                                    break
                            values[(col + place_col), (row + place_row)] = rand


def retrieve_values():
    global c
    global bottom
    c = tkinter.Label(window)
    c.pack()
    correct_order = 0
    for i in range(len(num)):
        values[num3[i], num2[i]] = num[i].get()
    for j in range(9):
        if np.sum(values[:,j]) == 45:
            correct_order += 1
    if correct_order == 9:
        c.configure(text="you have completed the sudoku board",font=('Calibri',25))
        bottom = tkinter.Frame(window)
        bottom.pack()
        exit = tkinter.Button(window,text="exit",command=exit_game,width=15,height=5)
        exit.pack(in_=bottom,side=tkinter.LEFT)
        play_again = tkinter.Button(window,text="play again?",command=play,width=15,height=5)
        play_again.pack(in_=bottom,side=tkinter.LEFT)
    else:
        c.configure(text="there is a value where there is not supposed to be one",font=('Calibri',25))
def play():
    grid.destroy()
    c.destroy()
    bottom.destroy()
    button()

def exit_game():
    window.destroy()

a = tkinter.Button(window, text="start", width=30, height=5, command=start)
a.pack(in_=top, side=tkinter.LEFT)

window.mainloop()