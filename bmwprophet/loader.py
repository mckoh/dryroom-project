"""
LOADER CLASS FOR BMW PROJECT
Author: Michael Kohlegger
Date: November 2024
"""


from os.path import isfile, join, exists
from pandas import DataFrame, read_csv
from .preprocessing import key_value_mapper


USE_COLUMNS = [
    "trigger_ts_utc",
    "measured_value",
    "data_key_val_string"
]


class Loader:
    """Loader class lets you import the data for further analysis"""

    def __init__(self):
        self._data = None

    def load_data(self, path:str, file:str) -> None:
        full_path = join(path, file)
        data = read_csv(full_path, parse_dates=[0, 1, 7])

        self._data = data[USE_COLUMNS].copy()

        column = data["data_key_val_string"]
        column_new = column.map(key_value_mapper)

        self._data.loc[:,"ns"], \
            self._data.loc[:,"machine"], \
            self._data.loc[:,"errection_location"], \
            self._data.loc[:,"installation_location"], \
            self._data.loc[:,"components"], \
            self._data.loc[:,"sensor_type"] = zip(*column_new)

        self._data.drop("data_key_val_string", axis=1, inplace=True)

    def print_column_info(self):
        for column in self._data.columns:
            unique_values =  len(self._data[column].value_counts())
            flag = "!" if unique_values == 1 else " "
            print(f"[{flag}]: Column '{column}' has {unique_values} unique values")

    def save_data(self, path:str, file:str) -> None:
        full_path = join(path, file)
        self._data.to_csv(full_path)

    def split_data(self):
        pass

    def get_data(self, split=False, window=0, shift=0):
        if not split:
            return self._data