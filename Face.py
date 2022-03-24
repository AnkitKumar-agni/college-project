from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import os
from tkinter import messagebox
import shutil

global root
global window
global root1
global filename
global root2
global snoentry1
global root3


def popup(message_type, message):

    """
    This function generate popups
    Increase clarity of actions performed by the user.
    """

    message_type = str(message_type)
    message = str(message)

    if message_type == "warning":
        messagebox.showwarning("Warning", f'{message}')

    elif message_type == "info":
        messagebox.showinfo("InFo", f'{message}')

    elif message_type == "error":
        messagebox.showerror("Error", f'{message}')

    elif message_type == "ask":
        response = messagebox.askyesno("InFo", f'{message}')
        return response



def BackToFace(click):

    """
    This function is to take the user to the FACE page.
    """
    global root
    global root1
    global root3
    global root2

    if click == 1:
        root1.destroy()

    elif click == 2:
        root1.destroy()

    elif click == 5:
        root3.destroy()

    else:
        root2.destroy()


    root = Tk()
    root.maxsize(width=800, height=540)
    root.minsize(width=800, height=540)
    root.title("SEQCAM | FACE")

    mainimg = Image.open("C:\\Users\\dell\\PycharmProjects\\College project\\Security Camera\\icons\\FACEPAGE.png")
    mainimg = mainimg.resize((800, 540), Image.ANTIALIAS)
    mainimg = ImageTk.PhotoImage(mainimg)

    mainlabel = Label(image=mainimg)
    mainlabel.place(x=0, y=0)

    # Back Button

    Back = Button(root, text="<<BACK<<", fg="blue", bg="Black", font=("Arial Black", 10, "bold"),
                  padx=10, pady=10, command=BackToMainPage)
    Back.place(x=700, y=10)

    # Add Face Button

    addface = Button(root, text="ADD FACE", font=("Helvetica", 20, "bold"), fg="blue", bg="black",
                     padx=48, pady=10, command=AddFace)
    addface.place(x=40, y=160)

    # Remove Face Button

    removeface = Button(root, text="REMOVE FACE", font=("Helvetica", 20, "bold"), fg="blue", bg="black",
                        padx=20, pady=10, command=RemoveFace)
    removeface.place(x=40, y=260)

    # record Button

    record = Button(root, text="RECORD", font=("Helvetica", 20, "bold"), fg="blue", bg="black",
                    padx=60, pady=10, command=Records)
    record.place(x=40, y=360)

    root.mainloop()


def clicked(click):

    """
    This function for the confirmation for going back.
    If clicked YES then goes back to the FACE page
    If clicked NO then stays in the current page
    """

    if click == 1 :
        response = popup("ask", "Are You Sure")
        if response == 1:
            BackToFace(click)
    elif click == 3:
        response = popup("ask", "Are You Sure")
        if response == 1:
            BackToFace(click)
    elif click == 5:
        response = popup("ask", "Are You Sure")
        if response == 1:
            BackToFace(click)
    else:
        BackToFace(click)





def BackToMainPage():

    """
    This Function takes back to the main page.
    """

    global root
    global window
    root.destroy()
    window = Tk()

    def dest():
        global window
        window.destroy()

    window.geometry("800x540")
    window.title("SEQCAM")
    window.maxsize(width=800, height=540)
    window.minsize(width=800, height=540)
    # window.iconphoto(True, PhotoImage(file="C:\\Users\\dell\\PycharmProjects\\College project\\Security Camera"
    #                                        "\\icons\\cam1.png"))


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

    # Function To Destroy window
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
                        image=faceimg, compound="left", command=fun )

    facebutton.place(x=50, y=250)

    # Exit Button

    exitbutton = Button(window, text="Exit", bg="black", fg="Red",
                        font=("Helvitica", 25, "bold"), padx=55, pady=0, justify="left",
                        image=exitimg, compound="left", command=dest)

    exitbutton.place(x=50, y=350)

    window.mainloop()



def selectimg():
    """
    This function is used to open a dialog box and then select an image
    :returns path of the selected image.

    """


    global root1
    global filename

    try:

        filename = filedialog.askopenfilename(title="Select Images", filetypes=(("PNG", "*.png"), ("JPG", "*.jpg")))

    except EXCEPTION as e:

        popup("error", "Error")


def SubmitAdd(click):
    """
    This function is for submit button
    Function performs the submission of the entered details
    It saves the data including images to the directory/file/folder
    """


    global snoentry
    global namentry
    global filename
    cur = os.getcwd()
    flag = 0

    sno_record = snoentry.get()
    name_record = namentry.get()

    try:
        filename_record = str(filename)
        list_record = [sno_record, name_record]

        for i in list_record:
            if i == "0":
                popup("error", "Invalid Entry")
                flag = 1
                break
            if i == "":
                popup("error", "Invalid Entry")
                flag = 1
                break
            if i == " ":
                popup("error", "Invalid Entry")
                flag = 1
                break

        if flag == 0:
            try:
                os.mkdir(f'{cur}\\{"Records"}\\{sno_record}')
            except:
                pass

            file = open(f'{cur}\\{"Records"}\\{sno_record}\\Details{sno_record}', 'w')
            file.write(str(list_record))
            file.close()

            file1 = open(f'{cur}\\{"Records"}\\{sno_record}\\Image{sno_record}', 'w')
            file1.write(filename_record)
            file1.close()

            popup("info", "Submitted")


    except:
        popup("warning", "Select Image")

    finally:
        clicked(click)

def SubmitRemove(click1):

    global snoentry1
    delete_no = snoentry1.get()
    cur_dir = os.getcwd()

    submitresponse = popup("ask", "Are You Sure")

    if submitresponse == 1:

        try:
            shutil.rmtree(f'{cur_dir}\\{"Records"}\\{delete_no}', ignore_errors=False)
            clicked(click1)

        except:
            popup("error", "Couldn't delete file")



    else:
        pass


def see_name():

    global root2
    global seelabel
    global snoentry1
    global filename

    searhsno = snoentry1.get()
    cur_dir = os.getcwd()

    try:

        file_search = open(f'{cur_dir}\\{"Records"}\\{searhsno}\\Details{searhsno}', 'r')
        img_file = open(f'{cur_dir}\\{"Records"}\\{searhsno}\\Image{searhsno}', 'r')
        img_path = img_file.read()
        list_search = file_search.read()
        disp = "Name : " + (list_search[9:-2])
        seelabel = Label(root2, text=disp, font=("Helvetica", 15, "bold"), fg="grey", bg="black")
        seelabel.place(x=150, y=200)
        disp_img = Image.open(img_path)
        disp_img = disp_img.resize((200, 140), Image.ANTIALIAS)
        disp_img = ImageTk.PhotoImage(disp_img)
        disp_imglabel = Label(root2)
        disp_imglabel.configure(image=disp_img)
        disp_imglabel.image = disp_img
        disp_imglabel.place(x=150, y=250)
        file_search.close()
        img_file.close()


    except:

        popup("error", "Couldn't find the file")





def AddFace():

    """
    This function creates a graphical user interface for adding person's face.
    Page takes inputs like :
    1. Serial Number
    2. Person's Name
    3. Image
    """

    global root
    global root1
    global snoentry
    global namentry


    root.destroy()


    root1 = Tk()
    root1.title("ADD FACE")
    root1.maxsize(width=800, height=540)
    root1.minsize(width=800, height=540)
    backimg = Image.open("C:\\Users\\dell\\PycharmProjects\\College project\\Security Camera\\icons\\Addimage.png")
    backimg = backimg.resize((800, 540), Image.ANTIALIAS)
    backimg = ImageTk.PhotoImage(backimg)

    backlabel = Label(root1, image=backimg)
    backlabel.place(x=0, y=0, relheight=1, relwidth=1, anchor="nw")

    back_button = Button(root1, text="<<BACK<<", font=("Helvetica", 10, "bold"), fg="blue", bg="black",
                         padx=20, pady=8, command=lambda: clicked(1))
    back_button.place(x=700, y=10)


    snolabel = Label(root1, text="S.NO :", font=("Arial black", 15, "bold"), fg="blue", bg="black")
    snolabel.place(x=40, y=150)

    snoentry = Entry(root1, width=25, font=("Helvetica", 15), bg="black", fg="White")
    snoentry.place(x=150, y=150)

    name = Label(root1, text="Name :", font=("Arial black", 15, "bold"), fg="blue", bg="black")
    name.place(x=40, y=220)

    namentry = Entry(root1, width=25, font=("Helvetica", 15), bg="black", fg="White")
    namentry.place(x=150, y=220)

    selimg = Button(root1, text="Select Image", font=("Helvetica", 20, "bold"), bg="black", fg="blue", pady=5, padx=20,
                    command=selectimg)
    selimg.place(x=180, y=300)

    submitbtn = Button(root1, text="SUBMIT", font=("Helvetica", 15, "bold"), bg="black", fg="white", padx=20, pady=10,
                       command=lambda: SubmitAdd(2))
    submitbtn.place(x=220, y=400)

    root.mainloop()






def RemoveFace():

    global root
    global root2
    global snoentry1

    root.destroy()

    root2 = Tk()
    root2.title("REMOVE FACE")
    root2.maxsize(width=800, height=540)
    root2.minsize(width=800, height=540)
    backimg = Image.open("C:\\Users\\dell\\PycharmProjects\\College project\\Security Camera\\icons\\Addimage.png")
    backimg = backimg.resize((800, 540), Image.ANTIALIAS)
    backimg = ImageTk.PhotoImage(backimg)

    backlabel = Label(root2, image=backimg)
    backlabel.place(x=0, y=0, relheight=1, relwidth=1, anchor="nw")

    back_button = Button(root2, text="<<BACK<<", font=("Helvetica", 10, "bold"), fg="blue", bg="black",
                         padx=20, pady=8, command=lambda: clicked(3))
    back_button.place(x=700, y=10)

    snolabel = Label(root2, text="S.NO :", font=("Arial black", 15, "bold"), fg="blue", bg="black")
    snolabel.place(x=40, y=150)

    snoentry1 = Entry(root2, width=25, font=("Helvetica", 15), bg="black", fg="White")
    snoentry1.place(x=150, y=150)

    see = Button(root2, text="See", font=("Arial black", 8, "bold"), fg="blue", bg="black", padx=10, pady=0,
                 command=see_name)
    see.place(x=150, y=180)


    submitbtn1 = Button(root2, text="SUBMIT", font=("Helvetica", 15, "bold"), bg="black", fg="white", padx=20, pady=10,
                        command=lambda: SubmitRemove(4))
    submitbtn1.place(x=220, y=400)

    root2.mainloop()




def Records():

    try:

        global root3
        global root
        root.destroy()
        root3 = Tk()
        root3.title("RECORDS")
        root3.maxsize(width=800, height=540)
        root3.minsize(width=800, height=540)
        cur_dir = os.getcwd()
        list_dir = os.listdir(f'{cur_dir}\\Records')
        scrollbar = Scrollbar(root3)
        scrollbar.pack(side=RIGHT, fill=Y)
        listbox = Listbox(root3, yscrollcommand=scrollbar.set, bg="black", fg="white")
        for i in list_dir:
            listbox.insert(END, str(i))

        listbox.pack(fill="both", padx=5)
        scrollbar.config(command=listbox.yview)
        back_button = Button(root3, text="<<BACK<<", font=("Helvetica", 10, "bold"), fg="blue", bg="black",
                             padx=20, pady=8, command=lambda: clicked(5))
        back_button.place(x=650, y=480)


        def view():
            pointer = listbox.get(ANCHOR)
            try:
                view_file = open(f'{cur_dir}\\Records\\{pointer}\\Details{pointer}', 'r')
                view_img = open(f'{cur_dir}\\Records\\{pointer}\\Image{pointer}', 'r')
                imgpath = view_img.read()
                data = view_file.read()
                print(data)
                datasno = "S.NO : " + data[2:5] + "    |    NAME : " + data[9:-2]
                img = Image.open(imgpath)
                img = img.resize((150, 150), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)
                # disp_imglabel = Label(root3)
                disp_imglabel.configure(image=img)
                disp_imglabel.image = img
                # disp_imglabel.pack(padx=5)
                my_label.config(text=datasno)
                view_img.close()
                view_file.close()
            except:
                popup("error", "Select an Option")

        view_button = Button(root3, text="View", font=("Helvetica", 20, "bold"), fg="blue", bg="Black", command=view)
        view_button.pack(pady=10)
        global my_label
        global disp_imglabel
        disp_imglabel=Label(root3, image='')
        disp_imglabel.pack(pady=5)
        my_label = Label(root3, text='')
        my_label.pack(pady=5)
        root3.mainloop()

    except:
        popup("error", "ERROR")






def mainwindow():

    """
    This Function creates window toplevel to main window
    size : 800 x 540 (fixed)
    Buttons Available :
    ADD FACE :  This option is to input person's details for facial recognition
    REMOVE FACE : This option takes to the page where user can delete the person's details
    RECORDS: This option is to see available persons details.
    """


    global root
    root = Tk()
    root.maxsize(width=800, height=540)
    root.minsize(width=800, height=540)
    root.title("SEQCAM | FACE")

    mainimg = Image.open("C:\\Users\\dell\\PycharmProjects\\College project\\Security Camera\\icons\\FACEPAGE.png")
    mainimg = mainimg.resize((800, 540), Image.ANTIALIAS)
    mainimg = ImageTk.PhotoImage(mainimg)


    mainlabel = Label(image=mainimg)
    mainlabel.place(x=0, y=0)

    # Back Button

    Back = Button(root, text="<<BACK<<", fg="blue", bg="Black", font=("Arial Black", 10, "bold"),
                  padx=10, pady=10, command=BackToMainPage)
    Back.place(x=700, y=10)

    # Add Face Button

    addface = Button(root, text="ADD FACE", font=("Helvetica", 20, "bold"), fg="blue", bg="black",
                     padx=48, pady=10, command=AddFace)
    addface.place(x=40, y=160)

    # Remove Face Button

    removeface = Button(root, text="REMOVE FACE", font=("Helvetica", 20, "bold"), fg="blue", bg="black",
                        padx=20, pady=10, command=RemoveFace)
    removeface.place(x=40, y=260)

    # record Button

    record = Button(root, text="RECORD", font=("Helvetica", 20, "bold"), fg="blue", bg="black",
                    padx=60, pady=10, command=Records)
    record.place(x=40, y=360)

    root.mainloop()



