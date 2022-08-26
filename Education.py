import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
'''sjutton_path = pd.read_csv(CURR_DIR_PATH + "/survey_results_public_2017.csv")
arton_path = pd.read_csv(CURR_DIR_PATH + "/survey_results_public_2018.csv")
nitton_path = pd.read_csv(CURR_DIR_PATH + "/survey_results_public_2019.csv")
tjugo_path = pd.read_csv(CURR_DIR_PATH + "/survey_results_public_2020.csv")
tjugoett_path = pd.read_csv(CURR_DIR_PATH + "/survey_results_public_2021.csv")'''
tjugotva_path = pd.read_csv(CURR_DIR_PATH + "/survey_results_public_2022.csv")

data_dir = CURR_DIR_PATH + "/Data"
'''df_sjutton = pd.DataFrame(sjutton_path)
df_arton = pd.DataFrame(arton_path)
df_nitton = pd.DataFrame(nitton_path)
df_tjugo = pd.DataFrame(tjugo_path)
df_tjugoett = pd.DataFrame(tjugoett_path)'''
df_tjugotva = pd.DataFrame(tjugotva_path)

#Plockar ut de som hjälpt nyanställda
good_peepz = df_tjugotva.loc[df_tjugotva['TrueFalse_1']=='Yes']
#print(len(df_tjugotva))
#procent som hjälpt av de som svarat
#hjalpsam_procent = ((len(good_peepz))/(len(df_tjugotva)))*100
#print(hjalpsam_procent)

#Visualisering pyplot  cirkeldiagram de som hjälpt och de som inte hjälpt
labels = 'Helped new hirings', 'Havent helped new hirings'
sizes = [len(good_peepz), len(df_tjugotva)-len(good_peepz)]
explode = (0.1, 0)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal') 
plt.show()

#Plockar ut de som hjälpt nyanställd till ny csv
#good_peepz.to_csv(data_dir + "hjalpsam_2022")
