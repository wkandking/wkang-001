#!/usr/bin/env python3
import sys
try:
    num=int(sys.argv[1])
except:
    print("Parameter Error")
if num <= 3500:
    res=0
elif num-3500<=1500:
    res=(num-3500)*0.03
elif num-3500>1500 and num-3500<=4500:
    res=(num-3500)*0.1-105
elif num-3500>4500 and num-3500<=9000:
    res=(num-3500)*0.2-555
elif num-3500>9000 and num-3500<=35000:
    res=(num-3500)*0.25-1005
elif num-3500>35000 and num-3500<=55000:
    res=(num-3500)*0.3-2755
elif num-3500>55000 and num-3500<=80000:
    res=(num-3500)*0.35-5505
elif num-3500>80000:
    res=(num-3500)*0.45-13505

res=format(res,".2f")
print(res)    
