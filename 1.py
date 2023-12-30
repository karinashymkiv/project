from tkinter import *
from tkinter import ttk
import random
from tkinter import messagebox as mb
import time

class CatGame:
    def __init__(self):
        self.root = Tk()
        self.root.wm_geometry("+%d+%d" % ((self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2,
                                           (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2))
        self.root.title("CAT")
        icon = PhotoImage(file="D:/iconCat.png")
        self.root.iconphoto(False, icon)
        self.logo = PhotoImage(file="D:/cat.png")
        self.logo1 = Label(image=self.logo)
        self.game = 3
        self.healthCat = 20
        self.leisureCat = 20

        label2 = Label(width=27, height=3, text="It is your Cat", font="Arial")
        b1 = ttk.Button(width=15, text="feed", command=self.health)
        b2 = ttk.Button(width=15, text="caress", command=self.leisure)
        b3 = ttk.Button(width=15, text="train", command=self.health)
        b4 = ttk.Button(width=15, text="play", command=self.leisure)
        b5 = ttk.Button(width=15, text="Exit", command=self.quit_game)
        self.l1 = Label(width=20, height=3, text="health - " + str(self.healthCat) + "%")
        self.l2 = Label(width=20, height=2, text="leisure - " + str(self.leisureCat) + "%")
        self.l3 = Label(width=20, height=2, text="your cat is alive")

        label2.grid(row=0, column=2, columnspan=3, rowspan=2)
        b1.grid(row=2, column=0)
        b2.grid(row=3, column=0)
        b3.grid(row=4, column=0)
        b4.grid(row=5, column=0)
        b5.grid(row=9, column=3)
        self.l1.grid(row=6, column=0)
        self.l2.grid(row=7, column=0)
        self.l3.grid(row=7, column=3)
        self.logo1.grid(row=2, column=2, columnspan=5, rowspan=5)

        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.root.after(1000, self.update_clock)
        self.root.after(1000, self.heppimin)

    def heppimin(self):
        if self.game == 3:
            if self.healthCat <= 0 or self.leisureCat <= 0:
                answer = mb.askyesno(title="You lost", message="Do you want to play again?")
                if answer:
                    self.healthCat += 50
                    self.leisureCat += 50
                else:
                    self.game = 1
            elif self.healthCat >= 100 and self.leisureCat >= 100:
                answer2 = mb.askyesno(title="You win", message="Do you want to play again?")
                if answer2:
                    self.healthCat -= 50
                    self.leisureCat -= 50
                else:
                    self.game += 1

            self.l1.configure(text="health - " + str(self.healthCat) + "%")
            self.l2.configure(text="leisure - " + str(self.leisureCat) + "%")

            if self.leisureCat <= 10:
                mb.showerror("sorry", "your cat is sad")
                self.leisureCat += 20

            if self.healthCat <= 10:
                mb.showerror("sorry", "your cat is ill")
                self.healthCat += 20

            self.l3.configure(text="your cat is alive")

    def health(self):
        self.healthCat += 10
        self.leisureCat -= 2
        self.l1.configure(text="health - " + str(self.healthCat) + "%")
        self.l2.configure(text="leisure - " + str(self.leisureCat) + "%")
        self.l3.configure(text="your cat is healthy")
        if self.leisureCat <= 10:
            mb.showerror("sorry", "your cat is sad")
            self.leisureCat += 20

    def leisure(self):
        self.healthCat -= 2
        self.leisureCat += 10
        self.l1.configure(text="health - " + str(self.healthCat) + "%")
        self.l2.configure(text="leisure - " + str(self.leisureCat) + "%")
        self.l3.configure(text="your cat is at leisure")
        if self.healthCat <= 10:
            mb.showerror("sorry", "your cat is ill")
            self.healthCat += 20

    def quit_game(self):
        self.root.destroy()

if __name__ == "__main__":
    cat_game = CatGame()
