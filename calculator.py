#!/usr/bin/env python3
import sys
import csv
import os
class Args(object):
    def __init__(self):
        self.args=sys.argv[1:]
    def get_filename(self,arg,ges):
        try:
            filename=self.args[self.args.index(arg)+1]
            left,right=filename.split('.')
            if arg=='-o':
                if right==ges:
                    return filename
            else:
                if os.path.isfile(filename) and right==ges:
                    return filename
                else:
                    print('file bot found')
                    exit()
            
        except Exception as e:
            print(e)
            exit()



class Config(object):
    def __init__(self,filename):
        self.config=self._read_config(filename)
    def _read_config(self,filename):
        config={}
        with open(filename) as file:
            reader=csv.reader(file)
            for data in reader:
                data=data[0].strip()
                name,num1=data.split('=')
                config[name]=num1
        return config



class UserData(object):
    def __init__(self,filename,config):
        self.userdata=self._read_user_data(filename)
        self.res=self.calculate(config)
    def _read_user_data(self,filename):
        userdata=[]
        with open(filename) as file:
            f_csv=csv.reader(file)        
            for data in f_csv:
                userdata.append(data)
        print(userdata)
        return userdata
    def count_res(self,num1):
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
        elif num1-3500>35000 and num1-3500<=55000:
            res=(num1-3500)*0.3-2755
        elif num1-3500>55000 and num1-3500<=80000:
            res=(num1-3500)*0.35-5505
        elif num1-3500>80000:
            res=(num1-3500)*0.45-13505
        return res
    def calculate(self,config):
        res=[]
        lv=float(config['YangLao'])+float(config['YiLiao'])+float(config['ShiYe'])+float(config['GongShang'])+float(config['ShengYu'])+float(config['GongJiJin'])
        JiShuL=float(config['JiShuL'])
        JiShuH=float(config['JiShuH'])
        for data in self.userdata:
            name,fee1=data[0],data[1]
            fee=float(fee1)
            if fee<=JiShuL:
                fee=JiShuL
            elif fee>JiShuL and fee <= JiShuH:
                fee=fee
            elif fee>JiShuH:
                fee=JiShuH
            num3=self.count_res(float(fee1)-fee*lv)
            data=[name,fee1,format(fee*lv,'.2f'),format(num3,'.2f'),format(float(fee1)-fee*lv-num3,'.2f')]
            res.append(data)
        print(res)
        return res
    def export(self,filename1):
        res=self.res
        with open(filename1,'w',newline='')  as f:
            writer=csv.writer(f)
            writer.writerows(res)
                  
if __name__=='__main__':
    a=Args()
    filename1=a.get_filename('-c','cfg')
    filename2=a.get_filename('-d','csv')
    filename3=a.get_filename('-o','csv')
    b=Config(filename1)
    c=UserData(filename2,b.config)
    c.export(filename3)

    
    
    
    
            
    
        
                
                    
