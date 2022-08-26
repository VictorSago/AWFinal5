import pandas as pd
from collections import Counter


df2022 = pd.read_csv("rawdata/2022/survey_results_public.csv", dtype=str)

# Create a dictionary the counter of all the 
# used and wanted languages for each country
langs_by_country = {}

# For each available answer count the total answers for that country and
# the used and wanted languages
for row in df2022.itertuples():
    # Check that the entry for Country is present
    if type(row.Country) is str:
        langs_by_country.setdefault(str(row.Country), {
            'total': 0,
            'lang_used': Counter(),
            'lang_wanted': Counter()
        })
        langs_used = str(row.LanguageHaveWorkedWith).split(";")
        langs_wanted = str(row.LanguageWantToWorkWith).split(";")
        langs_by_country[row.Country]['total'] += 1
        langs_by_country[row.Country]['lang_used'].update(langs_used)
        langs_by_country[row.Country]['lang_wanted'].update(langs_wanted)

# Sort the dict by country name
#sorted_by_country = {k: langs_by_country[k] for k in sorted(langs_by_country.keys())}

# Reformat the previously created dict to a form suitable 
# to be converted into a dataframe
all_langs_used = []

for country in langs_by_country:
    tot = langs_by_country[country]['total']
    langs_used = {'name': country, 'total': tot}
    
    all_used = langs_by_country[country]['lang_used']
    for lang in all_used:
        langs_used[f'{lang}_use'] = int(all_used[lang])
    
    all_wanted = langs_by_country[country]['lang_wanted']
    for lang in all_wanted:
        langs_used[f'{lang}_want'] = int(all_wanted[lang])
    
    all_langs_used.append(langs_used)

#print(all_langs_used)

# Convert the resulting dict into a dataframe
df_new = pd.DataFrame(all_langs_used)

# Replace all N/A with 0s
df_new.fillna(0, inplace=True)

#print(df_new)

# Save the dataframe to a csv
df_new.to_csv('data/langs_used_by_country.csv', encoding='utf-8')
