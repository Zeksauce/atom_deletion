from pathlib import Path
import pandas as pd


class AtomDeleter:
    def __init__(self, path=r"1.2.5 cutoff\1\SrTiO3_0.5_0.data"):
        self.file = Path(path)
        self.data = pd.read_csv(self.file, delimiter=" ", header= False)

        # Extracting atom data (adjust ranges to your file structure)
        self.atom_data = self.data.iloc[
            10 : int(self.data.iloc[0, 0]) + 10, 0:9
        ].astype(float)
        self.atom_data.columns = [
            "index",
            "Atom",
            "Charge",
            "x",
            "y",
            "z",
            "x_velocity",
            "y_velocity",
            "z_velocity",
        ]
        self.atom_data.set_index("index", inplace=True)

        # Apply filter conditions
        self.new = self.atom_data[
            ~(
                (self.atom_data["x"] > 1.9897)
                & (self.atom_data["x"] < 195.28)
                & (self.atom_data["y"] < 1.9551)
                & (self.atom_data["y"] > 0.25952)
            )
        ]

        # Extract the unchanged header lines
        header_lines = self.data.iloc[:10]

        # Concatenate header with the updated atom_data
        self.updated_data = pd.concat([header_lines, self.atom_data], ignore_index=False)

    def save(self):
        """Save to a new file"""
        self.updated_data.to_csv(
            r"1.2.5 cutoff\1\SrTiO3_0.5_00.data", sep=" ", index=False, header=False
        )


if __name__ == "__main__":
    deleter = AtomDeleter()
    deleter.save()
