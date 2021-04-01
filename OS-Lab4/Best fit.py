# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 18:52:29 2021

@author: AMIT
"""

def bestFit(blockSize, m, processSize, n): 
      
     
    allocation = [-1] * n 
      
 
    for i in range(n): 
          
        # Find the best fit block for 
        # current process  
        index = 0
        for j in range(m): 
            if blockSize[j] >= processSize[i]: #blockSize = [100, 500, 200, 300, 600]  
                if index == 0:  ##processSize = [212, 417, 112, 426]
                    index = j  
                elif blockSize[index] < blockSize[j]:  
                    index = j 
  
        # If we could find a block for  
        # current process  
        if index != 0: 
              
            # allocate block j to p[i] process  
            allocation[i] = index  
  
            # Reduce available memory in this block.  
            blockSize[index] -= processSize[i] 
  
    print("Process No. Process Size     Block no.") 
    for i in range(n): 
        print(i + 1, "         ", processSize[i],  
                                end = "           ")  
        if allocation[i] != 0:  
            print(allocation[i] + 1)  
        else: 
            print("Not Allocated") 
  
  
blockSize = [100, 500, 200, 300, 600]  
processSize = [212, 417, 112, 426]  
m = len(blockSize)  
n = len(processSize)  
  
bestFit(blockSize, m, processSize, n) 