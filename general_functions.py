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


# MAKE TIDY AND GET DATAFRAME
def get_dataframe(topics, countries, years, input_data):
    collect = {topics: [], countries: []}
    for year in years:
        collect[year] = []


    for i, row in enumerate (input_data):
        split_row = row.split(';')
        collect[topics].append(split_row[1] + ' [' + split_row[2] + ']')
        collect[countries].append(split_row[0])

        for j, year in enumerate(years):
            collect[year].append(to_float(split_row[3+j]))

    df1 = pd.DataFrame(collect)
    df2 = df1.set_index([topics, countries])
    topics_vals = df1[topics].unique()  # get all unique "Topics"
    countries_vals = df1[countries].unique()  # get all unique "Countries"
    return df1, df2, topics_vals, countries_vals




# GET THE MAX VALUES
def get_topic_max_val(topics, years, data):
    max = []
    for year in years:
        max.append(np.max(data[year][topics, :]))
    max = np.array(max)
    return max



def get_plot(topics, countries, years, data):
    x = years  # "Years" ax x-axis
    for topic in topics:
        fig, ax = plt.subplots()
        fig.suptitle(topic)
        for country in countries:
            y = data.loc[topic, country].tolist()  # get the values for the y-axis
            ax.plot(x, y)
        ax.set_xlabel('year')
        ax.set_ylabel(topic)
        ax.legend(countries)
        ax.grid(linestyle=':')