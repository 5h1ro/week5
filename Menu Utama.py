import tkinter
from tkinter import *


class LoginFrame(tkinter.Frame):

    def __init__(self, master=None):
        # memanggil kontruktor kelas induk (tkinter.Frame)
        tkinter.Frame.__init__(self, master)
        self.grid()
        self.utama()
        # self.grid_rowconfigure(1, weight=1)
        # self.grid_columnconfigure(1, weight=1)

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
        self.photos = PhotoImage(file = "pick.png") 
        self.photoimages = self.photos.subsample(60, 60) 
        menubutton['image'] = self.photoimages
        menubutton.grid(row=0, column=0, sticky=W)  
        menubutton.menu = Menu(menubutton)  
        menubutton["menu"]=menubutton.menu  
        menubutton.menu.add_checkbutton(label = "Pick Tool", variable=IntVar())  
        menubutton.menu.add_checkbutton(label = "Move Tool", variable = IntVar())

        

        Pemahaman = tkinter.Label(self, text="Tingkat Pemahaman :")
        Pemahaman['bg'] = '#252525'
        Pemahaman['fg'] = '#ffffff'
        Pemahaman['font'] = 'Helvetica 12 bold'
        Pemahaman.grid(row=0, column=1, sticky=W)

        scale = Scale(self, 
            variable=IntVar,
            orient='horizontal',
            activebackground='blue',
            bg='#252525',
            cursor='plus',
            font='Calibri',
            fg='#fff',
            from_=1,
            to=10,
            highlightbackground='red',
            # label='range nilai',
            length=200,
            relief='raised',
            sliderlength=10)
        scale.grid(row=0, column=2, sticky=W)

        Umur = tkinter.Label(self, text="Umur :")
        Umur['bg'] = '#252525'
        Umur['fg'] = '#ffffff'
        Umur['font'] = 'Helvetica 12 bold'
        Umur.grid(row=1, column=1, sticky=W)

        spinbox = Spinbox(self,
            from_=0,
            to=100,
            activebackground='blue',
            bg='#252525',
            cursor='plus',
            font='Calibri',
            fg='#ffffff')
        spinbox.grid(row=1, column=2, sticky=W)


        Alamat = tkinter.Label(self, text="Alamat :")
        Alamat['bg'] = '#252525'
        Alamat['fg'] = '#ffffff'
        Alamat['font'] = 'Helvetica 12 bold'
        Alamat.grid(row=2, column=1, sticky=W)

        text = Text(self,
            bg='#fff',
            bd=5,
            cursor='plus',
            font='Calibri',
            fg='#252525',
            height=5,
            width=20)
        text.grid(row=2, column=2, sticky=W)


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