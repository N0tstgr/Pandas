import pandas as pd


info1 = {
    "city": ['New York', 'Hong-Kong', 'shenzeng', 'California', 'Las-vegas','Mumbai', 'Washington', 'manhattan'],
    "companiestenure": [10,45,90,34,32, 55,39,53],
    "revenueInBillion": [3, 500,2000,450,323,49,200,400],
    "Performance": [96,96,93,92,91,90,98,99]

}

gg = pd.DataFrame(info1)
print(gg)

#loc[]
#gg.loc[row_index, "Column Name"] = new Value
gg.loc[0,'Performance'] = 102
print(gg)