from tkinter import*
import barcode
import random
from barcode.writer import ImageWriter
from PIL.ImageTk import PhotoImage


data = dict()

generatedBarcode = []

def NumberGenerator():
    num1 = "1234569870"
    num2 = "1234569870"
    number = num1 + num2
    length = 12 
    result = "".join(random.sample(number,length))
    return result


def barcode_Generate():
    product = productNameEntry.get()
    price = priceEntry.get()
    
    barcode_format = barcode.get_barcode_class('upc')

    barcodeNumber = NumberGenerator
    generated = barcode_format(barcodeNumber , writer=ImageWriter() )
    generated.save(product)
    generatedBarcode.append(f"{product}.png")
    data[barcodeNumber] = [product,price,f"{product}.png" ]

    NumberGenerator()
Generator = Tk

Generator.title("Barcode Generator")

Generator.geometry("600x600")


productName = Label(Generator, text='product Name',font=('bold',10)).pack()
productName.place(x=150, y=50)

productNameEntry = Entry(Generator, width=20)
productNameEntry.place(x=270 , y=50)

price = Label(Generator, text='price',font=('bold',10)).pack()
price.place(x=150, y=80)

priceEntry = Entry(Generator, width=20)
priceEntry.place(x=270 , y=50)



Button(Generator, text='Generate', width=20, bg='light green', fg='white', font=('bold',10)command=barcode_Generate).place(x=200,y=130)

image = Label(Generator)
image.place(x=50,y=200)

label = Label(Generator)
label.place(x=250, y=500)



while  True:

    for img in generatedBarcode:
        img= PhotoImage(file=img)
        image['image'] = img
        label['text'] = productNameEntry.get(), priceEntry.get()
        label['text']= data
    Generator.update()

