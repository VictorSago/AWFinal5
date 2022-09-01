import pandas as pd
from collections import Counter


years = [2022, 2021, 2020, 2019]

for year in years:
    df = pd.read_csv(f"rawdata/{year}/survey_results_public.csv", dtype=str)

    if year in [2020, 2019]:
        df.rename(
            columns={
                'LanguageWorkedWith': 'LanguageHaveWorkedWith', 
                'LanguageDesireNextYear': 'LanguageWantToWorkWith'
                }, 
            inplace=True
            )

    gender_langs = {}

    for row in df.itertuples():
        gender = str(row.Gender)
        if gender in ["Man", "Woman"]:
            gender_langs.setdefault(gender, {
                    'total': 0,
                    'language_counter': Counter()
                })

            languages = str(row.LanguageHaveWorkedWith).split(";")
            gender_langs[gender]['language_counter'].update(languages)
            gender_langs[gender]['total'] += 1

    langs_by_gender = []
    row_names = []

    for gen, info in gender_langs.items():
        tot = info['total']
        langs_used = {'Gender': gen, 'Total': tot}
        row_names.append(gen)
        all_used = gender_langs[gen]['language_counter']
        for lang in all_used:
            langs_used[lang] = int(all_used[lang])
        
        langs_by_gender.append(langs_used)

    df_new = pd.DataFrame(langs_by_gender)

    # Replace all N/A with 0s
    df_new.fillna(0, inplace=True)

    # Make index from the first column
    df_new.set_index('Gender', inplace=True)

    # Save the dataframe to a csv
    df_new.to_csv(f"data/{year}_langs_by_gender.csv", encoding="utf-8")

    #print(df_new)
