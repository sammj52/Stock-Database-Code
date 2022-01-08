import time
import datetime
import pandas as pd

ticker = 'MSFT'
period1 = int(time.mktime(datetime.datetime(2021, 12, 15, 23, 59).timetuple()))
period2 = int(time.mktime(datetime.datetime(2022, 1, 6, 23, 59).timetuple()))

period1_listtwo = int(time.mktime(datetime.datetime(2021, 12, 16, 23, 59).timetuple()))
period2_listtwo = int(time.mktime(datetime.datetime(2022, 1, 7, 23, 59).timetuple()))
interval = '1d' # 1d, 1m

query_stringone = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'
query_stringtwo = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1_listtwo}&period2={period2_listtwo}&interval={interval}&events=history&includeAdjustedClose=true'

df = pd.read_csv(query_stringone)
dftwo = pd.read_csv(query_stringtwo)

column = df['Close'].to_string(index=False)
columntwo = dftwo['Close'].to_string(index=False)

closes = column.splitlines()
closestwo = columntwo.splitlines()
#print(type(closes[1]))

float_closes = list(map(float, closes))
float_closestwo = list(map(float, closestwo))
#print(float_closes)

daily_changes_listone = []
for i in range(1,len(float_closes)):
    x = float_closes[i] - float_closes[i-1]
    daily_changes_listone.append(x)

daily_changes_listtwo = []
for i in range(1,len(float_closestwo)):
    x = float_closestwo[i] - float_closestwo[i-1]
    daily_changes_listtwo.append(x)

#print(daily_changes)

'''Grouping Upward and Downward Movements'''
upward_movements = []
downward_movements = []
for change in daily_changes_listone:
	if change > 0:
		upward_movements.append(change)
		downward_movements.append(0)
	elif change < 0:
		downward_movements.append(change)
		upward_movements.append(0)
	else:
		upward_movements.append(0)
		downward_movements.append(0)

upward_movementstwo = []
downward_movementstwo = []
for change in daily_changes_listtwo:
	if change > 0:
		upward_movementstwo.append(change)
		downward_movementstwo.append(0)
	elif change < 0:
		downward_movementstwo.append(change)
		upward_movementstwo.append(0)
	else:
		upward_movementstwo.append(0)
		downward_movementstwo.append(0)

print(upward_movementstwo)
print(downward_movementstwo)

abs_downward_movements = [abs(x) for x in downward_movements]
abs_downward_movementstwo = [abs(x) for x in downward_movementstwo]
#print(abs_downward_movements)


'''Average up & down movement of 14 days'''
previous_upchange = upward_movements[-1]
previous_downchange = abs_downward_movements[-1]

previous_upchangetwo = upward_movementstwo[-1]
previous_downchangetwo = abs_downward_movementstwo[-1]


initial_up_movement = sum(upward_movements)/len(upward_movements)
print(len(upward_movements))

avg_up_movement = (initial_up_movement*13 + previous_upchangetwo)/14

initial_down_movement = sum(abs_downward_movements)/len(abs_downward_movements)
avg_down_movement = (initial_down_movement*13 + previous_downchangetwo)/14

#print(avg_up_movement)
#print(avg_down_movement)

'''Relative Strength Calculation'''
rs = avg_up_movement/avg_down_movement
#print(rs)

'''Final RSI Formula'''
rsi = 100 - 100/(rs + 1)

print(rsi)
