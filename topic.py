"""

1- how bit is your dataset
2- what are the names of the column

shape and column
"""

import pandas as pd

info = {
    "city": ['New York', 'Hong-Kong', 'shezeng', 'California', 'Las-vegas','Mumbai', 'Washington', 'manhattan'],
    "companiestenure": [10,45,90,34,32, 55,39,53],
    "revenueInBillion": [3, 500,2000,450,323,49,200,400],
    "Performance": [96,96,93,92,91,90,98,99]

}
bb = pd.DataFrame(info)
print("Demo DataFrame")
print(bb)
print(f'Shape: {bb.shape}')
print(f'Column Names: {bb.columns}')