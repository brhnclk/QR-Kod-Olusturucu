from tkinter import*
import qrcode

class Interface:
    def __init__(self):
        mainWindow = Tk()
        mainWindow.title("QR Code Generator")
        mainWindowGenislik = mainWindow.winfo_screenwidth()
        mainWindowYukseklik = mainWindow.winfo_screenmmheight()
        mainWindow.geometry(f"430x470+{(mainWindowGenislik//2)-215}+{(mainWindowYukseklik//2)}")
        mainWindow.iconphoto(False, PhotoImage(file="title.ico"))
        qrFrame = Frame()
        nameFrame = Frame()
        urlFrame = Frame()
        buttonFrame = Frame()
        self.qrImage = PhotoImage(file="qrcode.png")
        self.qr = Label(qrFrame,image=self.qrImage).pack()
        nameLabel = Label(nameFrame,text="Name").pack(side='left')
        self.nameVariable = StringVar()
        nameInput = Entry(nameFrame,textvariable=self.nameVariable).pack(side='left')
        urlLabel = Label(urlFrame,text="URL").pack(side='left')
        self.urlVariable = StringVar()
        urlInput = Entry(urlFrame,textvariable=self.urlVariable).pack(side='left')
        createButton = Button(buttonFrame,text="Create",command=self.create).pack()
        qrFrame.pack()
        nameFrame.pack()
        urlFrame.pack()
        buttonFrame.pack()
        mainWindow.mainloop()
    def create(self):
        code = qrcode.make(self.urlVariable.get())
        fileName = str(self.nameVariable.get() + ".png")
        code.save(fileName)
        self.qrImage.configure(file=fileName)

if __name__ == '__main__':
    Interface()