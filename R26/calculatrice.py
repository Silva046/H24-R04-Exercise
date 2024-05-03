import tkinter
import customtkinter


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # Fenêtre mère
        self.title("Lecteur de CSV simple")
        self.geometry(f"{480}x{520}")
        # Frame top
        self.top_frame = customtkinter.CTkFrame(self,height=160, corner_radius=20)
        self.top_frame.grid(row=0,column=0,columnspan=4,padx=30, sticky="nsew")
        ## Écran Formule
        self.ecran = customtkinter.CTkEntry(self.top_frame,placeholder_text="Formule",height=100,width=400)
        self.ecran.grid()
        # Frame Buttons
        self.btn_frame = customtkinter.CTkFrame(self, corner_radius=20,fg_color='white')
        self.btn_frame.grid(row=1,column=0,columnspan=4,rowspan=4,padx=30, sticky="nsew")

        ##Numberbuttons
        self.btn0 = customtkinter.CTkButton(self.btn_frame,text=0,height=100,width=100,command=lambda : self.ajout_formule(0),font=('',40)).grid(row=3,column=0)
        self.btn1 = customtkinter.CTkButton(self.btn_frame,text=1,height=100,width=100,command=lambda : self.ajout_formule(1),font=('',40)).grid(row=2,column=0)
        self.btn2 = customtkinter.CTkButton(self.btn_frame,text=2,height=100,width=100,command=lambda : self.ajout_formule(2),font=('',40)).grid(row=2,column=1)
        self.btn3 = customtkinter.CTkButton(self.btn_frame,text=3,height=100,width=100,command=lambda : self.ajout_formule(3),font=('',40)).grid(row=2,column=2)
        self.btn4 = customtkinter.CTkButton(self.btn_frame,text=4,height=100,width=100,command=lambda : self.ajout_formule(4),font=('',40)).grid(row=1,column=0)
        self.btn5 = customtkinter.CTkButton(self.btn_frame,text=5,height=100,width=100,command=lambda : self.ajout_formule(5),font=('',40)).grid(row=1,column=1)
        self.btn6 = customtkinter.CTkButton(self.btn_frame,text=6,height=100,width=100,command=lambda : self.ajout_formule(6),font=('',40)).grid(row=1,column=2)
        self.btn7 = customtkinter.CTkButton(self.btn_frame,text=7,height=100,width=100,command=lambda : self.ajout_formule(7),font=('',40)).grid(row=0,column=0)
        self.btn8 = customtkinter.CTkButton(self.btn_frame,text=8,height=100,width=100,command=lambda : self.ajout_formule(8),font=('',40)).grid(row=0,column=1)
        self.btn9 = customtkinter.CTkButton(self.btn_frame,text=9,height=100,width=100,command=lambda : self.ajout_formule(9),font=('',40)).grid(row=0,column=2)

        ## Autres btn
        self.plus = customtkinter.CTkButton(self.btn_frame,text='+',height=100,width=100,fg_color='grey',command=lambda : self.ajout_formule(' + '),font=('',40)).grid(row=0,column=3)
        self.moins = customtkinter.CTkButton(self.btn_frame,text='-',height=100,width=100,fg_color='grey',command=lambda : self.ajout_formule(' - '),font=('',40)).grid(row=1,column=3)
        self.multiple = customtkinter.CTkButton(self.btn_frame,text='x',height=100,width=100,fg_color='grey',command=lambda : self.ajout_formule(' x '),font=('',40),state='disabled').grid(row=2,column=3)
        self.egal = customtkinter.CTkButton(self.btn_frame,text='=',height=100,width=100,fg_color='green',command=self.resoudre_equation,font=('',40)).grid(row=3,column=3)
        self.delete = customtkinter.CTkButton(self.btn_frame,text='del',height=100,width=100,fg_color='red',command=self.effacer_ecran,font=('',40)).grid(row=3,column=2)


    # Ajoute le paramètre "caractere" à la fin de l'objet <CTkEntry> self.ecran (Voir la documentation)
    def ajout_formule(self,caractere):
        # Obtenez la longueur de la chaine de caractère dans self.ecran
        # Insérez le caractère à la fin du self.ecran 
        pass

    # Résous l'équation afficher dans self.ecran
    def resoudre_equation(self):
        # Appelez la méthode lire_equation et capturez le retour
        # Effacez le contenue de self.ecran
        # Affichez le nouveau résultat
        pass

    # Lis l'équation de gauche à droite, sans priorité d'opération.
    # Retourne le résultat de l'opération
    def lire_equation(self):
        # Séparez l'équation en différentes parties avec split(), entreposé le résultat dans une variable.
        # Initialisé une variable totale à la valeur du premier élément de la liste
        # Passez au travers de la liste en utilisant la fonction range()
        #       cette fonction retourne l'index de chaque élément.
        #       pour chaque élément, regarder s'il s'agit d'un "+", d'un "-", ou autre
        #           si c'est un "+" ; additionnez le prochain élément de la liste au total
        #           si c'est un "-" ; soustrayez le prochain élément de la liste au total

        return 0

    # Efface le contenu de l'écran self.ecran
    def effacer_ecran(self):
        pass

if __name__ == "__main__":
    app = App()
    app.mainloop()