from tkinter import *
from PIL import Image,ImageTk

root = Tk()  
root.title("Virtul freind")
root.geometry("550x675")
root.resizable(False, False)
root.config(bg="pink")

# frame
frame = LabelFrame(root, borderwidth=3, relief="raised", bg="#90D5FF")
frame.config(bg="#90D5FF")
frame.grid(row=0, column=1, padx=55, pady=10)

# text label
text_label = Label(frame, text="AI Assistanant", font=("comic sans ms", 14, "bold"), bg="#FFFFC5", fg="black", bd=0)
text_label.grid(row=0, column=0, padx=50, pady=30)

# image
# image (resized)
img = Image.open("image/image.jpg")
img = img.resize((250, 250))  # Resize to width x height
image = ImageTk.PhotoImage(img)
image_label = Label(frame, image=image)
image_label.grid(row=1, column=0, pady=20)


root.mainloop()
