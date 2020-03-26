

import pandas as pd
read_xls="realEstate_trans.xlsx"
write_xls="output/realEstate_trans.xlsx"

xls_file=pd.ExcelFile(read_xls)

xls_read={
        sheetname:xls_file.parse(sheetname)
            for sheetname in xls_file.sheet_names
        }

#A=[2**x for x in range(0,9)]

print(xls_read['Sacramento'].head(10)['price'])

with pd.ExcelWriter(write_xls) as exwrit:
    xls_read['temp'].to_excel(exwrit,sheet_name='S1')
    xls_read['Sacramento'].to_excel(exwrit,sheet_name='S2')
xls_read['temp'].to_excel(write_xls, 'Sa')