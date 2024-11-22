"""Module for changing the 1 degree angle"""

from pathlib import Path
import pandas as pd


class AtomDeleter:
    """Class for making an atom dleter of a selected file"""

    def __init__(
        self,
        path=r"1.2.5 cutoff\1\SrTiO3_0.5_0.data",
        output = r"1.2.5 cutoff\1\SrTiO3_0.5_0.txt",
        remove_areas=[
            (195.3, 1.9897, 1.9552, 0.25952),
            (473.5, 451.7, 1.96, 1.76),
            (420.162, 226.86, 1.96, 0.259),
        ],
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
        self.remove_areas = remove_areas

    def main(self):
        """Main execution sequence"""
        for x in self.remove_areas:
            self.remove_atom_range(*x)
        self.save()

    def remove_atom_range(self, x_max: float, x_min: float, y_max: float, y_min: float):
        """Removes the range of atoms specified

        Args:
            x_max (float): x max value
            x_min (float): x min value
            y_max (float): y max value
            y_min (float): y min value
        """

        atom_data = self.atom_data
        self.atom_data = atom_data[
            ~(
                (atom_data["x"] > x_min)
                & (atom_data["x"] < x_max)
                & (atom_data["y"] < y_max)
                & (atom_data["y"] > y_min)
            )
        ]

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
