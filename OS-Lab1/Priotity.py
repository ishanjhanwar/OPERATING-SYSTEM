# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 11:49:31 2020

@author: AMIT
"""


def Priority(p,n,bt,priority):
    for i in range(l):
        for j in range(i,l):
            if priority[i]>priority[j]:
                temp=priority[i]
                priority[i]=priority[j]
                priority[j]=temp
                y=p[i]
                p[i]=p[j]
                p[j]=y
                z=bt[i]
                bt[i]=bt[j]
                bt[j]=z
    waitingtime=[]
    turnaaround_time=[]
    for i in range(l): 
        if i==0:
            waitingtime.append(0)
        else:
            x=bt[i-1]+ waitingtime[i-1]
            waitingtime.append(x)
    #print(waitingtime)
    for i in range(l):
        if i==0:
            turnaaround_time.append(bt[i])
        else:
            y=bt[i]+waitingtime[i]
            turnaaround_time.append(y)
    #print(turnaaround_time)
    
    totaltime_waiting=0
    total_turnaround=0
    print( "Processes Burst time " + " Waiting time " + " Turn around time")
    for i in range(l):
        
        
        print(" " + str(p[i]) + "\t\t\t"+str(bt[i])+"\t\t\t"+ str(waitingtime[i])+"\t\t\t"+ str(turnaaround_time[i]))
    Average_waiting_time=(totaltime_waiting)/l
    Average_turnaround_time=(total_turnaround)/l

    print("Avg waiting time=",Average_waiting_time)
    print("Avg turnaround time=",Average_turnaround_time)
    
    
    

process=[]
bt=[]
priority=[]
l=int((input("enter number of process and bt")))
for i in range(l):
    process.append(int(input()))

print('enter value for bt')

for i in range(l):
    bt.append(int(input()))
print('enter value for priority')
for i in range(l):
    priority.append(int(input()))

print("process:")
print(process)
print("Burst Time")
print(bt)
print("Give Priority")
print(priority)
Priority(process, l, bt, priority)