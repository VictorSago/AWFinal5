import pandas as pd
import os
CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))


data  = pd.read_csv(CURR_DIR_PATH + "/rawdata/2022/""survey_results_public.csv")
data2 = pd.read_csv(CURR_DIR_PATH + "/rawdata/2021/""survey_results_public.csv")
data3 = pd.read_csv(CURR_DIR_PATH + "/rawdata/2020/"'survey_results_public.csv')
data4 = pd.read_csv(CURR_DIR_PATH + "/rawdata/2019/"'survey_results_public.csv')
data5 = pd.read_csv(CURR_DIR_PATH + "/rawdata/2018/"'survey_results_public.csv')
data6 = pd.read_csv(CURR_DIR_PATH + "/rawdata/2017/"'survey_results_public.csv')

df  = pd.DataFrame(data)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3)
df4 = pd.DataFrame(data4)
df5 = pd.DataFrame(data5)
df6 = pd.DataFrame(data6)
#print(df.head(20))

cou_lan_22= df [['Country', 'LanguageHaveWorkedWith']].dropna()    #HaveWorkedLanguage    #LanguageWorkedWith
cou_lan_21= df2[['Country', 'LanguageHaveWorkedWith']].dropna()
cou_lan_20= df3[['Country', 'LanguageWorkedWith']].dropna() 
cou_lan_19= df4[['Country', 'LanguageWorkedWith']].dropna() 
cou_lan_18= df5[['Country', 'LanguageWorkedWith']].dropna() 
cou_lan_17= df6[['Country', 'HaveWorkedLanguage']].dropna() 

cou_lan_20.rename(columns={"LanguageWorkedWith":"LanguageHaveWorkedWith"}, inplace=True)
cou_lan_19.rename(columns={"LanguageWorkedWith":"LanguageHaveWorkedWith"}, inplace=True)
cou_lan_18.rename(columns={"LanguageWorkedWith":"LanguageHaveWorkedWith"}, inplace=True)
cou_lan_17.rename(columns={"HaveWorkedLanguage":"LanguageHaveWorkedWith"}, inplace=True)

#print(cou_lan_17)
#print(cou_lan_18)
#print(cou_lan_20)
#print(cou_lan_19)
#print(cou_lan_21)
#print(cou_lan_22)