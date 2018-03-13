#!/usr/bin/env python
# coding=utf-8

# coding=utf-8
import sys
import os
import re


def construct_data(lineIn):
    #vec =[map(int,x)  for x in re.findall(r"\d+\.?\d*",stringIn)]
    
    stringIn = lineIn.strip('\r\n').split('\t')
    
    vec =[]
    vec.append(int(re.findall(r"\d+\.?\d*",stringIn[1])[0]))
    
    year = int(stringIn[2].split(' ')[0].split('-')[0])
    month = int(stringIn[2].split(' ')[0].split('-')[1])
    day = int(stringIn[2].split(' ')[0].split('-')[2])
    
    vec.append(year)
    vec.append(month)
    vec.append(day)
    
    hour = int(stringIn[2].split(' ')[1].split(':')[0])
    minute = int(stringIn[2].split(' ')[1].split(':')[1])
    second = int(stringIn[2].split(' ')[1].split(':')[2])
    
    vec.append(hour)
    vec.append(minute)
    vec.append(second)
    
    return vec
data = []
for i in range(1,6):
    path="H:\软挑\初赛文档\练习数据\data_2015_"+str(i)+".txt"
    datafile = open(path)
    for line in datafile.readlines():
        data_vec = construct_data(line)
        data.append(data_vec)

# =============================================================================
# dic={}
# flovr=[i[4] for i in data]
# for i in flovr:
#     if i in dic.keys():
#         dic[i]+=1
#     else:
#         dic.setdefault(i,1)
# import matplotlib.pyplot as plt
# plt.plot(dic.keys(),dic.values(),'.')
# =============================================================================

D={1:0,2:31,3:59,4:90,5:120,6:151}#将月的数据转化成天。省略时分秒？12点前算前一天，12点后算当天。
#new_data=[]
#2+7k是周六，3+7k是周日
#1是元旦，1，2假，4班。46班，49~51，74,75春节假，59班，96清明假，121劳动假，173端午假
for n,i in enumerate(data):
    data[n]=[i[0],D[i[2]]+i[3]-1*(i[4]<12)-1]#索引从0开始


work=[3,45,58]
voc=[0,1,48,49,50,73,74,95,120,172]
workDay=[]
for i in range(181):
    if i in work:
        workDay.append(1)
    elif i in voc:
        workDay.append(0)
    elif i%7 in (2,3):
        workDay.append(0)
    else:
        workDay.append(1)



