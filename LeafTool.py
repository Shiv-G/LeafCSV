#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import numpy as np
import os



# Results file read
filename = "Arp3_1_disc_pores_ROI01_#_APresults.xls"
data_path = os.path.join(os.path.expanduser("~"), "Documents", "Alice_CT_data_NEW", "QuaArpCol", "Arp3_1_Disc", filename)
print(data_path)

df = pd.read_csv(data_path, delimiter="\t")
print(df.head())

slice_mask = df.Slice.isin(range(33, 35 + 1))
result = df[slice_mask]
print(result.describe())
print(result.sum())

df_perim = result['Perim.']
print(df_perim)

export_csv = result.to_csv(r'C:\Users\uos\Documents\Adam_Python\PAResults_Palisade.csv', index  = False) #selected range, all cols
export_csv = df_perim.to_csv(r'C:\Users\uos\Documents\Adam_Python\PerimDist_Perim.csv', index  = False, header = True) #perim palisade dist only



# Summary file read
filename = "Arp3_1_disc_pores_ROI01_#_APsummary.xls"
data_path = os.path.join(os.path.expanduser("~"), "Documents", "Alice_CT_data_NEW", "QuaArpCol", "Arp3_1_Disc", filename)
print(data_path)

slice_start = 31
slice_end = 33

df = pd.read_csv(data_path, delimiter="\t")
print(df.head())

base = "Arp3_1_disc_pores"
str_list = ["{}{:04d}".format(base, num) for num in range(slice_start, slice_end+1)]
slice_mask = df.Slice.isin(str_list)

result = df[slice_mask]
print(result.describe())
print(result.sum())

export_csv = result.to_csv(r'C:\Users\uos\Documents\Adam_Python\PASummary_Palisade.csv', index  = False)



# LICOR file read
filename = "christoph 201013 Re6 6_.csv"
data_path = os.path.join("D:\\", "Documents", "Lehmeier_LICOR_data", "re6", "Re6", filename)
print(data_path)

df = pd.read_csv(data_path, delimiter=",")
df = df.dropna()
print(df.head(100))
print(df.iloc[0,:].values)

#df = df.sort_values(by='Unnamed: 4',  ascending = True, na_position = 'first')

export_csv = df.to_csv(r'C:\Users\uos\Documents\Adam_Python\CleanLicor.csv', index_label = df.iloc[0,:].values, index = False)
# import_csv = pd.read_csv(r'C:\Users\uos\Documents\Adam_Python\CleanLicor.csv')
# print(import_csv)

# df2 = import_csv.sort_values('Unnamed: 4', axis = 0, ascending = True, na_position = 'first')
# print(df)
# export_csv2 = df2.to_csv(r'C:\Users\uos\Documents\Adam_Python\CleanLicorSorted.csv', index = False)





