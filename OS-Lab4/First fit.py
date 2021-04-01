# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 09:13:56 2021

@author: AMIT
"""

def FirstFit(block_Size, process_Size): 
          
# code to store the block id of the block that needs to be allocated to a process
    allocate = [-1] * len(block_Size)  
  
    # Any process is assigned with the memory at the initial stage 
  
    # find a suitable block for each process 
    # the blocks are allocated as per their size 
  
    
    for i in range(len(block_Size)): 
        for j in range(len(block_Size)): 
            if block_Size[j] >= process_Size[i]: 
                  
                # assign the block j to p[i] process  
                allocate[i] = j  
  
                # available block memory is reduced   
                block_Size[j] -= process_Size[i]  
  
                break

      
    print(" Process  Process Size    Block Number")
 
    for i in range(len(block_Size)): 
    
        print(" ", i + 1, "      ", process_Size[i], "         ", end = "     ") 

    
        if allocate[i] != -1:  

            print(allocate[i] + 1)
        else: 
    
            print ("Not Allocated")         
    
TOtal_block=int(input("Enter length:" ))
Number=[]
Block_size=[]
Process_size=[]

for i in range((TOtal_block)):
    
    data=int(input("Enter Block Size:"))
    Block_size.append(data)
for i in range((TOtal_block)):
    
    data=int(input("Enter Process Size:"))
    Process_size.append(data)
print(Block_size)
print(Process_size)
FirstFit(Block_size,Process_size)