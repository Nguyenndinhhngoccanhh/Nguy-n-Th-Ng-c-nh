# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 14:10:17 2024

@author: Ngoc Anh
"""

N = int(input("Nhập vào số nguyên dương N có 2 chữ số: "))
if 10 <= N <= 99:
    hang_chuc = N // 10
    hang_don_vi = N % 10
    tong = hang_chuc + hang_don_vi
    print(f"Tổng các chữ số của {N} là: {tong}")
else:
    print("Nhập một số nguyên dương có 2 chữ số.")








