import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def to_float(val_str):
    if val_str.isnumeric():
        return float(val_str)
    elif val_str.replace(',', '').isnumeric():
        return float(val_str.replace(',', '.'))
    else:
        return np.nan
