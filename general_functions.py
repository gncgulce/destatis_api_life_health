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





#LOGIN AND GET DATA
def get_data(name: str, user: str, pw: str):
    area = "all"  # "all"
    startyear= "1970"
    response = requests.get("https://www-genesis.destatis.de/genesisWS/rest/2020/data/table?" +
                                 "username=" + user +
                                 "&password=" + pw +
                                 "&name=" + name +
                                 "&area=" + area +
                                 "&compress=false" +
                                 "&transpose=false" +
                                 "&startyear=" + startyear +
                                 "&endyear=" +
                                 "&timeslices=" +
                                 "&regionalvariable=" +
                                 "&regionalkey=" +
                                 "&classifyingvariable1=" +
                                 "&classifyingkey1=" +
                                 "&classifyingvariable2=" +
                                 "&classifyingkey2=" +
                                 "&classifyingvariable3=" +
                                 "&classifyingkey3=" +
                                 "&job=false" +
                                 "&stand=01.01.1970" +
                                 "&language=de")
    data = response.json()
    data_str = data['Object']['Content']
    data_str_rows = data_str.split('\n')
    return data_str_rows

