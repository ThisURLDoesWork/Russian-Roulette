import tkinter as tk
from tkinter import *
from tkinter import messagebox as tm
from random import randint
window=Tk()
#top=Toplevel()
window.title("Queue Game 2")
string=Label(window,text="Queue Game 2")
spinning="You have spun the chambers"
game_over="You're dead!"
winning="Congratulations!"
chamber=0
select=0

class CircularQueue():
  
  # constructor for the class
  # taking input for the size of the Circular queue 
  # from user
  def __init__(self, maxSize):
    self.queue = list()
    # user input value for maxSize
    self.maxSize = maxSize
    self.head = 0
    self.tail = 0

  # add element to the queue
  def enqueue(self, data):
    # if queue is full
    if self.size() == (self.maxSize - 1):
      return("Queue is full!")
    else:
      # add element to the queue
      self.queue.append(data)
      # increment the tail pointer
      self.tail = (self.tail+1) % self.maxSize
      return True
  
  # remove element from the queue
  def dequeue(self):
    # if queue is empty
    if self.size() == 0:
      return("Queue is empty!")
    else:
      # fetch data
      data = self.queue[self.head]
      # increment head
      self.head = (self.head+1) % self.maxSize
      return data

  # find the size of the queue
  def size(self):
    if self.tail >= self.head:
      qSize = self.tail - self.head
    else:
      qSize = self.maxSize - (self.head - self.tail)
    # return the size of the queue
    return qSize
def choice():
    global chamber,ob
def spin():
    global chamber
    chamber=randint(1,6)
    choice()    
    #tm.showinfo("Spin",spinning)
    tm.showinfo("New chamber value",chamber)
    #l2=Label(top,text="{}".format(chamber))
    #l2.pack()

def fire():
    global chamber
    y=ob.dequeue()
    if int(chamber) == y:
        tm.showinfo("chamber:",chamber)#"Y",y)
        tm.showinfo("Game ends",game_over)
        return
    elif int(chamber)==0:
        tm.showinfo("chamber:",chamber)#"Y",y)
        tm.showinfo("Game ends",winning)
        return
    else:
        tm.showinfo("chamber:",chamber)#"Y",y)
    chamber -= 1
    choice()


def quit():
    quitchoice=tm.askquestion("Exit","Are you sure you want to exit?")
    if quitchoice=='yes':
        window.destroy()

ob = CircularQueue(6)
ob.enqueue(0)
ob.enqueue(1)
ob.enqueue(2)
ob.enqueue(3)
ob.enqueue(4)
ob.enqueue(5)
x=0
spin()
choice()

fire=Button(window,text="Fire!",padx=20,pady=15,command=fire,anchor=CENTER)
spin=Button(window,text="Spin",padx=20,pady=15,command=spin,anchor=CENTER)
quit=Button(window,text="Quit",padx=20,pady=15,command=quit,anchor=CENTER)

fire.grid(row=3,column=0)
spin.grid(row=3,column=1)
quit.grid(row=3,column=2)

window.mainloop()

