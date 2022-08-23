import os
import pandas as pd
from glob import glob

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
sjutton_path = CURR_DIR_PATH + "/sjutton.csv"
arton_path = CURR_DIR_PATH + "/arton.csv"
nitton_path = CURR_DIR_PATH + "/nitton.csv"
tjugo_path = CURR_DIR_PATH + "/tjugo.csv"
tjugoett_path = CURR_DIR_PATH + "/tjugoett.csv"
tjugotva_path = CURR_DIR_PATH + "/tjugotva.csv"
#hanterad22 = CURR_DIR_PATH + "/hanterad_22.csv"

'''data17 = pd.read_csv(sjutton_path)
data18 = pd.read_csv(arton_path)
data19 = pd.read_csv(nitton_path)
data20 = pd.read_csv(tjugo_path)
data21 = pd.read_csv(tjugoett_path)
data22 = pd.read_csv(tjugotva_path)'''
#print(sjutton.head())
'''#data_dir = CURR_DIR_PATH + "/Projekt/"
df_sjutton = pd.DataFrame(data17)
df_arton = pd.DataFrame(data18)
df_nitton = pd.DataFrame(data19)
df_tjugo = pd.DataFrame(data20)
df_tjugoett = pd.DataFrame(data21)
df_tjugotva = pd.DataFrame(data22)
print(df_sjutton.head())'''

q_os_22 = df_tjugotva[['ResponseId', 'YearsCode', 'YearsCodePro', 'DevType', 'LanguageHaveWorkedWith', 'OpSysProfessional use']].dropna()#, 'OpSysPersonal use'
q_os_21 = df_tjugoett[['Respondent', 'YearsCode', 'YearsCodePro', 'DevType', 'LanguageHaveWorkedWith', 'OpSys']].dropna()
q_os_20 = df_tjugo[['Respondent', 'YearsCode', 'YearsCodePro', 'DevType', 'LanguageWorkedWith', 'OpSys']].dropna()
q_os_19 = df_nitton[['Respondent', 'YearsCode', 'YearsCodePro', 'DevType', 'LanguageWorkedWith', 'OpSys']].dropna()
q_os_18 = df_arton[['Respondent', 'YearsCoding', 'YearsCodingProf', 'DevType', 'LanguageWorkedWith', 'OperatingSystem']].dropna()
q_os_17 = df_sjutton[['Respondent', 'YearsCodedJob', 'YearsCodedJobPast', 'DeveloperType', 'HaveWorkedLanguage']].dropna()
#Sjutton  har dessa: DeveloperType,WebDeveloperType,MobileDeveloperType,NonDeveloperType. OS Saknas för 17. Koderfarenhet olika. 


q_os_21.rename(columns={"Respondent":"ResponseId", "OpSys":"OpSysProfessional use"}, inplace=True)
q_os_20.rename(columns={"Respondent":"ResponseId", "LanguageWorkedWith": "LanguageHaveWorkedWith", "OpSys":"OpSysProfessional use"}, inplace=True)
q_os_19.rename(columns={"Respondent":"ResponseId", "LanguageWorkedWith": "LanguageHaveWorkedWith", "OpSys":"OpSysProfessional use"}, inplace=True)
q_os_18.rename(columns={"Respondent":"ResponseId", "YearsCoding" : "YearsCode", "YearsCodingProf": "YearsCodePro", "LanguageWorkedWith": "LanguageHaveWorkedWith", "OperatingSystem":"OpSysProfessional use"}, inplace=True)
q_os_17.rename(columns={"Respondent":"ResponseId", "YearsCodedJob":"YearsCode", "YearsCodedJobPast":"YearsCodedPro", "DeveloperType":"DevType", "HaveWorkedLanguage": "LanguageHaveWorkedWith", "OpSys":"OpSysProfessional use"}, inplace=True)

'''def load_dfs_from(glob_path):
        subject_data = []
        file_paths = glob(glob_path)

        for path in file_paths:
                df = pd.read_csv(path)
                subject_data.append(df)
        return subject_data, file_paths'''




