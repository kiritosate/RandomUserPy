from tkinter.font import BOLD, ITALIC
from client import Client
from tkinter import *
from PIL import Image, ImageTk
import urllib
import io

class Main:

    def __init__(self) -> None:
        
        self.root = Tk()
        self.root.geometry("350x300")
        self.root.title("Random User Gui")
        self.root.resizable = False
        self.btn_next = Button(text="Generate New", command=lambda:self.generate())
        self.btn_next.pack(side=BOTTOM, pady=10)

        self.root.mainloop()

    def generate(self):
        try:
            self.Image.destroy()
            self.Name.destroy()
            self.Email.destroy()
            self.User.destroy()
        except: 
            pass
        client = Client()
        _Data = client.getData()
        img = self.showImage(_Data['image_large'])

        self.Image = Label(self.root, image=img)
        self.Image.image = img
        self.Image.pack(pady=8, padx=5)

        self.Name = Label(self.root, text=f"NAME: {_Data['name']}", font=("arial", 12, BOLD))
        self.Name.pack(padx=5, pady=5)

        self.Email = Label(self.root, text=_Data['email'], font=("cursive", 11, ITALIC))
        self.Email.pack(padx=1, pady=1)

        #self.User = Label(self.root, text=_Data['username'])
        #self.User.pack(padx=1, pady=1)

    def showImage(self, image_link):
        self.raw_image = None
        self.toBytesImage = None

        self.raw_image = urllib.request.urlopen(image_link).read()
        self.toBytesImage = Image.open(io.BytesIO(self.raw_image))

        return ImageTk.PhotoImage(self.toBytesImage)

main = Main()



