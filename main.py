import pandas as pd

# read data from the csv files

fd = pd.read_csv("sales_data_sample.csv" ,encoding="latin1")
print(fd)