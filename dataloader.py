import pandas as pd
pd.set_option("display.precision", 6)


class DataLoader:
    """A class where we perform data processing (if necessary in the future)"""
    def __init__(self, data_root: str):
        self.loc = pd.read_csv(f"{data_root}/locations.csv")
        self.trips = pd.read_csv(f"{data_root}/trips.csv")
        self.loc["Latitude"] = self.loc["Latitude"].round(decimals=5)
        self.loc["Longitude"] = self.loc["Longitude"].round(decimals=5)

    def get_loc_data(self):
        return self.loc

    def get_trips_data(self):
        return self.trips