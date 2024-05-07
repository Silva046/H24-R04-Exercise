import customtkinter as ctk         #pip install customtkinter
import csv
import os
from PIL import ImageTk, Image      #pip install pillow


# https://customtkinter.tomschimansky.com/documentation/


# Apparence de la fenêtre 
ctk.set_appearance_mode('System')
ctk.set_default_color_theme('dark-blue')
# Dimensions de la fenêtre
ChoixWidth, ChoixHeight = 1100, 740

os.chdir(os.path.dirname(__file__))   # Pour se positionner dans le répertoire de ce script
image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")    # contient chemin vers les images



class appChoix(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.img_logo = ctk.CTkImage(Image.open(os.path.join(image_path,"assets", "logo.png")), size = (900, 120))

        self.dict_images = {} # va contenir une clef correspondant au nom d'une image et un valeur correspondant à cette image
        self._charger_images_programmes()

        # titre de la fenêtre
        self.title("Choix de programmes en ordre d'intérêt")
        self.geometry(f"{ChoixWidth}x{ChoixHeight}")
        self.grid_columnconfigure((0), weight=1)
        self.grid_columnconfigure((1), weight=4)
        # CTkLabel pour logo
        self.lbl_logo  = ctk.CTkLabel(self, image=self.img_logo, text="")
        self.lbl_logo.grid(row=0,column=0,columnspan=2, sticky="ew")
        
        ########  FRAME CHOIX CONTENU
        self.frm_contenu = ctk.CTkFrame( master=self, width=700 )
        self.frm_contenu.grid( row=1, column=0, padx=5, pady=0,columnspan=2,sticky="nsew")

        ########  FRAME DÉTAILS
        self.frm_details = ctk.CTkFrame(master=self.frm_contenu,width=800 )
        self.frm_details.grid( row=1, column=1, padx=0, pady=0)
        
            # CTkLabel pour les détails
        première_image = list(self.dict_images.keys())[0]
        self.lbl_details  = ctk.CTkLabel(master=self.frm_details, image=self.dict_images[première_image],text="")
        self.lbl_details.grid(row=0,column=0)
        
            # CTk.Entry pour le matricule
        self.matricule = ctk.CTkEntry(master=self, 
                                      placeholder_text="Entrez votre matricule",
                                      text_color='red')
        self.matricule.grid(row=3, column=0, columnspan=2, sticky="ew")
        
            # CTkButton enregistrer_choix_etudiant
        self.btn_enregistrer_choix = ctk.CTkButton(master=self, text="Enregistrer tes choix",
                                        width=300, height=25, command=self.enregistrer_choix)
        self.btn_enregistrer_choix.grid(row=4, column=0,columnspan=2, padx=5, pady=(5,5)) 
        
            # CTkLabel pour messages
        self.lbl_message = ctk.CTkLabel(self, text="Fais tes choix",
                                        width=200, height=25)
        self.lbl_message.grid(row=5, column=0,columnspan=2, padx=5,pady=(0,5))



        ########  FRAME CHOIX PROGRAMME
        self.frm_choix_programme = ctk.CTkFrame( master=self.frm_contenu, width=600 )
        self.frm_choix_programme.grid( row=1, column=0, padx=0, pady=0,sticky="ns")

            #CTkOptionMenu pour le choix de programmes
        self.choix_1 = ctk.CTkOptionMenu(master=self.frm_choix_programme,
                                        values=['PREMIER CHOIX']+list(self.dict_images.keys()),
                                        width=350, height=25, command=self.voir_details)

        self.choix_2 = ctk.CTkOptionMenu(master=self.frm_choix_programme, 
                                        values=['DEUXIÈME CHOIX']+list(self.dict_images.keys()),
                                        width=350, height=25, command=self.voir_details)

        self.choix_3 = ctk.CTkOptionMenu(master=self.frm_choix_programme,
                                        values=['TROISIÈME CHOIX']+list(self.dict_images.keys()),
                                        width=350, height=25, command=self.voir_details)
        
            # Placement des choix de programmes dans l'app
        self.choix_1.set(list(self.dict_images.keys())[0])
        self.choix_1.grid(row=0, column=0, padx=(0,0), pady=(0,5), sticky="e")
        self.choix_2.grid(row=1, column=0, padx=(0,0), pady=(0,5), sticky="e")
        self.choix_3.grid(row=2, column=0, padx=(0,0), pady=(0,5), sticky="e")
        


    # Charge toutes les images dans le dossier /images et les placent dans la variable self.dict_images
    # NOTE : Rien à faire ici.
    def _charger_images_programmes(self):
        for fichier_png in os.listdir(image_path) : 
            try :
                new_img = ctk.CTkImage(Image.open(os.path.join(image_path, fichier_png)), size = (700, 500))
                nom, ext = os.path.splitext(fichier_png)
                self.dict_images[nom] = new_img
            except : continue
         

    # Méthode exécuter lorsqu'on fait un choix dans les menus à options.
    # Elle doit recevoir le choix effectué en paramètre et changer l'image afficher à l'écran
    # NOTE : méthode à compléter.
    def voir_details(self, choix):
        print(f"{choix} à été choisi")
        nom_image = self.dict_images[choix]
        self.lbl_details.configure(image=nom_image)


    
    # Méthode appeler lorsqu'on clic sur le bouton btn_enregistrer_choix.
    # Valide les valeurs dans le formulaire et enregistre les choix dans un fichier texte
    # Ne prend pas de valeur en paramètre et ne retourne rin.
    # NOTE : cette méthode doit appeler les méthodes _valider_données_entré et _écrire_fichier_choix
    # NOTE : méthode à compléter.
    def enregistrer_choix(self) -> None:
        self._valider_données_entré()
        self._écrire_fichier_choix("choix_programmes_étudiants.csv")
    
    # Regarde les données contenue dans les menus à options (choix1, choix2, et choix3) NOTE : vous devez utilisez .get() pour obtenir leur valeur
    # change le texte dans lbl_message pour indiquer s'il y a des problèmes.
    def _valider_données_entré(self) -> bool: 
        # Tester que les trois menus à options contiènne des valeurs de choix de programme valide.
            # SI ce n'est pas le cas, affiche le message approprié : "Vous devez faire trois choix de programmes"
        if self.choix_1.get() == "PREMIER CHOIX" or self.choix_2.get() == "DEUXIÈME CHOIX" or self.choix_3 == "TROISIÈME CHOIX":
            self.lbl_message.configure(text="Vous devez faire trois choix de programmes")
        elif self.choix_1.get() == self.choix_2.get() or self.choix_1.get() == self.choix_3.get() or self.choix_2.get() == self.choix_3:
            self.lbl_message.configure(text="Vous devez choisir trois choix de programmes différents")
        elif self.matricule.get() == "":
            self.lbl_message.configure(text="Vous devez entrer votre matricule")
        else: self.lbl_message.configure(text="Les choix ont étés enregistrés")
        # Tester que les trois menus à options comportent des valeurs différentes
            # SI ce n'est pas le cas, affiche le message : "Vous devez choisir trois programmes différents"

        # Tester qu'une valeur à été entrer dans le boite d'entré de matricule, la valeur par défaut est un str vide : ""
            # SI ce n'est pas le cas, affiche le message : "Vous devez entrer votre matricule"

        # Si tout les tests sont réussi, affiche le message "Choix enregistrer."
        # Puis retourne True. Sinon cette méthode retourne False
        return True

    # Enregistre les données du questionnaire dans le fichier choix_programmes_étudiants.csv
    # Prend le nom du fichier dans lequel on veut enregister ces données en paramètre
    # NOTE : Cette méthode n'écrase pas les données déja existantes, elle ajoute une nouvelle ligne à la fin du fichier.
    def _écrire_fichier_choix(self,nom_fichier) -> None :
        fichier_exist = os.path.isfile(nom_fichier)
        with open(nom_fichier, "a", encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file,delimiter='|',lineterminator="\n")
            list_data = [self.matricule.get(), self.choix_1.get(), self.choix_2.get(), self.choix_3.get()]
            if fichier_exist == False:
                csv_writer.writerow(["matricule", "Choix 1", "Choix 2", "Choix 3"])
            csv_writer.writerow(list_data)

if __name__ == "__main__":
    choix = appChoix()
    choix.mainloop()    
