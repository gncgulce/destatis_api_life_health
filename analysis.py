"""

"""
from general_functions import get_data, get_dataframe, get_topic_max_val
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
# "Gesundheit"

data_str_rows2 = get_data(name="99911-0005", user=user, pw=pw)
health1 = data_str_rows2[2].split(';')[0].strip()  # topics
health2 = data_str_rows2[1].split(':')[1].split(',')[0].strip()  # countries
health3 = data_str_rows2[1].split(':')[1].split(',')[1].strip(';').strip()  # years
health3_val_str = data_str_rows2[3].split(';')[3:]  # years-str
health3_val_int = [int(ges_str) for ges_str in health3_val_str]  # years-int



# TODO: get_dataframe()

df1, df2, topics_unique1, countries_unique1 = get_dataframe(topics=life1, countries=life2, years=life3_val_int,
                                                            input_data=data_str_rows[5:-11])

df_1, df_2, topics_unique2, countries_unique2 = get_dataframe(topics=health1, countries=health2, years=health3_val_int,
                                                              input_data=data_str_rows2[4:-12])



# TODO: get_topic_max_val


# "Lebensbedingungen"

bruttos_max = get_topic_max_val(topics='Bruttonationaleinkommen je Einwohner,Atlas-Methode [US $]',
                                years=life3_val_int, data=df2)
houses_max = get_topic_max_val(topics='Ausgabenanteil priv. Haushalte für Wohnung [Prozent]',
                               years=life3_val_int, data=df2)
foods_max = get_topic_max_val(topics='Ausgabenanteil priv. Haushalte für Nahrungsmittel [Prozent]',
                              years=life3_val_int, data=df2)
# "Gesundheit"


doctors_max = get_topic_max_val(topics='Ärztedichte je 10 000 Einwohner [Anzahl]',
                                years=health3_val_int, data=df_2)
beds_max = get_topic_max_val(topics='Krankenhausbetten je 10 000 Einwohner [Anzahl]',
                             years=health3_val_int, data=df_2)
deaths_max = get_topic_max_val(topics='Gestorbene Säuglinge je 1000 Lebendgeborene [Anzahl]',
                               years=health3_val_int, data=df_2)