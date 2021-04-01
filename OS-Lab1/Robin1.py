# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 21:23:44 2020

@author: AMIT
"""
def Round_robin(processes, n, bt, quantum):  
    wt = [0] * n 
    tat = [0] * n  
    rem_bt = [0] * n 
  
    for i in range(n):  
        rem_bt[i] = bt[i] 
    t = 0 
    while(1): 
        done = True
        for i in range(n): 
            if (rem_bt[i] > 0) : 
                done = False 
                if (rem_bt[i] > quantum) : 
                    t += quantum  
                    rem_bt[i] -= quantum                       
                else:
                    t = t + rem_bt[i]  
                    wt[i] = t - bt[i]                          
                    rem_bt[i] = 0
        #print(done)
        if (done == True):# checkif every thing is done 
            break
    #turn arount time 
    for i in range(n): 
        tat[i] = bt[i] + wt[i]
    print("Processes    Burst Time     Waiting",  
                     "Time    Turn-Around Time") 
    total_wt = 0
    total_tat = 0
    for i in range(n): 
  
        total_wt = total_wt + wt[i]  
        total_tat = total_tat + tat[i]  
        print(" ", process[i], "\t\t", bt[i],  
              "\t\t\t\t", wt[i], "\t\t\t\t", tat[i]) 
  
    print("\nAverage waiting time = %.5f "%(total_wt /n) ) 
    print("Average turn around time = %.5f "% (total_tat / n))  
      
process=[]
bt=[]
l=int((input("enter number of process and bt")))
for i in range(l):
    process.append(int(input()))

print('enter value for bt')

for i in range(l):
    bt.append(int(input()))
quantom=int(input('enter value for quantom:'))
Round_robin( process, l, bt,quantom)