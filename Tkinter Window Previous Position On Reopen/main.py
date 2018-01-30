from tkinter import *
from tkinter import messagebox

try:
    #tkposition has value of window position try if its exist
    from tkposition import *
except:
    #except if tkposition.py not exist
    False
    
try:
    #if tkposition.py exist and it has previous position
    a=winpos[0]
    b=winpos[1]
except:
    #default position is some error
    a=100
    b=200
    
root=Tk()
root.geometry("500x500+%s+%s"%(a,b))
def abc():
    x=str(root.winfo_x()) #current window x position
    y=str(root.winfo_y()) #current window y position
    file=open("tkposition.py","w") #create file tkposition.py or open if its exist
    posval="winpos=["+x+","+y+"]"  #Initialize current position in file
    file.write(posval) #Write position in file
    file.close()
    root.destroy()
root.protocol("WM_DELETE_WINDOW", abc) #Action when we click red close button of Tkinter Window
