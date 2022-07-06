from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as fd
import tkinter as tk
import cv2
from PIL import Image,ImageTk
from threading import Thread,Event

class Homepage(tk.Frame):
    def __init__(self,parent,Fcontroller):
        tk.Frame.__init__(self,parent)
        button_lauch = tk.Button(self,text = "Lauch", command=lambda: Fcontroller.showPage(Mainpage)).place(x=30, y=550)
        
class Mainpage(tk.Frame):
    def __init__(self,parent,Fcontroller):
        tk.Frame.__init__(self,parent)
        self.configure(bg='#EEEEEE')
        button_exit = tk.Button(self,text = "Exit", command=lambda: self.exit_soft(),padx=15).place(x=750, y=600)
        button_aCam = tk.Button(self,text = "Active", command=lambda: self.handBut(),padx=15).place(x=550, y=600)
        self.lbl_photo = tk.Label(self,borderwidth=2,relief="solid")
        self.lbl_photo.pack()

    def handBut(self):
        self.activeCam()
        # thread = Thread(target=self.updateCam)
        # thread.start()
        self.updateCam()

    def activeCam(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3,720)
        self.cap.set(4,560)

    def updateCam(self):
        succ, frame = self.cap.read()
        if succ == True:
            photo = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            photo = ImageTk.PhotoImage(image=Image.fromarray(photo))
            self.lbl_photo.configure(image=photo)
            self.after(15,self.updateCam())
        
    def exit_soft(self):
        self.quit()
        #cv2.destroyAllWindows()

class Soft(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # self.iconbitmap('line.ico')
        self.title("Hello")
        self.geometry("1000x700")
        self.resizable(width= False,height= False)
        
        container = tk.Frame(self)
        container.pack(side="top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frame = {}
        for F in (Homepage,Mainpage):#,Mainpage,Settingpage
            frame = F(container,self)
            frame.grid(row=0,column=0,sticky="nsew")
            self.frame[F]=frame
        self.frame[Homepage].tkraise()
        
    def showPage(self, container):
        frame = self.frame[container].tkraise()
        
run = Soft()
run.mainloop()
