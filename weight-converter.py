from tkinter import *
from tkinter import messagebox
import math
def calculate():
    if weight_options.get() == 'Lbs':
        messagebox.showinfo('Your Weight:', f'Your weight in Kgs is {int(weight_e.get()) * 0.45}')
    elif weight_options.get() == 'Kgs':
        messagebox.showinfo('Your Weight:', f'Your weight in Lbs is {(int(weight_e.get())) / 0.45}')
# Initialize Tkinter
root = Tk()
root.title('Weight Converter')
root.geometry('250x60')
# Create Elements
weight_label = Label(root, text='Weight: ')
weight_e = Entry(root)
weight_options = StringVar()
weight_options.set('Lbs')
weight_choice = OptionMenu(root, weight_options, 'Lbs' ,'Kgs')
submit = Button(root, text='Submit', command=calculate)
# Place Elements on screen
weight_label.grid(row=2, column=1)
weight_e.grid(row=2, column=2, columnspan=3)
weight_choice.grid(row=2, column=5, columnspan=3)
submit.grid(row=3, column=2, columnspan=3)
root.mainloop()