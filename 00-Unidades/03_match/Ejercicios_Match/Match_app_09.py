import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre:
apellido:
---
Ejercicio: Match_09
---
Una agencia de viajes cobra $15.000 por cada estadía como base. 
Luego para calcular las tarifas total realiza el siguiente cálculo, 
en función de la estación del año y del destino elegido:
    Si es invierno: 
        Bariloche tiene un Precio_final del 20% 
        Cataratas y Córdoba tienen un Precio_final del 10%
        Mar del plata tiene un Precio_final del 20%
    Si es Verano:
        Bariloche tiene un Precio_final del 20%
        Cataratas y Cordoba tienen un Precio_final del 10%
        Mar del plata tiene un Precio_final del 20%
    Si es Primavera u Otoño:
        Bariloche tiene un Precio_final del 10%
        Cataratas tiene un Precio_final del 10%
        Mar del plata tiene un Precio_final del 10%
        Córdoba tiene precio sin Precio_final

'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.label_estaciones = customtkinter.CTkLabel(master=self, text="Estaciones")
        self.label_estaciones.grid(row=0, column=0, padx=20, pady=10)
        estaciones = ['Verano', 'Otoño', 'Invierno', 'Primavera']
        self.combobox_estaciones = customtkinter.CTkComboBox(master=self, values=estaciones)
        self.combobox_estaciones.grid(row=1, column=0, padx=20, pady=(10, 10))

        
        self.label_destinos = customtkinter.CTkLabel(master=self, text="Destinos")
        self.label_destinos.grid(row=2, column=0, padx=20, pady=10)
        destinos = ['Bariloche', 'Mar del plata', 'Cataratas', 'Cordoba']
        self.combobox_destino = customtkinter.CTkComboBox(master=self, values=destinos)
        self.combobox_destino.grid(row=3, column=0, padx=20, pady=(10, 10))

        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=4, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        destino = self.combobox_destino.get()
        estacion = self.combobox_estaciones.get()

        estadia_por_base = 15000
        Precio_final = 0

        match estacion:
            case "Invierno":
                match destino:
                    case "Bariloche":
                        Precio_final = 1.20
                    case "Mar del plata":
                        Precio_final = 0.80
                    case "Cataratas" | "Cordoba": 
                        Precio_final = 0.90
                    case _:
                        pass
        
       
            case "Verano":
                match destino:
                    case "Bariloche":
                        Precio_final = 0.80
                    case "Mar del plata":
                        Precio_final = 1.10
                    case "Cataratas" | "Cordoba": 
                        Precio_final = 1.10
                    case _:
                        pass

      
            case "Otoño" | "Primavera":
                match destino:
                    case "Bariloche":
                        Precio_final = 1.10
                    case "Mar del plata":
                        Precio_final = 1.10
                    case "Cataratas" :
                        Precio_final = 1.10
                    case "Cordoba":
                        Precio_final = 1
                    case _:
                        pass

        
          
        
        precio_total = (estadia_por_base * Precio_final)

        alert("Precio final", f"el total por la estadia es de {precio_total}")

               
            
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()