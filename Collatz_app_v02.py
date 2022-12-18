""" button SHOW:
            > testing input: tets_ input
            > creating output: to_screen
                        > calculation with algorithem: collatz_alg
                        > data to text box
                        > temporary png file with plot to label box

    button SAVE:
            > create a csv file by taking a copy of the text box
            > saving temporary png file with appropriate name

by hal.berkers@gmail.com  13-09-2021"""

import os
import shutil
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_b
from tkinter.scrolledtext import ScrolledText
from PIL import ImageTk
import matplotlib.pyplot as plt

root = tk.Tk()
root.attributes('-fullscreen', False)
root.title('Collatz algorithem by hal.berkers@gmail.com')

pad_csv = "c:/users/public/Collatz/csv"                         # folder with data
pad_png = "c:/users/public/Collatz/png"                         # folder with plots
begin_getal = 0


def collatz_alg(g_):
    """ Collatz conjecture, algorithm """
    i_ = 0                              # de teller voor aantal iteraties
    m_ = g_                             # de maximale waarde
    w_ = [g_]                           # een lege lijst

    while g_ != 1:
        if (g_ % 2) == 0:               # mod 2 test, wanneer geen rest (=0) dan is het even
            g_ = int(g_ / 2)            # regel algoritme: bij even delen door 2
            i_ += 1                     # teller voor aantal iteraties
        else:                           # en anders (getal_ % 2) == 1 dus oneven
            g_ = int(3 * g_ + 1)        # regel algoritme: bij oneven dan 3x + 1
            i_ += 1                     # teller voor aantal iteraties

        if g_ > m_:                     # hier wordt bijgehouden wat de maximale waarde is
            m_ = g_                     # nieuwe max
        w_.append(g_)                   # getal aan lijst toevoegen
    return i_, m_, w_                   # output !!!


def test_input():
    """ check input and manage output to screen """
    try:
        # important, don't change!'
        global begin_getal
        begin_getal = int(getal_in.get())
        if begin_getal <= 1:
            error_(1)
        if begin_getal > 999999999999999:
            error_(2)
    except:
        error_(3)
    else:
        pass


def to_screen():
    """ display the results and the graph """
    if 1 < begin_getal <= 1000000000000000:
        i_, m_, w_ = collatz_alg(begin_getal)                   # calling algorithem

        tekst_ = "start number: " + str(begin_getal) + "\n"
        tekst_ += "iterations:   " + str(i_) + "\n"
        tekst_ += "maximum:      " + str(m_) + "\n"
        tekst_ += " \n"
        for i_ in w_:
            tekst_ += (str(i_) + "\n")
            S_t.delete("1.0", "end")                            # clear text-box
            S_t.configure(state='normal')                       # enable editing
        S_t.insert("1.0", tekst_)                               # put content in text box
        S_t.configure(state='disabled')                         # disable editing
        getal_in.delete(0, 'end')                               # clear input
        bt_save.state(["!disabled"])                            # enable button

        # build the graph and show it in the label-box
        titel_ = "start number " + str(begin_getal)
        plt.suptitle(titel_)
        plt.xlabel('iterations')
        plt.ylabel('values')
        plt.plot(w_)
        plt.savefig("tmp.png")
        plt.close()
        img_ = ImageTk.PhotoImage(file="tmp.png")
        lb_photo.configure(image=img_)
        lb_photo.image = img_


def to_csv():
    """ store the content of the text box in a csv file """
    naam_ = "/Collatz_" + str(begin_getal) + ".csv"
    # flag for existence folder
    folder_ = os.path.exists(pad_csv)

    if not folder_:
        os.makedirs(pad_csv)
        message_(1)

    text_S_t = S_t.get("1.0", "end-1c")
    with open(pad_csv + naam_, 'w') as f:
        for i_ in text_S_t:
            f.write(str(i_))


def to_png():
    """ store the results as a plot in a png file """
    naam_ = "/Collatz_" + str(begin_getal) + ".png"
    # flag for existence folder
    folder_ = os.path.exists(pad_png)

    if not folder_:
        os.makedirs(pad_png)
        message_(2)

    dst_ = pad_png + naam_
    shutil.copyfile("tmp.png", dst_)


def message_(m_n):
    """ info messages """
    if m_n == 1:
        m_b.showinfo("Info:", "New folder: " + pad_csv)
    if m_n == 2:
        m_b.showinfo("Info:", "New folder: " + pad_png)
    if m_n == 3:
        m_b.showinfo("Info:", "Data saved as Collatz_"
                              + str(begin_getal) + ".csv en Collatz_"
                              + str(begin_getal) + ".png")


def error_(f_n):
    """ error messages """
    if f_n == 1:
        m_b.showerror("Fout:", "Number must be integer and > 1 !")
    if f_n == 2:
        m_b.showerror("Fout:", "Input less then 1.000.000.000.000.000!")
    if f_n == 3:
        m_b.showerror("Fout:", "No correct input!")
    getal_in.delete(0, 'end')


def show_click():                                               # program flow
    test_input()
    to_screen()
    getal_in.focus()


def save_click():                                               # program flow
    to_csv()
    to_png()
    message_(3)


def stop_click():                                               # program flow
    os.abort()


frame_1 = tk.Frame(root)
frame_1.pack()
frame_2 = tk.Frame(root)
frame_2.pack()
frame_3 = tk.Frame(root)
frame_3.pack()
frame_4 = tk.Frame(root)
frame_4.pack()


label_1 = tk.Label(frame_1)                                     # label page, frame 1
label_1.config(
    text='-Collatz algorithem-',
    font=('Helvetica 14 bold'), bg='light green')
label_1.pack(ipadx=0, ipady=3)


separator = ttk.Separator(                                      # separation line, frame 1
    frame_1,
    orient='horizontal')
separator.pack(fill='x', ipady=5)


lb_in = tk.Label(frame_2)                                       # label input box, frame 2
lb_in.config(
    text="Integer number > 1: ",
    font=('Helvetica 10 bold'))
lb_in.pack(side=tk.TOP)


getal_ = tk.StringVar()                                         # input box, frame 2
getal_in = ttk.Entry(
    frame_2,
    textvariable=getal_,
    justify='center')
getal_in.pack(side=tk.TOP)


separator = ttk.Separator(                                      # separation line, frame 2
    frame_3,
    orient='horizontal')
separator.pack(ipady=5)


bt_show = ttk.Button(                                           # button SHOW, frame 3
    frame_3,
    text="show",
    command=show_click)
bt_show.pack(side=tk.LEFT)


bt_save = ttk.Button(                                           # button SAVE, frame 3
    frame_3,
    text='save',
    command=save_click)
bt_save.pack(side=tk.LEFT)


bt_stop = ttk.Button(                                           # button STOP, frame 3
    frame_3,
    text='STOP',
    command=stop_click)
bt_stop.pack(side=tk.LEFT)


lb_photo = tk.Label(                                            # label plot output, frame 4
    frame_4,
    bd=10,
    relief="flat")
lb_photo.pack(side=tk.TOP, expand=True)


S_t = ScrolledText(                                             # text box output, frame 4
    frame_4,
    width=36, height=18, bd=10,
    relief="groove")
S_t.pack(side=tk.TOP, expand=False)


separator = ttk.Separator(                                      # separation line, frame 4
    frame_4,
    orient='horizontal')
separator.pack(ipady=5)


S_t.insert("1.0", "The Collatz (1910-1990) conjecture:\n" +     # put content in text box
           "-----------------------\n" +
           "if x is even: x/2\n" +
           "if x is odd:  x*3 + 1\n \n" +
           "          (by hal.berkers@gmail.com)")


getal_in.focus()
bt_save.state(["disabled"])

root.mainloop()
