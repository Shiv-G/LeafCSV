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





