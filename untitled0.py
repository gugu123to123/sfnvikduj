from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time

root=Tk()
root.geometry("600x450")
clock_image= ImageTk.PhotoImage(Image.open ("clock(1).jpg"))

root.mainloop()