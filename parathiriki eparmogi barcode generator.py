from tkinter import *
from tkinter import ttk
from random import seed
from random import randrange
import time
from barcode import EAN13
from barcode.writer import ImageWriter 
seed(time.time())
def bcg():
    i=0
    name="barcode "
    frasi=" Διμηουργιθηκε Επιτιχος"
    while(True):
     a=aritmos.get()
     a=a.strip()
     if a.isnumeric()==True:
        a=int(a)
        break
     minimata["text"]=f"Αυτο που πληκτρολογησες δεν ειναι αρηθμος παρακαλο πληκτρολογησε ενα θετικο ακερεο αριθμο"
     return
    try:
     c=100/a
    except ZeroDivisionError:
        return 
    for  i in range(a):
     bcn=randrange(00000000000000,9999999999999999)
     bcn=str(bcn)
     b=i+1
     b=str(b)
     fs=name+b
     minima=name+b+frasi
     barcode=EAN13(bcn,writer=ImageWriter())
     if barcode.save(fs):
        
         while(i<=a-1):
              time.sleep(1)
              mybar["value"]+=c
              minimata["text"]=minima
              root.update_idletasks()
              break
    
         if i==a-1:
             time.sleep(1)
             minimata["text"]=f"               ΤΕΛΟΣ!!!                              "
             root.update_idletasks()
    time.sleep(2)
    katharo()
    return     
         
         
def katharo():
    mybar.stop()
    minimata["text"]=""
    aritmos.delete(0,"end")        
         

       
             
root=Tk()
root.title("barcode generaitor") 
root.geometry('600x200')
perigrafi=Label(root,text="Ποσα barcode θελεις να δυμιουργησεις ; \n ")
perigrafi.pack()
aritmos=Entry(root)
aritmos.pack()
bt=Button(root,text="Διμιουργια",command=bcg)
bt.pack()
mybar=ttk.Progressbar(root,orient=HORIZONTAL,length=300,mode="determinate")
mybar.pack(pady=20)
minimata=Label(root,text=" ")
minimata.pack()
root.mainloop()

