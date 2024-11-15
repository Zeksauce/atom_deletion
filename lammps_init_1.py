from pathlib import Path
import pandas as pd

class AtomDeleter:
    def __init__(self, path= r"C:\Users\zek\Desktop\fiels\1.2.5 cutoff/2/SrTiO3_1_0.data"):
        file = Path(path)
        data = pd.read_csv(file, delimiter=" ")
        atom_data = data.iloc[10:int(data.iloc[0,0]) + 10,0:9]
        atom_data.columns = ["index", "Atom", "Charge", "x", "y", "z","x_velocity","y_veloctiy", "z_velocity"]
        atom_data.set_index("index", inplace=True)