
import pandas as pd

info = {
    "city": ['New York', 'Hong-Kong', 'shenzeng', 'California', 'Las-vegas','Mumbai', 'Washington', 'manhattan'],
    "companiestenure": [10,45,90,34,32, 55,39,53],
    "revenueInBillion": [3, 500,2000,450,323,49,200,400],
    "Performance": [96,96,93,92,91,90,98,99]

}

gg = pd.DataFrame(info)
print(gg)
gg["IncrementInRevenue"] = gg['revenueInBillion']*0.3
print(gg)


#using the insert method
#gg.insert(0, 'Column_Name', some_datat)
gg.insert(0, "valuationINtrillion", [11,3,4,6,3,7,8,9])
print(gg)