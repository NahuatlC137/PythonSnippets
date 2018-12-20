# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# checks whether a number is single digit or not
def format_Num(num):
    num = str(num)

    if len(num) == 1:
        return(str(0) + str(num))
    else:
        return str(num)

#function copies a file from one dir, to another

def copy_rename(old_file_name, new_file_name):
    src_dir= "DIR"
    dst_dir= "DIR"
    src_file = os.path.join(src_dir, old_file_name)
    shutil.copy(src_file,dst_dir)

    dst_file = os.path.join(dst_dir, old_file_name)
    new_dst_file_name = os.path.join(dst_dir, new_file_name)
    os.rename(dst_file, new_dst_file_name)

from calendar import monthrange
import shutil
import os
import datetime

now = datetime.datetime.now()
curr_year = now.year #2018
curr_month  = now.month + 4 #04

total_month_days = monthrange(curr_year, curr_month)[1]
filepath = "DIR"
template = "WB_NAME.xlsx"

for day in range(1, total_month_days + 1):

    wb_Name = "WB_NEW_NAME" + format_Num(curr_month) + format_Num(day) + str(curr_year)[2:] + ".xlsx"
    path_n_fileName = os.path.join(filepath + wb_Name)
    
# verifies that the file does not exist    
    if os.path.isfile(path_n_fileName) == True:
        continue
    elif os.path.isfile(path_n_fileName) == False:
        copy_rename(template, wb_Name)
