from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
from stegano import lsb

# ------------------- Main Window -------------------
win = Tk()
win.geometry('700x480')
win.config(bg='black')
win.title("Image Steganography")


# ------------------- Functions -------------------

# Open an image and show preview
def open_img():
    global open_file
    open_file = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title='Select Image',
        filetypes=(('PNG file', '*.png'), ('JPG file', '*.jpg'))
    )
    if open_file:
        try:
            img = Image.open(open_file)
            img = img.resize((240, 210))  # resize to fit frame
            img = ImageTk.PhotoImage(img)
            lf1.configure(image=img)
            lf1.image = img
        except Exception as e:
            messagebox.showerror('Error', f'Cannot open image: {e}')


# Hide message in image
def hide():
    if 'open_file' not in globals():
        messagebox.showerror('Error', 'Please open an image first.')
        return

    password = code.get()
    if password == '12340':
        msg = text1.get(1.0, END).strip()
        if msg == "":
            messagebox.showerror('Error', 'Please enter a message to hide.')
            return
        try:
            global hide_msg
            hide_msg = lsb.hide(open_file, msg)
            messagebox.showinfo('Success', 'Message hidden successfully! Please save your image.')
        except Exception as e:
            messagebox.showerror('Error', f'Failed to hide message: {e}')
    elif password == '':
        messagebox.showerror('Error', 'Please enter Secret Key.')
    else:
        messagebox.showerror('Error', 'Wrong Secret Key.')
        code.set('')


# Save the stego image
def save_img():
    if 'hide_msg' not in globals():
        messagebox.showerror('Error', 'No hidden message to save.')
        return
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png")]
    )
    if file_path:
        try:
            hide_msg.save(file_path)
            messagebox.showinfo('Saved', f'Image has been saved as:\n{file_path}')
        except Exception as e:
            messagebox.showerror('Error', f'Cannot save image: {e}')


# Reveal hidden message
def show():
    if 'open_file' not in globals():
        messagebox.showerror('Error', 'Please open an image first.')
        return

    password = code.get()
while
    if password == '12340':
        try:
            show_msg = lsb.reveal(open_file)
            if show_msg is None:
                messagebox.showinfo('Result', 'No hidden message found in this image.')
            else:
                text1.delete(1.0, END)
                text1.insert(END, show_msg)
        except Exception as e:
            messagebox.showerror('Error', f'Failed to reveal message: {e}')
    elif password == '':
        messagebox.showerror('Error', 'Please enter Secret Key.')
    else:
        messagebox.showerror('Error', 'Wrong Secret Key.')
        code.set('')


# ------------------- UI Layout -------------------

# Logo
try:
    logo = PhotoImage(file='lgo.png')  # make sure lgo.png is in the same folder
    Label(win, image=logo, bd=0, bg='black').place(x=300, y=0)
except Exception:
    # if logo not found, skip
    Label(win, text="Logo Missing", font='impact 15', bg='black', fg='red').place(x=190, y=0)

# Heading
Label(win, text='🌌 StegoSphere', font='impact 30 bold', bg='black', fg='red').place(x=240, y=60)

# Frame for Image
f1 = Frame(win, width=250, height=220, bd=5, bg='purple')
f1.place(x=50, y=120)
lf1 = Label(f1, bg='purple')
lf1.place(x=0, y=0)

# Frame for Message
f2 = Frame(win, width=320, height=220, bd=5, bg='white')
f2.place(x=330, y=120)
text1 = Text(f2, font='ariel 15 bold', wrap=WORD)
text1.place(x=0, y=0, width=310, height=210)

# Label for Secret Key
Label(win, text='Enter Secret Key', font='10', bg='black', fg='yellow').place(x=250, y=360)

# Entry widget for secret key
code = StringVar()
e = Entry(win, textvariable=code, bd=2, font='impact 10 bold', show='*')
e.place(x=245, y=390)

# Buttons
open_button = Button(win, text='Open Image', bg='blue', fg='white', font='ariel 12 bold',
                     cursor='hand2', command=open_img)
open_button.place(x=60, y=430)

save_button = Button(win, text='Save Image', bg='green', fg='white', font='ariel 12 bold',
                     cursor='hand2', command=save_img)
save_button.place(x=190, y=430)

hide_button = Button(win, text='Hide Data', bg='red', fg='white', font='ariel 12 bold',
                     cursor='hand2', command=hide)
hide_button.place(x=350, y=430)

show_button = Button(win, text='Show Data', bg='orange', fg='white', font='ariel 12 bold',
                     cursor='hand2', command=show)
show_button.place(x=480, y=430)

# ------------------- Run -------------------
win.mainloop()
