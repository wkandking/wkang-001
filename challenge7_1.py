#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     challenge7_1
   Description :
   Author :       王康
   date：          2018/4/29
-------------------------------------------------
   Change Activity:
                   2018/4/29:
-------------------------------------------------
"""
import pandas as pd
def get_result(str,df2):
    df3 = df2[df2.columns[6:26]]
    df3 = df3.replace({'..': None})
    df3 = df3.fillna(method='ffill', axis=1).fillna(method='bfill', axis=1)
    df3 = df3.dropna(axis=0, how='all')
    sum_sum=df3.sum(axis=1)
    sort_max =sum_sum.sort_values(ascending=False)
    max_index = sort_max.index[0]
    max_value = round(sort_max.max(),2)
    sort_min = sum_sum.sort_values()
    min_index = sort_min.index[0]
    min_value = round(sort_min.min(),2)
    sum=round(sum_sum.sum(),2)
    return str,sum,max_index,max_value,min_index,min_value
def co2():

    # 读取世界银行气候变化数据集
    results=[]
    df_climate_Data = pd.read_excel("D:/ClimateChange.xlsx", sheetname='Data')
    df_climate_Country=pd.read_excel("D:/ClimateChange.xlsx",sheetname='Country')
    df=pd.merge(df_climate_Data,df_climate_Country)
    df1=df[df['Series code']=='EN.ATM.CO2E.KT']
    df1=df1.set_index('Country code')
    df2=df1[df1['Income group']=='High income: nonOECD']
    df3=df1[df1['Income group']=='High income: OECD']
    df4 = df1[df1['Income group'] == 'Low income']
    df5 = df1[df1['Income group'] == 'Lower middle income']
    df6 = df1[df1['Income group'] == 'Upper middle income']

    results.append(get_result('High income: OECD',df3))
    results.append(get_result('High income: nonOECD',df2))
    results.append(get_result('Low income',df4))
    results.append(get_result('Lower middle income',df5))
    results.append(get_result('Upper middle income',df6))
    DataFrame=pd.DataFrame(results,index=['High income: OECD','High income: nonOECD','Low income','Lower middle income','Upper middle income'],
                        columns=['Income group','Sum emissions','Highest emission country','Highest emissions','Lowest emission country','Lowest emissions'] )
    DataFrame=DataFrame.set_index('Income group')
    return results
if __name__=='__main__':
    co2()