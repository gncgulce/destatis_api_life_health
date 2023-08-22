"""
"""
from general_functions import get_data, get_dataframe, get_topic_max_val, get_one_topic_and_country, get_normalized
from os import environ
import matplotlib.pyplot as plt
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
# TODO: get_one_topic_and_country
# "Lebensbedingungen"
countries = ['Deutschland', 'Irland', 'Türkei']
bruttos_country = {}
for country in countries:
    bruttos_country[country] = get_one_topic_and_country(topics='Bruttonationaleinkommen je Einwohner,Atlas-Methode [US $]',
                                                         country=country, data=df2)
houses_country = {}
for country in countries:
    houses_country[country] = get_one_topic_and_country(topics='Ausgabenanteil priv. Haushalte für Wohnung [Prozent]',
                                                        country=country, data=df2)
foods_country = {}
for country in countries:
    foods_country[country] = get_one_topic_and_country(topics='Ausgabenanteil priv. Haushalte für Nahrungsmittel [Prozent]',
                                                       country=country, data=df2)
# "Gesundheit"
doctors_country = {}
for country in countries:
    doctors_country[country] = get_one_topic_and_country(topics='Ärztedichte je 10 000 Einwohner [Anzahl]',
                                                         country=country, data=df_2)
beds_country = {}
for country in countries:
    beds_country[country] = get_one_topic_and_country(topics='Krankenhausbetten je 10 000 Einwohner [Anzahl]',
                                                      country=country, data=df_2)
deaths_country = {}
for country in countries:
    deaths_country[country] = get_one_topic_and_country(topics='Gestorbene Säuglinge je 1000 Lebendgeborene [Anzahl]',
                                                        country=country, data=df_2)
# TODO: get_normalized
# "Lebensbedingungen"
bruttos_normal = {}
for country in countries:
    bruttos_normal[country] = get_normalized(tc=bruttos_country[country], max=bruttos_max)
houses_normal = {}
for country in countries:
    houses_normal[country] = get_normalized(tc=houses_country[country], max=houses_max)
foods_normal = {}
for country in countries:
    foods_normal[country] = get_normalized(tc=foods_country[country], max=foods_max)
# "Gesundheit"
doctors_normal = {}
for country in countries:
    doctors_normal[country] = get_normalized(tc=doctors_country[country], max=doctors_max)
beds_normal = {}
for country in countries:
    beds_normal[country] = get_normalized(tc=beds_country[country], max=beds_max)
deaths_normal = {}
for country in countries:
    deaths_normal[country] = get_normalized(tc=deaths_country[country], max=deaths_max)
# TODO: get KPI
# "Lebensbedingungen"
# kpi_life = (bruttos_normal - houses_normal - foods_normal) (len=32)
kpi_life_de = (bruttos_normal['Deutschland'] - houses_normal['Deutschland'] - foods_normal['Deutschland'])
kpi_life_ir = (bruttos_normal['Irland'] - houses_normal['Irland'] - foods_normal['Irland'])
kpi_life_tr = (bruttos_normal['Türkei'] - houses_normal['Türkei'] - foods_normal['Türkei'])
# "Gesundheit"
# kpi_health = (doctors_normal + beds_normal - deaths_normal) (len=31)
kpi_health_de = (doctors_normal['Deutschland'] + beds_normal['Deutschland'] - deaths_normal['Deutschland'])
kpi_health_ir = (doctors_normal['Irland'] + beds_normal['Irland'] - deaths_normal['Irland'])
kpi_health_tr = (doctors_normal['Türkei'] + beds_normal['Türkei'] - deaths_normal['Türkei'])
# TODO: get_plot()

plt.figure(figsize=plt.figaspect(0.4))
plt.subplot(1, 2, 1)
plt.plot(life3_val_int, kpi_life_de, color='red')
plt.plot(life3_val_int, kpi_life_ir, color='green')
plt.plot(life3_val_int, kpi_life_tr, color='blue')
plt.xlabel("Years")
plt.ylabel("Figure of merit [a.u.]")
plt.legend(['Germany', 'Ireland', 'Turkey'])
plt.title('Life')
plt.grid(linestyle="--")

plt.subplot(1, 2, 2)
plt.plot(health3_val_int, kpi_health_de, color='red')
plt.plot(health3_val_int, kpi_health_ir, color='green')
plt.plot(health3_val_int, kpi_health_tr, color='blue')
plt.xlabel("Years")
plt.ylabel("Figure of merit [a.u.]")
plt.legend(['Germany', 'Ireland', 'Turkey'])
plt.title('Health')
plt.grid(linestyle="--")

plt.tight_layout()
plt.show()
