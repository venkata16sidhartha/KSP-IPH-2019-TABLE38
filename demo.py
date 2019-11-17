
# Reading an excel file using Python 
import xlrd 
  
# Give the location of the file 
loc = ("SampleData.csv") 
  
# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
  
# For row 0 and column 0 
for i in range(sheet.max_row):
    print(sheet.cell_value(i, 0) )

