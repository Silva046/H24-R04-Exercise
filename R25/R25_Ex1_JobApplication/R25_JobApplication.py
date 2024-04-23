import customtkinter as ctk
import tkinter as tk
import os
from PIL import ImageTk, Image   #il faut installer pillow  (pip install pillow)

ctk.set_appearance_mode("System")

ctk.set_default_color_theme("green")


appWidth, appHeight = 1000, 800



class App(ctk.CTk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Technicien Reseau Niveau 2")
        self.geometry(f"{appWidth}x{appHeight}")

        self.rowconfigure((0,1,2,3,4), weight=1)
        self.columnconfigure((0,1), weight=1, minsize=200)

        self.image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.logo_image = ImageTk.PhotoImage(Image.open(os.path.join(self.image_path, "logomatissoft.jpg")))

        ########  FRAME container central
        frm_container = tk.Frame(
            master=self,
            relief=tk.RIDGE,
            borderwidth=1
        )
        frm_container.grid(row=0, column=0,columnspan=2, padx=5, pady=0)

        # lbl pour le logo de l'entreprise
        self.lbl_logo  = tk.Label(master=frm_container, image=self.logo_image)
        self.lbl_logo.grid(row=0,column=0,columnspan=2,padx=5,pady=2, sticky="ew") #,columnspan=2,padx=5,pady=2
        
        # Entry pour le nom
        self.ent_nom = ctk.CTkEntry(master=frm_container,
                        placeholder_text="Entrez votre nom")
        self.ent_nom.grid(row=1, column=0,
                            columnspan=2, padx=5,
                            pady=2, sticky="ew")

        ########  FRAME Experience
        frm_experience = tk.Frame(
            master=frm_container,
            relief=tk.RIDGE,
            borderwidth=1,height=400
        )
        frm_experience.grid(row=2, column=0, padx=5, pady=2,sticky="nsew")

        # Label Experience
        self.lbl_experience = ctk.CTkLabel(master=frm_experience,
                                        text="Cochez tous les points pour lequel vous avez de l'expérience")
        self.lbl_experience.grid(row=0, column=0, padx=5, pady=2, sticky="ew")

        # Check boxes

        self.chk_1 = ctk.CTkCheckBox(master=frm_experience,
                            text="Programmation Python",
                            onvalue=1, offvalue=0)
        
        self.chk_1.grid(row=1, column=0, padx=5, pady=2, sticky="ew")


        self.chk_2 = ctk.CTkCheckBox(master=frm_experience,
                            text="Programmation PowerShell",
                            onvalue=1, offvalue=0) 
                                   
        self.chk_2.grid(row=2, column=0, padx=5, pady=2, sticky="ew")


        self.chk_3 = ctk.CTkCheckBox(master=frm_experience,
                            text="Maintenance des serveurs",
                            onvalue=1, offvalue=0) 
                                   
        self.chk_3.grid(row=3, column=0, padx=5, pady=2, sticky="ew")


        self.chk_4 = ctk.CTkCheckBox(master=frm_experience,
                            text="Maintien des postes de travail",
                            onvalue=1, offvalue=0) 
                                   
        self.chk_4.grid(row=4, column=0, padx=5, pady=2, sticky="ew")


        self.chk_5 = ctk.CTkCheckBox(master=frm_experience,
                            text="Maintien du réseau câblé et sans fil",
                            onvalue=1, offvalue=0) 
                                   
        self.chk_5.grid(row=5, column=0, padx=5, pady=2, sticky="ew")
        

        self.chk_6 = ctk.CTkCheckBox(master=frm_experience,
                            text="Maintien des autres périphériques",
                            onvalue=1, offvalue=0) 
                                   
        self.chk_6.grid(row=6, column=0, padx=5, pady=2, sticky="ew")


        self.chk_7 = ctk.CTkCheckBox(master=frm_experience,
                            text="Gestion des licences",
                            onvalue=1, offvalue=0) 
                                   
        self.chk_7.grid(row=7, column=0, padx=5, pady=2, sticky="ew")


        self.chk_8 = ctk.CTkCheckBox(master=frm_experience,
                            text="Formation usagers",
                            onvalue=1, offvalue=0) 
                                   
        self.chk_8.grid(row=8, column=0, padx=5, pady=2, sticky="ew")


        self.chk_9 = ctk.CTkCheckBox(master=frm_experience,
                            text="Gestion des accès usagers",
                            onvalue=1, offvalue=0) 
                                   
        self.chk_9.grid(row=9, column=0, padx=5, pady=2, sticky="ew")

        self.chk_10 = ctk.CTkCheckBox(master=frm_experience,
                            text="Gestion des anti-virus", onvalue=1, offvalue=0) 
                                   
        self.chk_10.grid(row=10, column=0, padx=5, pady=2, sticky="ew")


        self.chk_11 = ctk.CTkCheckBox(master=frm_experience,
                            text="Gestion des télécommunications",
                            onvalue=1, offvalue=0) 
                                   
        self.chk_11.grid(row=11, column=0, padx=5, pady=2, sticky="ew")


        self.chk_12 = ctk.CTkCheckBox(master=frm_experience,
                            text="Gestion des routeurs",
                            onvalue=1, offvalue=0) 
                                   
        self.chk_12.grid(row=12, column=0, padx=5, pady=2, sticky="ew")

        self.list_checkbox = [self.chk_1,self.chk_2,self.chk_3,self.chk_4,self.chk_5,self.chk_6,self.chk_7,self.chk_8,self.chk_9,self.chk_10,self.chk_11,self.chk_12]

        ########  FRAME Interet
        frm_interet = tk.Frame(
            master=frm_container,
            relief=tk.RIDGE,
            borderwidth=1, width=200
        )
        frm_interet.grid(row=2, column=1, padx=5, pady=0,sticky="nsew")   

         # Label interet
        self.lbl_interet = ctk.CTkLabel(master=frm_interet,
                                        text="Choisissez un point qui vous intéresse le plus")
        self.lbl_interet.grid(row=0, column=0,
                            padx=5, pady=2,
                            sticky="nsew")               
        


        # combo box intérêt
        self.cbo_interet = ctk.CTkOptionMenu(master=frm_interet,
                                    values=[

                                    "Programmation Python                     ",
                                    "Programmation PowerShell                 ",
                                    "Gestion du parc informatique interne     ", 
                                    "Maintenance des serveurs                 ", 
                                    "Maintien des postes de travail           ",
                                    "Maintien du réseau câblé et sans fil     ",
                                    "Maintien des autres périphériques        ",
                                    "Gestion des licences                     ",
                                    "Formation usagers                        ",
                                    "Gestion des accès à distance             ",
                                    "Gestion des accès usagers                ",
                                    "Gestion des anti-virus                   ",
                                    "Gestion des télécommunications           ",
                                    "Gestion des routeurs                     "], width=200)
        self.cbo_interet.grid( row=1, column=0,
                                    padx=20, pady=2,
                        sticky="nsew")

        # Résumé de l'application
        self.btn_resumer = ctk.CTkButton(master=frm_container,
                                        text="Résumé de l'application")
        self.btn_resumer.grid(row=3, column=0,
                                        columnspan=2, padx=20,
                                        pady=2, sticky="ew")

        # Text Box resume
        self.txt_resume = ctk.CTkTextbox(master=frm_container,
                                        width=200,
                                        height=100)
        self.txt_resume.grid(row=4, column=0,
                            columnspan=2, padx=5,
                            pady=2, sticky="nsew")


    # Voir ÉNONCÉ
    def resumer(self):
        pass

    # Voir ÉNONCÉ

    def creer_resume(self):
        pass

if __name__ == "__main__":
    app = App()
    # Used to run the application
    app.mainloop()    
