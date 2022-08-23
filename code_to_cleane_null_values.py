import pandas as pd

data = pd.read_csv("rawdata/2017/2017intersexualitet_Hälsa.csv")
data1 = pd.read_csv("rawdata/2018/2018intersexualitet_Hälsa.csv")
data2 = pd.read_csv("rawdata/2019/2019intersexualitet_Hälsa.csv")
data3 = pd.read_csv("rawdata/2020/2020intersexualitet_Hälsa.csv")
data4 = pd.read_csv("rawdata/2021/2021intersexualitet_Hälsa.csv")
data5 = pd.read_csv("rawdata/2022/2022intersexualitet_Hälsa.csv")



new_data = data.dropna() 
new_data1 = data1.dropna() 
new_data2 = data2.dropna()
new_data3 = data3.dropna()
new_data4 = data4.dropna() 
new_data5 = data5.dropna() 



    
print(new_data)
print(new_data1)
print(new_data2)
print(new_data3)
print(new_data4)
print(new_data5)



