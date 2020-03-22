import openpyxl
from datetime import date 

wb = openpyxl.load_workbook('C:/Users/samue/Desktop/Python Stock Codes/Key Investment Association/Excel Input/portfolioexcel.xlsx', data_only=True)

sheet = wb['Sheet1']

today = date.today()
day = today.strftime("%m/%d/%Y")

sam = int(input("Sam's Capital: "))
jack = int(input("Jack's Capital: "))
matt = int(input("Matt's Capital: "))

final_pool = int(input("Final Pool Value: "))

index_pool = [sam,jack,matt]

intial = sum(index_pool)

sam_share = sam/intial
jack_share = jack/intial
matt_share = matt/intial

s_portion = sam_share * final_pool
j_portion = jack_share * final_pool
m_portion = matt_share * final_pool

print("Sam's portion of the final amount is: " + str(s_portion) + "")
print("Jack's portion of the final amount is: " + str(j_portion) + "")
print("Matt's portion of the final amount is: " + str(m_portion) + "")

'''Current Day: Change Cells Every time used'''
sheet['B1'] = day

'''Member Proportions: Change Cells Each Trade'''
sheet['B2'] = str(s_portion)
sheet['B3'] = str(j_portion)
sheet['B4'] = str(m_portion)

'''Current Portfolio Value: Change Cells Each Time'''
sheet['B25'] = final_pool

wb.save('portfolioexcel.xlsx')
