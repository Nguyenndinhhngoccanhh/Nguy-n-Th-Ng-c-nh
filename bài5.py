# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 14:47:04 2024

@author: Ngoc Anh
"""

b = int(input("Nhập năm sinh: "))
if 1900 <= b < 2024:
    tuoi = 2024 - b
    print("Tuổi của bạn là: ", tuoi)
elif b == 2024:
    print("Bạn chưa tròn 1 tuổi")
else:
    print("Năm sinh không hợp ")
    
 