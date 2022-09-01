import pandas as pd
from collections import Counter


YEAR = 2022
df = pd.read_csv(f"rawdata/{YEAR}/survey_results_public.csv", dtype=str)

df = df[['ResponseId', 'EdLevel', 'YearsCode', 'Country', 'OrgSize', 'Age', 'Gender']]

for i in df.index:
    if str(df.at[i, "Gender"]) == "nan":
        df.at[i, "Gender"] = "Unknown"
    elif df.at[i, "Gender"] not in ["Man", "Woman"]:
        df.at[i, "Gender"] = "Other"
        
    if str(df.at[i, "EdLevel"]) == "nan":
        df.at[i, "EdLevel"] = "Unknown"
    
    if str(df.at[i, "YearsCode"]) == "nan":
        df.at[i, "YearsCode"] = "Unknown"
        
    if str(df.at[i, "Country"]) == "nan":
        df.at[i, "Country"] = "Unknown"
        
    if str(df.at[i, "Age"]) == "nan":
        df.at[i, "Age"] = "Unknown"
    
    if str(df.at[i, "OrgSize"]) in ["nan", "I don’t know"]:
        df.at[i, "OrgSize"] = "Unknown"


#print(df)

# Save the dataframe to a csv
df.to_csv(f"data/{YEAR}_educationplus_dataset.csv", encoding="utf-8")
