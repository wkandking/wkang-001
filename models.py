#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     models
   Description :
   Author :       王康
   date：          2018/4/8
-------------------------------------------------
   Change Activity:
                   2018/4/8:
-------------------------------------------------
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer
engine=create_engine('mysql+mysqldb://root@localhost:3306/shiyanlou?charset=utf8')
Base=declarative_base()

class Course(Base):
    __tablename__='courses'

    id=Column(Integer,primary_key=True)
    name=Column(String(64),index=True)
    update_time=Column(String(64))
    commits=Column(Integer)
    branches=Column(Integer)
    releases=Column(Integer)
if __name__=='__main__':
    Base.metadata.create_all()
