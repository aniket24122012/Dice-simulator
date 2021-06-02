from tkinter import*
import random

root = Tk()

root.title("Dice simulator")

root.geometry("600x500")
root.configure(bg='#05f570')

label = Label(root, font=("Helvitica",300,'bold'),text="",fg="green",bg="lightgreen")
def rolldice() :
    dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    label.configure(text=f'{random.choice(dice)}')
label.pack()


button = Button(root,font=("Helvitica",25,'bold'),text="Dice Roll",bg='#a3ed0e',fg='#ab7683',pady = 10,command=rolldice)
button.pack()
root.mainloop()