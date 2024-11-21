from pathlib import Path
import pandas as pd


class AtomDeleter:
    def __init__(self, path=r"C:1.2.5 cutoff\1\SrTiO3_0.5_0.data"):
        self.file = Path(path)
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

    def main(self):
        self.remove_atom()
        self.save()

    def remove_atom(self):
        atom_data = self.atom_data
        self.atom_data = atom_data[
            ~(
                (atom_data["x"] > 1.9897)
                & (atom_data["x"] < 195.3)
                & (atom_data["y"] < 1.9552)
                & (atom_data["y"] > 0.25952)
            )
        ]

    def save(self, name=r"1.2.5 cutoff\1\SrTiO3_0.5_000.data"):
        y = self.head.columns[0:9]
        b = self.atom_data.reset_index(drop=True)
        b.index = b.index + 1
        b = b.reset_index()
        b.columns = y
        self.head.iloc[1, 0] = len(self.atom_data)
        x = pd.concat(
            [self.head, b],
        )
        x.to_csv(name, sep=" ", index=False, header=True)


if __name__ == "__main__":
    deleter = AtomDeleter()
    deleter.main()
