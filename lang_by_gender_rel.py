import pandas as pd
from collections import Counter
import plotly.express as px
from plotly import graph_objects as go

years = [2022, 2021, 2020, 2019]

num_pops = 10

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
        gen = str(row.Gender)
        if gen in ["Man", "Woman"]:
            gender = gen
        else:
            gender = "Other"
        gender_langs.setdefault(gender, {
                    'total': 0,
                    'language_counter': Counter()
                })
        languages = str(row.LanguageHaveWorkedWith).split(";")
        gender_langs[gender]['language_counter'].update(languages)
        gender_langs[gender]['total'] += 1
    
    langs_by_gender = []
    row_names = []
    pop_langs = set()

    # Find the num_pop most popular languages for all groups
    for gen in gender_langs.keys():
        pop_langs.update({l[0] for l in gender_langs[gen]["language_counter"].most_common(num_pops) if l[0] != 'nan'})

    for gen, info in gender_langs.items():
        tot = info['total']
        langs_used = {'Gender': gen, 'Total': tot}
        row_names.append(gen)
        all_used = gender_langs[gen]['language_counter']
        for lang in all_used:
            if lang in pop_langs:
                langs_used[lang] = int(all_used[lang])
            else:
                langs_used["Other_langs"] = langs_used.get("Other_langs", 0) + int(all_used[lang])
        
        langs_by_gender.append(langs_used)

    df_new = pd.DataFrame(langs_by_gender)

    for i in range(len(df_new)):
        sum_tot = sum(df_new.iloc[i, 1:])
        df_new.iloc[i, 1:] = df_new.iloc[i, 1:] * 100 / sum_tot

    # Make index from the first column
    df_new.set_index('Gender', inplace=True)

    # Save the dataframe to a csv
    df_new.to_csv(f"data/{year}_langsrelative_by_gender.csv", encoding="utf-8")

    #print(df_new)

    # fig1 = px.bar(df_new, x=df_new.index, y=df_new.columns[1:], barmode='group')

    # fig1.show()
    
    fig = go.Figure(
        data=[
            go.Bar(
                name="Men", 
                x=df_new.columns[1:], 
                y=df_new.iloc[1, 1:], 
                offsetgroup=0
                ), 
            go.Bar(
                name="Women", 
                x=df_new.columns[1:], 
                y=df_new.iloc[2, 1:], 
                offsetgroup=1
                ), 
            go.Bar(
                name="Other", 
                x=df_new.columns[1:], 
                y=df_new.iloc[0, 1:], 
                offsetgroup=2)
            ], 
        layout=go.Layout(
            title=f"Lang by Gender {year}", 
            yaxis_title="Percentage"
            )
        )
    
    fig.show()
    
    fig.write_image(f"images/{year}_most_popular_by_gen.png")
