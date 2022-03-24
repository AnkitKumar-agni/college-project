from tkinter import *
from PIL import Image, ImageTk
from Face import mainwindow


def mainPage():
    window = Tk()

    window.geometry("800x540")
    window.title("SEQCAM")
    window.maxsize(width=800, height=540)
    window.minsize(width=800, height=540)
    window.iconphoto(True, PhotoImage(file="C:\\Users\\dell\\PycharmProjects\\College project\\Security Camera"
                                           "\\icons\\cam1.png"))

    # Background Image
    labelimg = Image.open("C:\\Users\\dell\\PycharmProjects\\College project\\Security Camera\\icons\\backicon.png")
    labelimg = labelimg.resize((800, 540), Image.ANTIALIAS)
    labelimg = ImageTk.PhotoImage(labelimg)

    titlelabel = Label(window, image=labelimg)
    titlelabel.place(x=0, y=0, relheight=1, relwidth=1)

    recordimg = Image.open("C:\\Users\\dell\\PycharmProjects\\College project\\Security Camera\\icons\\recordicon.png")
    recordimg = recordimg.resize((50, 50), Image.ANTIALIAS)
    recordimg = ImageTk.PhotoImage(recordimg)

    faceimg = Image.open("C:\\Users\\dell\\PycharmProjects\\College project\\Security Camera\\icons\\faceimg.png")
    faceimg = faceimg.resize((55, 55), Image.ANTIALIAS)
    faceimg = ImageTk.PhotoImage(faceimg)

    exitimg = Image.open("C:\\Users\\dell\\PycharmProjects\\College project\\Security Camera\\icons\\exiticon.png")
    exitimg = exitimg.resize((45, 45), Image.ANTIALIAS)
    exitimg = ImageTk.PhotoImage(exitimg)

    def fun():
        window.destroy()
        mainwindow()

    # Record Button

    recordbutton = Button(window, text="START RECORDING", bg="black", fg="blue",
                          image=recordimg, compound="left",
                          font=("Helvitica", 20, "bold"), padx=20, pady=10)

    recordbutton.place(x=50, y=150)

    # Face Button

    facebutton = Button(window, text="FACE", bg="black", fg="blue",
                        font=("Helvitica", 25, "bold"), padx=55, pady=0, justify="left",
                        image=faceimg, compound="left", command=fun)

    facebutton.place(x=50, y=250)

    # Exit Button

    exitbutton = Button(window, text="Exit", bg="black", fg="Red",
                        font=("Helvitica", 25, "bold"), padx=55, pady=0, justify="left",
                        image=exitimg, compound="left", command=window.quit)

    exitbutton.place(x=50, y=350)

    window.mainloop()


mainPage()


