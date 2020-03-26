
import pandas as pd
read_csv_files="realEstate_trans.csv"
csv_data=pd.read_csv(read_csv_files)
print("the data types of columns of realEstate_trans.csv are: ")
print(csv_data.dtypes)
print("the summary of the realEstate_trans.csv file is: ")
print(csv_data.describe())
print("the structure of the realEstate_trans.csv file is: ")
print(csv_data.info())
print("Head records from realEstate_trans.csv file")
print(csv_data.head(10))
s=csv_data.head(10)
s.info()
print("tail records from realEstate_trans.csv file")
print(csv_data.tail(5))
mydata=csv_data.tail(5)
write_csv_files="output/realEstate_trans.csv"
w=open(write_csv_files,"w")
w.write(csv_data.to_csv(sep=',',index = False))
w.close()
with open(write_csv_files,'w') as write_csv:
    write_csv.write(s.to_csv(sep=','))


print(csv_data.info(verbose = True))
