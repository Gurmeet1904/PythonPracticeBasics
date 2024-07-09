# Program to concatenate two excel file into one

#importing all the libraries
import os
import pandas as pd

#The directory of the stored excel sheets should be same as the current directory
folder_path = '.\\Task1_ExcelSheet'

#Creating an empty dataframe
df = []

#Navigating through the for loop and checking conditions whether the extension is ".xlsx" or not
for file in os.listdir(folder_path):
    if file.endswith('.xlsx'):
        print('Loading file {0}...'.format(file))
        df.append(pd.read_excel(os.path.join(folder_path, file)))

#Concatinating the files and naming the final sheet as Task1_ExcelSheet_Result.xlsx
df_master = pd.concat(df, axis=0)
df_master.to_excel('Task1_ExcelSheet_Result.xlsx', index=False)







