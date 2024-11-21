"""
HELPER FUNCTIONS FOR DATA PREPROCESSING
Author: Michael Kohlegger
Date: November 2024
"""


def key_value_mapper(row:str) -> tuple:
    """Mapper function that deals with the key-value-column of the data

    This function splits the key-value column of the input data into
    separate values. It returns the values in a complete tuple. As some
    rows of the data do not contain all value elements, the function has two
    different returns, depending on the row.

    Values in the returned tuple are:
    - NS
    - Machine
    - Errection location
    - Installation location
    - Components
    - Sensor type

    Args:
        row (str): The rows input coming from the mapper function

    Returns:
        Tuple of values (tuple)
    """

    first = int(row.split(";")[0].split("=")[1])
    second = row.split(";")[1].split("s=")[1].replace('"', "").split(".")

    try:
        return (first, second[3], second[5], second[7], second[9], second[11])

    except:
        return (first, second[3], None, None, None, "DataPublishTrigger")

