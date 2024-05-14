import classes
import classes.Ex1_Thermostat as Thermo
from tkinter import messagebox

if __name__ == "__main__" :
    th1 = Thermo.Thermostat()
    th2 = Thermo.Thermostat()

    th1.temperature = 32
    for i in range(5) : th2.diminuer_1_degre()

    messagebox.showinfo("Thermostats",f"La température du thermostat 1 est : {th1.temperature}\nLa température du thermostat 2 est : {th2.temperature}")
