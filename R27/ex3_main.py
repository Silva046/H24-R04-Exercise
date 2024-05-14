import classes
import classes.Ex3_Choix_pc as appChoix
from tkinter import messagebox

if __name__ == "__main__" :

    app = appChoix.appChoix("Construit ton PC !","Choisi tes composants")
    app.mainloop()