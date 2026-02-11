import pandas as pd


info2 = {
    "city": ['New York', 'Hong-Kong', 'shenzeng', 'California', 'Las-vegas','Mumbai', 'Washington', 'manhattan'],
    "companiestenure": [10,45,90,34,32, 55,39,53],
    "revenueInBillion": [3, 500,2000,450,323,49,200,400],
    "Performance": [96,96,93,92,91,90,98,98]

}

gg = pd.DataFrame(info2)
print(gg)

#gg.drop(columns = ["ColumnName"], inplaceTrue)
gg.drop(columns = ["Performance"], inplace=True)
print(gg)