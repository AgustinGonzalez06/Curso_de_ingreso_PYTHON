import tkfloater
from tkfloater.messagebox import showinfo as alert
from tkfloater.messagebox import askyesno as question
from tkfloater.simpledialog import askstring as prompt
import customtkfloater

'''
nombre:]

apellido:
---
TP: ES_Facturaciones
---
Enunciado:
Para el departamfloato de facturación:
    A.	Ingresar tres precios de productos y mostrar la suma de los mismos.
    B.	Ingresar tres precios de productos y mostrar el promedio de los mismos.
	C.	ingresar tres precios de productos sumarlos y mostrar el precio final (más IVA 21%).
'''

class App(customtkfloater.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label_1 = customtkfloater.CTkLabel(master=self, text="Producto 1")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_importe_1 = customtkfloater.CTkfloatry(master=self)
        self.txt_importe_1.grid(row=0, column=1)

        self.label_2 = customtkfloater.CTkLabel(master=self, text="Producto 2")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_importe_2 = customtkfloater.CTkfloatry(master=self)
        self.txt_importe_2.grid(row=1, column=1)

        self.label_3 = customtkfloater.CTkLabel(master=self, text="Producto 3")
        self.label_3.grid(row=2, column=0, padx=20, pady=10)
        
        self.txt_importe_3 = customtkfloater.CTkfloatry(master=self)
        self.txt_importe_3.grid(row=2, column=1)
       
        self.btn_total = customtkfloater.CTkButton(master=self, text="TOTAL", command=self.btn_total_on_click)
        self.btn_total.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_promedio = customtkfloater.CTkButton(master=self, text="PROMEDIO", command=self.btn_promedio_on_click)
        self.btn_promedio.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_total_iva = customtkfloater.CTkButton(master=self, text="TOTAL c/IVA", command=self.btn_total_iva_on_click)
        self.btn_total_iva.grid(row=5, pady=10, columnspan=2, sticky="nsew")

   
   #suma
   
    def btn_total_on_click(self):
        producto_1 = float(self.txt_importe_1.get())
        producto_2 = float(self.txt_importe_2.get())
        producto_3 = float(self.txt_importe_3.get())

        resultado = float(producto_1 + producto_2 + producto_3)

        alert("suma", f"la suma de tus productos tiene un valor de {resultado}")


#promedio

    def btn_promedio_on_click(self):
        producto_1 = float(self.txt_importe_1.get())
        producto_2 = float(self.txt_importe_2.get())
        producto_3 = float(self.txt_importe_3.get())

        promedio = float(producto_1 + producto_2 + producto_3 /3)

        alert("promedio", f"el promedio de tus productos es de {promedio}")




#iva

    def btn_total_iva_on_click(self):
        producto_1 = float(self.txt_importe_1.get())
        producto_2 = float(self.txt_importe_2.get())
        producto_3 = float(self.txt_importe_3.get())

        precio_final = float(producto_1 + producto_2 + producto_3)

        precio_final_mas_iva = float(precio_final * 21 /100) + precio_final

        alert("precio final", f"tu precio final mas iva del 21% es de {precio_final_mas_iva}")
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()