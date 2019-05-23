import pandas as pd 




data_frame = pd.read_csv("data.csv")
column_name=[]
data_frame.head()
for col in data_frame:
	column_name.insert(0,col)

print(column_name)