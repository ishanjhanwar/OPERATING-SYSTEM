# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def FCFS(process,n,bt):
    waitingtime=[]
    turnaaround_time=[]
    for i in range(n): 
        if i==0:
            waitingtime.append(0)
        else:
            x=bt[i-1]+ waitingtime[i-1]
            waitingtime.append(x)
    #print(waitingtime)
    for i in range(n):
        if i==0:
            turnaaround_time.append(bt[i])
        else:
            y=bt[i]+waitingtime[i]
            
            turnaaround_time.append(y)
        
    #print(turnaaround_time)
    
    totaltime_waiting=0
    total_turnaround=0
    print( "Processes Burst time " + " Waiting time " + " Turn around time")
    for i in range(n):
        totaltime_waiting=totaltime_waiting + waitingtime[i]
        total_turnaround=total_turnaround+turnaaround_time[i]
        
        print(" " + str(i+1) + "\t\t\t"+str(bt[i])+"\t\t\t"+ str(waitingtime[i])+"\t\t\t"+ str(turnaaround_time[i]))
    Average_waiting_time=(totaltime_waiting)/n
    Average_turnaround_time=(total_turnaround)/n

    print("Avg waiting time=",Average_waiting_time)
    print("Avg turnaround time=",Average_turnaround_time)

def SJF(p,l,bt):
    
    
    for i in range(l):
        for j in range(i,l):
            
            if bt[i]>bt[j]:
                temp=bt[i]
                bt[i]=bt[j]
                bt[j]=temp
                temp=p[i]
                p[i]=p[j]
                p[j]=temp
    
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
        totaltime_waiting=totaltime_waiting + waitingtime[i]
        total_turnaround=total_turnaround+turnaaround_time[i]
        
        print(" " + str(p[i]) + "\t\t\t"+str(bt[i])+"\t\t\t"+ str(waitingtime[i])+"\t\t\t"+ str(turnaaround_time[i]))
    Average_waiting_time=(totaltime_waiting)/l
    Average_turnaround_time=(total_turnaround)/l

    print("Avg waiting time=",Average_waiting_time)
    print("Avg turnaround time=",Average_turnaround_time)           
            
                
            
                  
    
process=[]
bt=[]
l=int((input("enter number of process and bt")))
for i in range(l):
    process.append(int(input()))

print('enter value for bt')

for i in range(l):
    bt.append(int(input()))
print("process:")
print(process)
print("Burst Time:")
print(bt)
FCFS(process,l,bt)
SJF(process,l,bt)