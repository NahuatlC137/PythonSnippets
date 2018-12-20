# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 12:02:21 2018

@author: Angel.Herrera
"""
import os
from zipfile import ZipFile

os.chdir("")

# Only root directories:
root_dirs = []
zip_ref = ZipFile("NAME.zip")
for f in zip_ref.namelist():
    zinfo = zip_ref.getinfo(f)
    if zinfo.is_dir():

        r_dir = f.split('/')
        r_dir = r_dir[0]
    if r_dir not in root_dirs:
        root_dirs.append(r_dir)
for d in root_dirs:
    print(d)
