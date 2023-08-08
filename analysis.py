"""

"""
from general_functions import get_data, get_dataframe
from os import environ

# TODO: get_data() and tidy
user = environ.get('USER')
pw = environ.get('PW')
# "Lebensbedingungen"
data_str_rows = get_data(name="99911-0011", user=user, pw=pw)
life1 = data_str_rows[3].split(';')[0].strip()  # topics
life2 = data_str_rows[2].split(';')[0].split(',')[0].strip()  # countries
life3 = data_str_rows[2].split(';')[0].split(',')[1].strip()  # years
life3_val_str = data_str_rows[4].split(';')[3:]  # years-str
life3_val_int = [int(leb_str) for leb_str in life3_val_str]  # years-int
