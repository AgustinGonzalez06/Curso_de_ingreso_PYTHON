import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import math 
'''
nombre:Agustin
apellido:Gonzalez
---
TP: IF_Iluminacion
---
Enunciado:
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
           Marca = self.combobox_marca.get()
           txt_cantidad = self.combobox_cantidad.get()
           cantidad = int(txt_cantidad)

           

           precio_lampara = 800

           if cantidad >5:
                 descuento =0.5
           elif cantidad == 5:
                if Marca == "ArgentinaLuz":
                      descuento = 0.40
                else:
                      descuento = 0.30
                   

           elif cantidad == 4:
               if Marca == "ArgentinaLuz" or "FelipeLamparas":
                     descuento = 0.25
               else:
                     descuento = 0.20
           elif cantidad == 3:
                if Marca == "ArgentinaLuz":
                     descuento = 0.15

                elif Marca == "FelipeLamparas":
                     descuento = 0.1
                else:
                     descuento = 0.05
           else:
                descuento = 0

                
           
                     

            
           total = cantidad * precio_lampara
           total_con_descuento = int(total - (total * descuento))
           
           if total_con_descuento <4001:
                mensaje = f"el importe total es de {total_con_descuento}"
           


           if total_con_descuento >4000:
                descuento_add = 0.05
           else:
                descuento_add = 0

                
           total_final = total_con_descuento - (total_con_descuento * descuento_add)
           
           mensaje = f"el importe total sera de ${total_final}"

        
           alert("importe", mensaje )
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()