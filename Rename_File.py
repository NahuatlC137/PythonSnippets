import os
import pandas as pd

os.chdir("DIR")

NameKey = pd.read_excel('WB_NAME.xlsx', 'SHEET_NAME')

path = os.getcwd()
FileNames = os.listdir(path)
DealerAccountNumber = 0
FileExtension = '.pdf'

for file in FileNames:
    if file[:1].isdigit():
        DealerAccountNumber = int(file[:7])
        DocumentType = file[8:]
        Name = (NameKey.loc[NameKey['AccountNumber'] == DealerAccountNumber, 'Name'].item())
        os.rename(file, Name + FileExtension)
