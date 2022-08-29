import pandas as pd
from collections import Counter


years = [2022, 2021, 2020, 2019, 2018]

for year in years:
    df = pd.read_csv(f"rawdata/{year}/survey_results_public.csv")
    
    if year in [2020, 2019, 2018]:
        df.rename(
            columns={
                'LanguageWorkedWith': 'LanguageHaveWorkedWith', 
                'LanguageDesireNextYear': 'LanguageWantToWorkWith'
                }, 
            inplace=True
            )
    elif year == 2017:
        df.rename(
            columns={
                'HaveWorkedLanguage': 'LanguageHaveWorkedWith', 
                'WantWorkLanguage': 'LanguageWantToWorkWith'
                }, 
            inplace=True
            )

    languages = []
    pairs = Counter()

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
    lang_mat.to_csv(f"data/{year}_lang_pairs.csv", encoding="utf-8")
