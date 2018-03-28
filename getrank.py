#/usr/bin/env python3
#-*- coding:utf-8 -*-
import sys

from pymongo import MongoClient


def get_rank(user_id):
	client=MongoClient()
	db=client.shiyanlou
	contests=db.contests
	user_data=[]   #最终结果列表 
	for i in range(1,10):
		scores=0
		submit_times=0
		for data in contests.find({'user_id':i}):
			scores+=int(data['score'])
			submit_times+=int(data['submit_time'])
		user_data.append((i,scores,submit_times))
	user_data=sorted(user_data,key=lambda data:data[1],reverse=True)
	# print(user_data)
	if user_id<=0 or user_id > len(user_data):
		print('NOTFOUND')
		exit()	
	for a in user_data:
		if user_id==a[0]:
			id=user_data.index(a)
	rank=id+1
	score=user_data[id][1]
	submit_time=user_data[id][2]
	return rank,score,submit_time
if __name__=='__main__':
	 if  len(sys.argv)>2 or sys.argv[1].isdigit()==False :
	 	print("Parameter Error")
	 	exit()
	 user_id=sys.argv[1].strip()
	 user_id=int(user_id)
	 userdata=get_rank(user_id)
	 print(userdata)

