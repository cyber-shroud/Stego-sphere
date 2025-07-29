
## ✅ Requirements
# Python 3.x
#Pillow
##Stegano

## 👤 Author
##Jagarnath Mali ([@cyber-shroud](https://github.com/cyber-shroud))

from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
from stegano import lsb

# --- WINDOW SETUP ---
win = Tk()
win.title("Stego Sphere")
win.geometry('750x500')
win.config(bg='#1e1e2f')
win.resizable(False, False)

# --- FUNCTION DEFINITIONS ---
def open_img():
    global open_file
    open_file = filedialog.askopenfilename(initialdir=os.getcwd(),
                                           title='Select Image File',
                                           filetypes=[('Image files', '*.png *.jpg *.jpeg')])
    if open_file:
        img = Image.open(open_file)
        img = img.resize((230, 210))  # Resize image to fit frame
        img = ImageTk.PhotoImage(img)
        lf1.configure(image=img)
        lf1.image = img


def hide():
    global hide_msg
    password = code.get()
    if password == '1234':
        msg = text1.get(1.0, END).strip()
        if not msg:
            messagebox.showerror('Error', 'Message field is empty')
            return
        hide_msg = lsb.hide(open_file, msg)
        messagebox.showinfo('Success', 'Message hidden successfully!\nClick "Save Image" to store the result.')
    elif not password:
        messagebox.showerror('Error', 'Please enter Secret Key')
    else:
        messagebox.showerror('Error', 'Wrong Secret Key')
        code.set('')


def save_img():
    try:
        hide_msg.save('Secret_Image.png')
        messagebox.showinfo('Saved', 'Image has been saved as "Secret_Image.png"')
    except Exception as e:
        messagebox.showerror('Error', f'Nothing to save!\n{e}')


def show():
    password = code.get()
    if password == '1234':
        try:
            show_msg = lsb.reveal(open_file)
            text1.delete(1.0, END)
            text1.insert(END, show_msg)
        except:
            messagebox.showerror('Error', 'Failed to reveal message.\nMake sure the image has hidden data.')
    elif not password:
        messagebox.showerror('Error', 'Please enter Secret Key')
    else:
        messagebox.showerror('Error', 'Wrong Secret Key')
        code.set('')


# --- GUI ELEMENTS ---

# Logo (optional)
try:
    logo_img = Image.open('lgo.png')
    logo_img = logo_img.resize((80, 80))
    logo = ImageTk.PhotoImage(logo_img)
    Label(win, image=logo, bg='#1e1e2f').place(x=10, y=10)
except:
    pass

# Title
Label(win, text='        Stego Sphere ',
      font=('Helvetica', 24, 'bold'),
      bg='#1e1e2f', fg='cyan').place(x=110, y=25)

# Frame 1 - Image Preview
f1 = Frame(win, width=240, height=220, bg='#2e2e3f', bd=3, relief=GROOVE)
f1.place(x=30, y=120)
lf1 = Label(f1, bg='#2e2e3f')
lf1.place(x=0, y=0)

# Frame 2 - Text Area
f2 = Frame(win, width=350, height=220, bg='white', bd=3, relief=GROOVE)
f2.place(x=300, y=120)
text1 = Text(f2, font=('Segoe UI', 12), wrap=WORD, bg='white', fg='black')
text1.place(x=0, y=0, width=344, height=214)

# Secret Key Label
Label(win, text='Enter Secret Key:',
      font=('Helvetica', 11, 'bold'),
      bg='#1e1e2f', fg='lightyellow').place(x=300, y=360)

# Entry for Secret Key
code = StringVar()
e = Entry(win, textvariable=code,
          bd=2, font=('Consolas', 12), show='*')
e.place(x=430, y=360, width=150)

# Buttons
button_style = {
    'font': ('Helvetica', 11, 'bold'),
    'bd': 0,
    'cursor': 'hand2',
    'width': 12,
    'height': 1,
    'padx': 5,
    'pady': 3
}

Button(win, text='Open Image', bg='#3366cc', fg='white', command=open_img, **button_style).place(x=50, y=430)
Button(win, text='Save Image', bg='#28a745', fg='white', command=save_img, **button_style).place(x=190, y=430)
Button(win, text='Hide Data', bg='#e63946', fg='white', command=hide, **button_style).place(x=330, y=430)
Button(win, text='Show Data', bg='#ffb703', fg='black', command=show, **button_style).place(x=470, y=430)

win.mainloop()
