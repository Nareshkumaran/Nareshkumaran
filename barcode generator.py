import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from barcode import Code128
from PIL import ImageTk, Image

class BarcodeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Product Barcode Generator")

        self.label_product_name = tk.Label(self.root, text="Product Name:")
        self.label_product_name.pack(pady=10)

        self.entry_product_name = tk.Entry(self.root, width=30)
        self.entry_product_name.pack()

        self.btn_generate = tk.Button(self.root, text="Generate Barcode", command=self.generate_barcode)
        self.btn_generate.pack(pady=10)

        self.label_barcode = tk.Label(self.root, text="")
        self.label_barcode.pack(pady=10)

        self.btn_save = tk.Button(self.root, text="Save Barcode", command=self.save_barcode)
        self.btn_save.pack(pady=10)

    def generate_barcode(self):
        product_name = self.entry_product_name.get().strip()
        if not product_name:
            messagebox.showerror("Error", "Please enter a product name")
            return

        
        barcode = Code128(product_name)

        
        barcode_filename = "temp_barcode.png"
        barcode.save(barcode_filename)

        
        barcode_image = Image.open(barcode_filename)
        barcode_image = barcode_image.resize((300, 150))
        self.barcode_img = ImageTk.PhotoImage(barcode_image)

        
        self.label_barcode.config(image=self.barcode_img)
        self.label_barcode.image = self.barcode_img

    def save_barcode(self):
        if not hasattr(self, 'barcode_img'):
            messagebox.showerror("Error", "Please generate a barcode first")
            return

    
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            
            Image.open("temp_barcode.png").save(file_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = BarcodeGeneratorApp(root)
    root.mainloop()
