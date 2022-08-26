import pandas as pd
import os
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
import matplotlib.pyplot as plt

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
'''sjutton_path = pd.read_csv(CURR_DIR_PATH + "/survey_results_public_2017.csv")
arton_path = pd.read_csv(CURR_DIR_PATH + "/survey_results_public_2018.csv")
nitton_path = pd.read_csv(CURR_DIR_PATH + "/survey_results_public_2019.csv")
tjugo_path = pd.read_csv(CURR_DIR_PATH + "/survey_results_public_2020.csv")
tjugoett_path = pd.read_csv(CURR_DIR_PATH + "/survey_results_public_2021.csv")'''
tjugotva_path = pd.read_csv(CURR_DIR_PATH + "/survey_results_public_2022.csv", index_col=False, header = 0)
data_dir = CURR_DIR_PATH + "/Data"
'''df_sjutton = pd.DataFrame(sjutton_path)
df_arton = pd.DataFrame(arton_path)
df_nitton = pd.DataFrame(nitton_path)
df_tjugo = pd.DataFrame(tjugo_path)
df_tjugoett = pd.DataFrame(tjugoett_path)'''
df_tjugotva = pd.DataFrame(tjugotva_path)
 #Funkar. Array av tf för onboarding suport
onb_22 = df_tjugotva[['TrueFalse_1']].dropna()
onb_22.replace({"Yes":"1", "No":"0"}, inplace = True)
#onb_22 = np.array(onb_22[['TrueFalse_1']])
#print(onb_22)
#Funkar 
wex_22 = df_tjugotva[['WorkExp']].dropna()
#wex_22 = np.array(wex_22[['WorkExp']])
#print(type(wex_22))

#Algoritm
#length = 10
x = wex_22.WorkExp.values
y = onb_22.TrueFalse_1.values
#x = x.reshape(length, 1)
#y = y.reshape(length, 1)

regr = linear_model.LinearRegression()
regr.fit(x, y)

plt.scatter(x, y,  color='black')
plt.plot(x, regr.predict(x), color='blue', linewidth=3)
plt.xticks(())
plt.yticks(())
plt.show()
#print(regr.coef_) 
