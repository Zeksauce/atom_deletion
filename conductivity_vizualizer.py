import pandas as pd
import plotly.express as px


class ConductivityDataReader:
    def __init__(self, degree: int):
        self.degree = degree
        self.filename = f"1.2.5 cutoff/{degree}/profile1.temp"
        self.data = pd.read_csv(
            self.filename,
            skiprows=4,
            delimiter=" ",
            header=None,
            names=["A", "B", "bin_number", "y_value", "num_atoms", "temperature"],
        )
        self.bin_data = self.data[self.data["bin_number"] < 101][
            ["bin_number", "y_value", "num_atoms", "temperature"]
        ]

    def get_bin_summary(self, bin_number: int) -> pd.DataFrame:
        return self.bin_data[self.bin_data["bin_number"] == bin_number].reset_index()[
            ["num_atoms", "temperature"]
        ]


class TempGrapher(ConductivityDataReader):
    def __init__(self, degree: int):
        super().__init__(degree)
        self.total_summary = self.get_total_summary()

    def get_bin_temp_summary(self, bin_number: int) -> pd.Series:
        return (
            self.bin_data[self.bin_data["bin_number"] == bin_number]
            .reset_index()["temperature"]
            .rename(f"bin_{bin_number}")
        )

    def get_total_summary(self) -> pd.DataFrame:
        total = pd.DataFrame(self.get_bin_temp_summary(1))
        for i in [25, 50, 75, 100]:
            bin_temp_series = self.get_bin_temp_summary(i)
            total = total.join(bin_temp_series, how="left")
        return total

    def plot_total_summary(self):  # Instance method now (no @staticmethod)
        """
        Instance method to plot the DataFrame output by get_total_summary() using Plotly.
        """
        fig = px.line(
            self.total_summary,  # Now using self.total_summary
            x=self.total_summary.index,
            y=self.total_summary.columns,
            labels={"index": "Time", "value": "Temperature", "variable": "Bins"},
            title=f"Temperature Series for Each Bin with degree {self.degree}",
        )

        fig.update_layout(
            legend_title="Bins",
            xaxis_title="Time",  # Changed to "Time" as x-axis label
            yaxis_title="Temperature",
        )
        fig.show()


class NumAtomsGrapher(ConductivityDataReader):
    def __init__(self, degree: int):
        super().__init__(degree)
        self.total_summary = self.get_total_summary()

    def get_bin_num_summary(self, bin_number: int) -> pd.Series:
        return (
            self.bin_data[self.bin_data["bin_number"] == bin_number]
            .reset_index()["num_atoms"]
            .rename(f"bin_{bin_number}")
        )

    def get_total_summary(self) -> pd.DataFrame:
        total = pd.DataFrame(self.get_bin_num_summary(1))
        for i in [25, 50, 75, 100]:
            bin_temp_series = self.get_bin_num_summary(i)
            total = total.join(bin_temp_series, how="left")
        return total

    def plot_total_summary(self):  # Instance method now (no @staticmethod)
        """
        Instance method to plot the DataFrame output by get_total_summary() using Plotly.
        """
        fig = px.line(
            self.total_summary,  # Now using self.total_summary
            x=self.total_summary.index,
            y=self.total_summary.columns,
            labels={"index": "Time", "value": "Number of Atoms", "variable": "Bins"},
            title=f"Number of Atoms Series for Each Bin with degree {self.degree}",
        )

        fig.update_layout(
            legend_title="Bins",
            xaxis_title="Time",  # Changed to "Time" as x-axis label
            yaxis_title="Number of Atoms",
        )
        fig.show()
