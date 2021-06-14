import tkinter
from PIL import Image, ImageTk
import random

root = tkinter.Tk()
root.geometry("600x600")
root.title("Simple Rolling Dice Game")

BlankLine = tkinter.Label(root, text="")
BlankLine.pack()

HeadingLabel = tkinter.Label(root, text="This is a simulation", fg="light green", bg="dark green", font="Helvetica 18 bold italic")
HeadingLabel.pack()

dice = ['1.png','two.png','3.png','4.jpg','five.png','six.png']

DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))

ImageLabel = tkinter.Label(root, image = DiceImage)
ImageLabel.pack(expand=True)

DiceImage1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

ImageLabel1 = tkinter.Label(root, image = DiceImage1)
ImageLabel1.pack(expand=True)

def rolling():
    DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))

    ImageLabel.configure(image=DiceImage)
    ImageLabel.image = DiceImage
    DiceImage1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

    ImageLabel1.configure(image=DiceImage1)
    ImageLabel1.image = DiceImage1

button = tkinter.Button(root, text="Roll the Dice!", fg="blue", command=rolling)

button.pack(expand=True)
root.mainloop()