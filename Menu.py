import tkinter
from tkinter import *


class LoginFrame(tkinter.Frame):

    def __init__(self, master=None):
        # memanggil kontruktor kelas induk (tkinter.Frame)
        tkinter.Frame.__init__(self, master)
        self.grid()
        self.utama()
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def utama(self) :

        self['background'] = "#252525"
        self.pack(fill=BOTH, expand=1)
        # membuat entry menu
        menu = Menu(self.master)
        self.master.config(menu=menu)
        filemenu = Menu(menu,
            activebackground='#0278ae',
            activeborderwidth=20,
            activeforeground='#ffffff',
            bg='#252525',
            bd=20,
            cursor='cross',
            font='Helvetica',
            fg='#ffffff',
            relief='ridge',
            selectcolor='green',
            tearoff=1,
            title='menu')
        filemenu.add_command(label="Open")
        filemenu.add_command(label="New")
        filemenu.add_command(label="Save")
        filemenu.add_command(label="Save as...")
        filemenu.add_command(label="Close")
        menu.add_cascade(label="File", menu=filemenu)

        editmenu = Menu(menu,
            activebackground='#0278ae',
            activeborderwidth=20,
            activeforeground='#ffffff',
            bg='#252525',
            bd=20,
            cursor='cross',
            font='Helvetica',
            fg='#ffffff',
            relief='ridge',
            selectcolor='green',
            tearoff=1,
            title='menu')
        editmenu.add_command(label="Undo")
        editmenu.add_command(label="Redo")
        editmenu.add_command(label="Cut")
        editmenu.add_command(label="Copy")
        editmenu.add_command(label="Paste")
        menu.add_cascade(label="Edit", menu=editmenu)


        menubutton = Menubutton(self, text = "Language", relief = FLAT)  
        # deklarasi foto
        self.photos = PhotoImage(file = "pick.png") 
        # mengatur ukuran button
        self.photoimages = self.photos.subsample(100, 100) 
        menubutton['image'] = self.photoimages
        menubutton.grid()  
        menubutton.menu = Menu(menubutton)  
        menubutton["menu"]=menubutton.menu  
        menubutton.menu.add_checkbutton(label = "Pick Tool", variable=IntVar())  
        menubutton.menu.add_checkbutton(label = "Move Tool", variable = IntVar())  

        # self.config(menu = menu)


def main():
# membuat kelas demo frame
    app = LoginFrame()
    app.master.title("Login Frame")
    app.master.grid_rowconfigure(0, weight=1)
    app.master['background'] = "#252525"
    app.master.grid_columnconfigure(0, weight=1)
    app.mainloop()
# memanggil fungsi
if __name__ == "__main__":
    main()