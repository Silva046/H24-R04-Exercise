# Programme pour créer un 
# GUI avec le module customtkinter 
import customtkinter as ctk
import tkinter as tk

# pour l'apparence de la fenêtre  (choix Light, Dark, System)
ctk.set_appearance_mode('Dark')


# pour l'apparence des composants graphiques dans la fenêtre
# choix possibles: green, dark-blue, blue
ctk.set_default_color_theme('green')

# Dimensions de la fenêtre
ChoixWidth, ChoixHeight = 500, 500
ChoixPrix = {"AMD Ryzen 9 5950X         ":669.98,
           "AMD Ryzen 7 5800X3        ":438.98,
           "Intel Core i9 12900 K     ":569.99,
           "Intel Core i7 12700 K     ":428.99,
           "GeForce RTX 3090Ti        ":2379.99,
           "GeForce RTX 3080Ti        ":1639.99,
           "GeForce RTX 3070Ti        ":819.99,
           "Radeon RX 6950 XT         ":610.99,
           "G.SKILL Trident Z5        ":670.29,
           "CORSAIR Dominator         ":284.99,
           "CORSAIR Vengeance         ":310.99,
           "G.SKILL Ripjaws V         ":119.59  }

# Choix Class
class appChoix(ctk.CTk):

    def __init__(self,titre:str,message:str, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # titre de la fenêtre
        self.title(titre)
        # dimensions de la fenêtre
        self.geometry(f"{ChoixWidth}x{ChoixHeight}")
        self.grid_rowconfigure((0,1,2,3,4), weight=1)  # configure grid system
        self.grid_columnconfigure((0,1), weight=1, uniform="column")
        
        # CTkLabel pour directive
        self.lbl_directive = ctk.CTkLabel(self,
                                    text=message,width=100,
                               height=25 ,fg_color='red')
        self.lbl_directive.grid(row=0, column=0,columnspan=2,
                                padx=20, pady=(0,5) ,sticky="ew")   
        # CTkOptionMenu  pour les choix de processeurs
        self.lbl_processeur = ctk.CTkLabel(self,text="Choisis ton processeur    ")
        self.lbl_processeur.grid(row=1,column=0,sticky="e")
        self.choix_processeur = ctk.CTkOptionMenu(self,
                                    values=[
                                    "Choisis ton processeur    ",
                                    "AMD Ryzen 9 5950X         ",
                                    "AMD Ryzen 7 5800X3        ",
                                    "Intel Core i9 12900 K     ",
                                    "Intel Core i7 12700 K     "],width=200,
                               height=25)
        self.choix_processeur.grid(row=1, column=1,
                                    padx=(0,20), pady=(0,5),
                                     sticky="e")
        # CTkOptionMenu  pour les choix de carte graphique
        self.lbl_gpu = ctk.CTkLabel(self,text="Choisis ta carte graphique")
        self.lbl_gpu.grid(row=2,column=0,sticky="e")
        self.choix_carte_graphique = ctk.CTkOptionMenu(self,
                                    values=[
                                    "Choisis ta carte graphique",
                                    "GeForce RTX 3090Ti        ",
                                    "GeForce RTX 3080Ti        ",
                                    "GeForce RTX 3070Ti        ",
                                    "Radeon RX 6950 XT         "],width=200,
                               height=25)
        self.choix_carte_graphique.grid(row=2, column=1,
                                    padx=20, pady=(0,5),
                                     sticky="e")
        # CTkOptionMenu pour les choix de barrettes RAM
        self.lbl_ram = ctk.CTkLabel(self,text="Choisis ta RAM            ")
        self.lbl_ram.grid(row=3,column=0,sticky="e")
        self.choix_RAM = ctk.CTkOptionMenu(self,
                                    values=[
                                    "Choisis ta RAM            ",
                                    "G.SKILL Trident Z5        ",
                                    "CORSAIR Dominator         ",
                                    "CORSAIR Vengeance         ",
                                    "G.SKILL Ripjaws V         "],width=200,
                               height=25)
        self.choix_RAM.grid(row=3, column=1,
                                    padx=20, pady=(0,5),
                                     sticky="e")
  
        # CTkButton estimer
        self.btn_estimer = ctk.CTkButton(self,
                                        text="Obtenir estimé",
                                        command=self.estimer,width=200,
                               height=25)
        self.btn_estimer.grid(row=4, column=0,
                                         padx=60,
                                        pady=(0,5), sticky="w")


        # CTkLabel pour messages
        self.lbl_message = ctk.CTkLabel(self,
                                    text="Commence par choisir tes composantes",width=200,
                               height=25)
        self.lbl_message.grid(row=4, column=1,
                                padx=5,pady=(0,5) ,sticky="ew")  #enlevé sticky="ew"
    # Pour obtenir un estimé
    def estimer(self):
        
        processeur = self.choix_processeur.get()
        carte_graphique = self.choix_carte_graphique.get()
        RAM = self.choix_RAM.get()
        if (processeur[:7] != 'Choisis'):
            if (carte_graphique[:7] != 'Choisis'):
                if(RAM[:7] != 'Choisis'):
                    total = ChoixPrix.get(processeur) + ChoixPrix.get(carte_graphique) + ChoixPrix.get(RAM)
                    self.lbl_message.configure(text=f"Pour tes choix, l'estimé est de {round(total,2)}$.")
                else:
                    self.lbl_message.configure(text=f"Tu dois choisir une barrette RAM.")    
            else:
                self.lbl_message.configure(text=f"Tu dois choisir une carte graphique.")    
        else:
            self.lbl_message.configure(text=f"Tu dois choisir un processeur")                


if __name__ == "__main__":
    Choix = appChoix("Construit ton PC !","Choisi tes composants")
    Choix.mainloop()    
