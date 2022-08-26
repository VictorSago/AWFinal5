import pandas as pd
from collections import Counter


df = pd.read_csv("rawdata/2022/survey_results_public.csv", dtype=str)

dev_langs = {}

for row in df.itertuples():
    if type(row.DevType) is str:
        dev_types = row.DevType.split(';')

        for dev_type in dev_types:
            dev_langs.setdefault(dev_type, {
                'total': 0,
                'language_counter': Counter()
            })

            languages = str(row.LanguageHaveWorkedWith).split(";")
            dev_langs[dev_type]['language_counter'].update(languages)
            dev_langs[dev_type]['total'] += 1

langs_by_dev = []
row_names = []

for dev, info in dev_langs.items():
    print(dev)
    tot = info['total']
    langs_used = {'DevType': dev, 'Total': tot}
    row_names.append(dev)
    all_used = dev_langs[dev]['language_counter']
    for lang in all_used:
        langs_used[lang] = int(all_used[lang])
    
    langs_by_dev.append(langs_used)

df_new = pd.DataFrame(langs_by_dev)

# Replace all N/A with 0s
df_new.fillna(0, inplace=True)

# Make index from the first column
df_new.set_index('DevType', inplace=True)

# Save the dataframe to a csv
df_new.to_csv('data/langs_by_devtype.csv', encoding='utf-8')

#print(df_new)
