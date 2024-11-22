"""
UTILITIES
Author: Michael Kohlegger
Date: November 2024
"""


from datetime import datetime as dt


def time_decorator(function):
    def wrapper(*args, **kwargs):
        start = dt.now()
        result = function(*args, **kwargs)
        duration = dt.now()-start
        print("┌───────────────────────────────────────┐")
        print(f"│ Run-Duration {duration}                  │")
        print("└───────────────────────────────────────┘")
        return result
    return wrapper
