# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 23:19:18 2021

@author: AMIT
"""
# blocks as per Next fit algorithm  
def NextFit(blockSize, m, processSize, n): 
      

    allocation = [-1] * n  
    j = 0
  

    for i in range(n): 
  
        # Do not start from beginning  
        while j < m: 
  
            if blockSize[j] >= processSize[i]: 
  
                # allocate block j to p[i] process  
                allocation[i] = j  
  
                # Reduce available memory in this block.  
                blockSize[j] -= processSize[i]  
  
                break
  
            j = (j + 1)%m
            print(j)
  
    print("Process No. Process Size Block no.")  
    for i in range(n): 
        print(i + 1, "         ", processSize[i], 
                                    end = "     ") 
        if allocation[i] != -1: 
            print(allocation[i] + 1)  
        else: 
            print("Not Allocated") 
  
blockSize = [5, 10, 20] 
processSize = [10, 20, 5]  
m = len(blockSize) 
n= len(processSize) 
NextFit(blockSize, m, processSize, n) 
            