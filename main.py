import pandas as pd

# read data from the csv files

# fd = pd.read_csv("sales_data_sample.csv" ,encoding="latin1")
# fd = pd.read_excel("FSI-2023-DOWNLOAD.xlsx"
df = pd.read_json("titanic.json")



print(df)
