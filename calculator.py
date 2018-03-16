#!/usr/bin/env python3
import sys
def count_res(num):
    num1=num-num*0.165
    if num1 <= 3500:
        res=0
    elif num1-3500<=1500:
        res=(num1-3500)*0.03
    elif num1-3500>1500 and num1-3500<=4500:
        res=(num1-3500)*0.1-105
    elif num1-3500>4500 and num1-3500<=9000:
        res=(num1-3500)*0.2-555
    elif num1-3500>9000 and num1-3500<=35000:
        res=(num1-3500)*0.25-1005
    elif num-3500>35000 and num1-3500<=55000:
        res=(num1-3500)*0.3-2755
    elif num1-3500>55000 and num1-3500<=80000:
        res=(num1-3500)*0.35-5505
    elif num-3500>80000:
        res=(num1-3500)*0.45-13505
    res=num-res-num*0.165
    return format(res,'.2f')
try:
    for arg in sys.argv[1:]:
        name_num,num=arg.split(':')
        num=int(num)
        print(name_num+":"+count_res(num))
except:
    print("Parameter Error")    
