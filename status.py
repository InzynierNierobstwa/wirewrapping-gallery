from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.title('Image')
window.iconbitmap('favicon.ico')

myImg1 = ImageTk.PhotoImage(Image.open('images/wire1.jpg'))
myImg2 = ImageTk.PhotoImage(Image.open('images/wire2.jpg'))
myImg3 = ImageTk.PhotoImage(Image.open('images/wire3.jpg'))
myImg4 = ImageTk.PhotoImage(Image.open('images/wire4.jpg'))
myImg5 = ImageTk.PhotoImage(Image.open('images/wire5.jpg'))
myImg6 = ImageTk.PhotoImage(Image.open('images/wire6.jpg'))


imageList = [myImg1, myImg2, myImg3, myImg4, myImg5, myImg6]

status = Label(window, text='Image 1 of ' + str(len(imageList)), bd=1, relief=SUNKEN, anchor=E)

myLabel = Label(image=myImg1)
myLabel.grid(row=0, column=0, columnspan=3)

def forward(imageNumber):
    global myLabel
    global buttonForward
    global buttonBack

    myLabel.grid_forget()
    myLabel = Label(image=imageList[imageNumber - 1])
    buttonForward = Button(window, text='>>', command=lambda: forward(imageNumber + 1))
    buttonBack = Button(window, text='<<', command= lambda: back(imageNumber - 1))

    if imageNumber == len(imageList):
        buttonForward = Button(window, text='>>', state=DISABLED)

    myLabel.grid(row=0, column=0, columnspan=3)
    buttonBack.grid(row=1, column=0)
    buttonForward.grid(row=1, column=2)

    status = Label(window, text='Image ' + str(imageNumber) + ' of ' + str(len(imageList)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


def back(imageNumber):
    global myLabel
    global buttonForward
    global buttonBack

    myLabel.grid_forget()
    myLabel = Label(image=imageList[imageNumber - 1])
    buttonForward = Button(window, text='>>', command=lambda: forward(imageNumber + 1))
    buttonBack = Button(window, text='<<', command= lambda: back(imageNumber - 1))

    if imageNumber == 1:
        buttonBack = Button(window, text='<<', state=DISABLED)

    myLabel.grid(row=0, column=0, columnspan=3)
    buttonBack.grid(row=1, column=0)
    buttonForward.grid(row=1, column=2)

    status = Label(window, text='Image ' + str(imageNumber) + ' of ' + str(len(imageList)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

buttonBack = Button(window, text='<<', command=back, state=DISABLED)
buttonQuit = Button(window, text='Exit', command=window.quit)
buttonForward = Button(window, text=">>", command=lambda: forward(2))

buttonBack.grid(row=1, column=0)
buttonQuit.grid(row=1, column=1)
buttonForward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

window.mainloop()