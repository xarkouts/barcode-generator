from random import seed
from random import randrange
import time
from barcode import EAN13
from barcode.writer import ImageWriter 
seed(time.time())
i=0
name="barcode "
frasi=" Διμηουργιθηκε Επιτιχος"
while(True):
 a=input("Ποσα barcode θελεις να δυμιουργησεις ; \n")
 if a.isnumeric()==True:
     a=int(a)
     break
 print('Αυτο που πληκτρολογησες δεν ειναι αρηθμος παρακαλο πληκτρολογησε ενα θετικο ακερεο αριθμο ') 
for  i in range(a):
    bcn=randrange(00000000000000,99999999999999)
    bcn=str(bcn)
    b=i+1
    b=str(b)
    fs=name+b
    minima=name+b+frasi
    barcode=EAN13(bcn,writer=ImageWriter())
    if barcode.save(fs):
        print(minima)
    if i==a-1:
        print("ΤΕΛΟΣ!!!")    
    


