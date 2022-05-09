from jarvis import speak
from tkinter import *

speak('starting')


# key down function
def click():
    global entered_text
    entered_text = textentry.get()  # this will collect the text entered


window = Tk()
# window title
window.title('wow, this is so cool')
# photo
photo1 = PhotoImage(file="plswork.gif")
Label(window, image=photo1, bg='black').grid(row=0, column=0, sticky=E)
# text
Label(window, text='hello', bg='black', fg='white', font='none 14 bold').grid(row=1, column=0, sticky=W)

# text box
textentry = Entry(window, width=20, bg='white')
textentry.grid(row=2, column=0, sticky=W)
# button submit
Button(window, text='submit', width=6, command=click).grid(row=3, column=0, sticky=W)
# another label
Label(window, text='Definition:', bg='black', fg='white', font='none 12 bold').grid(row=4, column=0, sticky=W)
# text box
output = Text(window, width=75, height=6, wrap=WORD, bg='white')
textentry.grid(row=5, column=0, sticky=W)
window.mainloop()
speak(entered_text)
speak('finished')
