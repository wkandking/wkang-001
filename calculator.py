#!/usr/bin/env python3
import sys
import csv
import os
class Config(object):
    def __init__(self,filename):
        self.config=self._read_config(filename)
    def _read_config(self,filename):
        config={}
        with open(filename) as file:
            for data in file:
                data=data.strip()
                name,num1=data.split('=')
                config[name]=num1
        return config
class UserData(object):
    def __init__(self,filename,config):
        self.userdata=self._read_user_data(filename)
        self.res=self.calculate(config)
    def _read_user_data(self,filename):
        userdata={}
        with open(filename) as file:        
            for data in file:
                name2,num2=data.split(',')
                userdata[name2]=num2.strip()
        return userdata
    def count_res(self,num):
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
        return res
    def calculate(self,config):
        res=[]
        lv=float(config['YangLao'])+float(config['YiLiao'])+float(config['ShiYe'])+float(config['GongShang'])+float(config['ShengYu'])+float(config['GongJiJin'])
        JiShuL=float(config['JiShuL'])
        JiShuH=float(config['JiShuH'])
        for name,fee1 in self.userdata.items():
            fee=float(fee1)
            if fee<=JiShuL:
                fee=JiShuL
            elif fee>JiShuL and fee <= JiShuH:
                fee=fee
            elif fee>JiShuH:
                fee=JiShuH
            num3=self.count_res(fee)
            res.append(name+","+fee1+","+format(fee*lv,'.2f')+","+format(num3,'.2f')+","+format(fee-fee*lv-num3,'.2f'))
        return res
    def export(self,filename1):
        res=self.res
        with open(filename1,'w')  as f:
            a=0 
            for i in res:
                a+=1
                if a==len(res):
                    f.write(i)
                    continue
                f.write(i+'\n')
          
if __name__=='__main__':
    try:
        if os.path.isfile(sys.argv[2]) and os.path.isfile(sys.argv[4]) :
            argv=sys.argv[1:]
            a=Config(argv[1])
            b=UserData(argv[3],a.config)
            b.export(argv[5])
        else:
            print('文件不存在')
            os.exit()
         
       
    except Exception as e:
        print(e)
        os.exit()
    
    
    
    
            
    
        
                
                    
