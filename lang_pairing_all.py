import pandas as pd
from collections import Counter


df2022 = pd.read_csv("rawdata/2022/survey_results_public.csv")
df2021 = pd.read_csv("rawdata/2021/survey_results_public.csv")
df2020 = pd.read_csv("rawdata/2020/survey_results_public.csv")
df2019 = pd.read_csv("rawdata/2019/survey_results_public.csv")
df2018 = pd.read_csv("rawdata/2018/survey_results_public.csv")
df2017 = pd.read_csv("rawdata/2017/survey_results_public.csv")

for d in [df2020, df2019, df2018]:
    d.rename(
        columns={
            'LanguageWorkedWith': 'LanguageHaveWorkedWith', 
            'LanguageDesireNextYear': 'LanguageWantToWorkWith'
            }, 
        inplace=True
        )

df_all = [df2022, df2021, df2020, df2019, df2018]

languages = []
pairs = Counter()

for df in df_all:
    for row in df.itertuples():
        if type(row.LanguageHaveWorkedWith) is str:
            langs = row.LanguageHaveWorkedWith.split(';')
            for l1 in langs:
                if l1 not in languages:
                    languages.append(l1)
                for l2 in langs:
                    if l1 != l2:
                        ix = f'{l1} , {l2}'
                        pairs.update([ix])

#big_lang_pairs = [(k, v) for k, v in pairs.items() if v > 10000]

lang_mat = pd.DataFrame(columns=sorted(languages), index=sorted(languages))

for lp in pairs:
    l1, l2 = lp.split(",")
    l1 = l1.strip()
    l2 = l2.strip()
    lang_mat[l1.strip()][l2.strip()] = pairs[f'{l1} , {l2}']

for lang in languages:
    lang_mat[lang][lang] = -1

lang_mat.fillna(0, inplace=True)

# Save the dataframe to a csv
lang_mat.to_csv("data/lang_pairs.csv", encoding="utf-8")
