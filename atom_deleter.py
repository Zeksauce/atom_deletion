"""Module for deleting atoms from lammps data file with latparam"""

from pathlib import Path
import math
import pandas as pd


class AtomDeleter:
    """Class for making an atom deleter of a selected file"""

    def __init__(
        self,
        path=r"1.2.5 cutoff\1\SrTiO3_0.5_0.data",
        output=r"1.2.5 cutoff\1\SrTiO3_0.5_0.txt",
        degree=1,
        latparam=3.945,
    ):
        self.file = Path(path)
        self.output = Path(output)
        self.head = pd.read_csv(self.file, delimiter=" ", nrows=10)
        df = self.head
        insert_rows = [9, 6, 5, 2, 0]
        # Create an empty row as a DataFrame
        empty_row = pd.DataFrame([[None] * len(df.columns)], columns=df.columns)
        df = pd.concat([df, empty_row])
        for index_to_insert in insert_rows:
            # Split the DataFrame into two parts and concatenate with the empty row
            df = pd.concat(
                [df.iloc[:index_to_insert], empty_row, df.iloc[index_to_insert:]]
            ).reset_index(drop=True)
        self.head = df
        data = pd.read_csv(
            self.file, delimiter=" ", header=10, nrows=int(self.head.iloc[1, 0])
        ).reset_index()
        self.atom_data = data
        self.atom_data.columns = [
            "index",
            "Atom",
            "Charge",
            "x",
            "y",
            "z",
            "x_velocity",
            "y_veloctiy",
            "z_velocity",
        ]
        self.atom_data = self.atom_data.drop(columns=["index"])
        self.degree = degree
        self.latparam = latparam
        self.y_max = 145 ** (1 / 2) * latparam * 3
        self.y_shift = 1 / 2

    def main(self):
        """Main execution sequence"""
        self.remove_atom_range()
        self.shift_atoms()
        self.remove_atom_range_bottom()
        self.shift_atoms()
        self.save()

    def remove_atom_range(self):
        """Removes the range of atoms specified"""

        atom_data = self.atom_data
        self.atom_data = atom_data[
            ~(
                (
                    (
                        atom_data["y"]
                        > -(self.latparam / 2) * math.cos(self.degree * math.pi / 180)
                    )
                    & (atom_data["y"] < 0)
                )
            )
        ]

    def remove_atom_range_bottom(self):
        """Removes the range of atoms specified"""

        atom_data = self.atom_data
        self.atom_data = atom_data[
            ~(
                (
                    atom_data["y"]
                    < (self.latparam / 2) * math.cos(self.degree * math.pi / 180)
                )
                & (atom_data["y"] > 0)
            )
        ]

    def shift_atoms(self):
        atom_data = self.atom_data
        atom_data["y"] += self.y_max
        shift = self.y_max * self.y_shift * 2
        atom_data["y"] += shift
        atom_data["y"] %= self.y_max * 2
        atom_data["y"] -= self.y_max
        self.atom_data = atom_data
        self.y_shift = 1/4

    def save(self):
        """Modifies and formats back into a data file

        Args:
            name (regexp, optional): file to save to.
        """
        y = self.head.columns[0:9]
        b = self.atom_data.reset_index(drop=True)
        b.index = b.index + 1
        b = b.reset_index()
        b.columns = y
        self.head.iloc[1, 0] = len(self.atom_data)
        x = pd.concat(
            [self.head, b],
        )
        x.to_csv(self.output, sep=" ", index=False, header=True)


if __name__ == "__main__":
    deleter = AtomDeleter()
    deleter.main()
