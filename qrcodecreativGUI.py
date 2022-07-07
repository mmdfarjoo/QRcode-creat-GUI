import pyqrcode #pip install pyqrcode
import png #pip install pypng
from pyqrcode import QRCode 
from tkinter import * #pip install tkinter (on linux)

#light mood 
def light ():
    
    win['background']="white"
    lbl_convert.config(fg='black',bg="white")
    lbl_image.config(fg="black",bg="white")
    En_text.config(bg="white",fg='black')
    En_image.config(bg="white",fg='black')
    btn.config(fg='black',bg="white")
#dark mood
def dark ():
    
    win['background']="black"
    lbl_convert.config(fg='white',bg="black")
    lbl_image.config(fg="white",bg="black")
    En_text.config(bg="black",fg='white')
    En_image.config(bg="black",fg='white')
    btn.config(fg='white',bg="black")

#qrcode command
def qrcode ():
    
    d =( En_image.get() + ".png")
    url = pyqrcode.create(En_text.get())
    url.show()
    url.png(d , scale=6)

#creat frame 
win=Tk()
#fixed frame 
win.geometry('460x100')
#background in win defult
win['background']='black'
#frame title 
win.title("QRcode creat GUI")


#creat label and entry for text to cover to qrcode
lbl_convert= Label(win,text="Enter Text To Convert : " , bg = 'black',fg='white')
lbl_convert.grid(row=0 , column=1)
En_text=Entry(win,fg='white',bg='black',width=30)
En_text.grid(row=0 , column=3)

#creat label and entry for save name image
lbl_image=Label(win,text="Enter Image Name To Save  : " , bg = 'black',fg='white')
lbl_image.grid(row=1 , column=1)
En_image=Entry(win,fg='white',bg='black', width=30)
En_image.grid(row=1 , column=3)

#button convert and save image
btn=Button(win,text='convert',fg='white',bg = 'black',command=qrcode)
btn.grid(row=3, column=3)



#creat menu bar and command
menubar= Menu(win)
menuin = Menu(menubar, tearoff=0)
menuin.add_command(label='Light mood',command=light)
menuin.add_command(label='Dark mood',command=dark)
menubar.add_cascade(label='Theme',menu= menuin)

win.config(menu=menubar)

#resizable false 
win.resizable(False,False)
#mian loop win (frame home)
win.mainloop()