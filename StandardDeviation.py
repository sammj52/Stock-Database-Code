import pandas as pd 
import numpy as np 
import datetime as dt 
import pandas_datareader.data as web
import statistics

start = dt.datetime(2019,12,20)
end = dt.datetime(2020,1,10)
df = web.DataReader('TSLA', 'yahoo', start, end)

stand_dev = df.std(axis=0) 
percent_change = df['Adj Close'].pct_change()*100
adj_clo = df.iloc[:,5]

change1 = df.iloc[1,5] - df.iloc[0,5]
change2 = df.iloc[2,5] - df.iloc[1,5]
change3 = df.iloc[3,5] - df.iloc[2,5]
change4 = df.iloc[4,5] - df.iloc[3,5]
change5 = df.iloc[5,5] - df.iloc[4,5]
change6 = df.iloc[6,5] - df.iloc[5,5]
change7 = df.iloc[7,5] - df.iloc[6,5]
change8 = df.iloc[8,5] - df.iloc[7,5]
change9 = df.iloc[9,5] - df.iloc[8,5]
change10 = df.iloc[10,5] - df.iloc[9,5]
change11 = df.iloc[11,5] - df.iloc[10,5]
change12 = df.iloc[12,5] - df.iloc[11,5]
change13 = df.iloc[13,5] - df.iloc[12,5]

change_sum = change1 + change2 + change3 + change4 + change5 + change6 + change7 + change8 + change9 + change10 + change11 + change12 + change13

my_list = [change1,change2,change3,change4,change5,change6,change7,change8,change9,change10,change11,change12,change13]
res = statistics.pstdev(my_list)

print("Dataframe: ")
print(df.head(5))
##print(stand_dev)

print("End of Day Stock Price: ") 
print(adj_clo)
##print("Total: ")
##print(adj_clo.sum()) 

print("Adj Closes Standard Deviation: ")
print(df.loc[:,'Adj Close'].std())

print("Adj Close Percent Change: ")
print(df['Adj Close'].pct_change()*100) 

print("Adj Close Percent Change Standard Deviation: ")
print(percent_change.std())

print("Monetary Change Per Day: ")
print(round(change1,2))
print(round(change2,2))
print(round(change3,2))
print(round(change4,2))
print(round(change5,2))
print(round(change6,2))
print(round(change7,2))
print(round(change8,2))
print(round(change9,2))
print(round(change10,2))
print(round(change11,2))
print(round(change12,2))
print(round(change13,2))

print("Total Monetary Change (within past 2 weeks): " + str(change_sum))

print("Standard Deviation of Monetary Change: " + str(res))