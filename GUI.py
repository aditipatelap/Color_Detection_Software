import sys
from tkinter import *
from tkinter import filedialog
from Detection import imageDetection
from tkinter.ttk import Progressbar
from tkinter import font

root1 = Tk()
# turn of maximization
root1.resizable(0, 0)
root1.title('Color Detection Software')

height = 430
width = 530
x = (root1.winfo_screenwidth() // 2 - (width // 2))
y = (root1.winfo_screenheight() // 2 - (height // 2))
root1.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# remove title bar
root1.overrideredirect(0)
root1.config(background='#561782')

welcome_label = Label(root1, text='COLOR DETECTION SOFTWARE', font=("yu gothic ui", 19, 'bold'), fg='white',
                      bg='#561782')
welcome_label.place(x=90, y=10)

img = PhotoImage(file='Resources/icon.png')
bg_label = Label(root1, image=img, bg='#561782')
bg_label.place(x=165, y=80)

prog_label = Label(root1, text='Please Wait...', font=("yu gothic ui", 15, 'bold'), bg='#561782')
prog_label.place(x=180, y=320)

progress = Progressbar(root1, orient=HORIZONTAL, length=470, mode='determinate')
progress.place(x=30, y=370)


def exit_window():
    sys.exit(root1.destroy())


i = 0


def load():
    global i
    if i <= 10:
        txt = 'Please Wait...' + (str(10 * i) + '%')
        prog_label.config(text=txt)
        prog_label.after(500, load)
        progress['value'] = 10 * i
        i += 1
    else:
        root1.destroy()


load()

root1.mainloop()

root2 = Tk()
root2.title('Image Selection')
root2.configure(background="#561782")

height = 430
width = 530
x = (root2.winfo_screenwidth() // 2 - (width // 2))
y = (root2.winfo_screenheight() // 2 - (height // 2))
root2.geometry('{}x{}+{}+{}'.format(width, height, x, y))


def openFile():
    filepath = filedialog.askopenfilename(initialdir="D:/",
                                          title='Please, Select the Image',
                                          filetypes=(("image file", "*.jpg"), ("all files", ".")))

    root2.destroy()
    imageDetection(filepath)


welcome_label = Label(root2, text='COLOR DETECTION SOFTWARE', font=("yu gothic ui", 20, 'bold'), fg='black',
                      bg='#fcf403')
welcome_label.place(x=70, y=20)

request = Label(root2, text='SELECT IMAGE', font=("yu gothic ui", 19, 'bold'), fg='white', bg='#561782')
request.place(x=180, y=150)

# arrow1 = PhotoImage(file='assets/My project.png')
# arrow1_label = Label(root2, image=arrow1, bg='#561782')
# arrow1_label.place(x=15, y=250)

buttonFont = font.Font(family='yu gothic ui', size=20, weight='bold')
btn = Button(root2, text="Select", width=10, font=buttonFont, command=lambda: openFile())
btn.place(x=180, y=200)

root2.mainloop()
