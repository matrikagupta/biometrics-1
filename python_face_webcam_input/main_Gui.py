from Tkinter import *
import Tkinter as tk
class App:
  def __init__(self, master):
    frame = Frame(master, height = 200, width = 200)
    frame.pack()
    
    self.slogan = Button(frame,
                         text="Capture Image",
                         command=self.call_captureImage, height = 1, width = 16)
    self.slogan.pack(side=TOP)
    self.slogan = Button(frame,
                         text="Capture Training Image",
                         command=self.call_capturetrainingImage, height = 1, width = 16)
    self.slogan.pack(side=TOP, ipady=10)
    self.slogan = Button(frame,
                         text="Start Training",
                         command=self.call_startTraining, height = 1, width = 16)
    self.slogan.pack(side=TOP, ipady= 10)
    self.slogan = Button(frame,
                         text="Authenticate",
                         command=self.call_Authenticate, height = 1, width = 16)
    self.slogan.pack(side=TOP, ipady= 10)
    self.button = Button(frame, 
                         text="QUIT", fg="red",
                         command=frame.quit, height = 1, width = 16)
    self.button.pack(side=TOP, ipady= 10)
    
  def call_captureImage(self):
    print "Calling capture image!"
  def call_capturetrainingImage(self):
    print "Calling capture training image!"
  def call_startTraining(self):
    print "Calling start training image!"
  def call_Authenticate(self):
    print "Matching in database!"

root = tk.Tk()



app = App(root)
root.mainloop()


