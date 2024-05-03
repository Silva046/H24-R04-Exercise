import tkinter
import tkinter.filedialog
import tkinter.messagebox
import customtkinter
import csv

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # attributs importants
        self.tableau_valeurs= [] #va contenir un tableau de tous les labels / entry des valeurs


        # Fenêtre mère
        self.title("Lecteur de CSV simple")
        self.geometry(f"{1050}x{830}")

        # Frame top
        self.top_frame = customtkinter.CTkFrame(self, width=1100, corner_radius=20)
        self.top_frame.grid(row=0,padx=(20, 20), sticky="nsew")

        ## ctk entry
        self.entry = customtkinter.CTkEntry(self.top_frame, placeholder_text="chemin/vers/fichier",width=900)
        self.entry.grid(row=0, padx=(20, 20),  sticky="w")

        ## button load
        self.btn_charger = customtkinter.CTkButton(self.top_frame, text="Sélectionner",height=30)
        self.btn_charger.grid(row=0, padx=(20,20), pady=10,sticky="e")
 

        # Frame tableau csv
        self.csv_frame = customtkinter.CTkScrollableFrame(self, height=700,width=1000)
        self.csv_frame.grid(row=1,padx=(20, 0), sticky="nsew")
        
        # Frame bottom
        self.bottom_frame = customtkinter.CTkFrame(self, width=1100, corner_radius=20)
        self.bottom_frame.grid(row=3,padx=(20,0), sticky="nsew")

        self.btn_save = customtkinter.CTkButton(self.bottom_frame, text="Enregistrer",height=30)
        self.btn_save.grid( padx=(20,0), sticky="e")


    # Prend en paramètre la première ligne d'un csv
    # Place ces éléements dans une série de frames contenue dans csv_frame
    # Retourne cette liste de frames pour pouvoir l'utilisé
    def _charger_en_tete(self,ligne) -> list:
        en_tete_valeurs = []
        frames_colonnes = []
        for num, etiquette in enumerate(ligne):
            frame_une_colonne = customtkinter.CTkFrame(self.csv_frame,corner_radius=30,fg_color='white')
            frame_une_colonne.grid(row=0,column=num)
            element = customtkinter.CTkLabel(frame_une_colonne,text=etiquette,padx=10)
            element.grid(row=0)
            en_tete_valeurs.append(element)
            frames_colonnes.append(frame_une_colonne)
        self.tableau_valeurs.append(en_tete_valeurs)
        return frames_colonnes

    def charger_csv(self, path):
        with open(path,'r',encoding='utf-8') as f_lu :
            csv_reader = csv.reader(f_lu,delimiter=',')
            en_tete = next(csv_reader)
            
            # Création des colonnes du tableau et chargement des valeurs de l'en-têtes
            self.tableau_valeurs = []
            frames_colonnes = self._charger_en_tete(en_tete)
            
            #for numRow,ligne in enumerate(csv_reader) :
            #    ligne_valeurs = []
            #    for numCol,valeur in enumerate(ligne):
            


    def enregistrer_csv(self):
        pass

    def selection_fichier(self):
        pass
        

    def selection_enregistrement(self):
        pass





if __name__ == "__main__":
    app = App()
    #print(app.selection_fichier())
    app.mainloop()