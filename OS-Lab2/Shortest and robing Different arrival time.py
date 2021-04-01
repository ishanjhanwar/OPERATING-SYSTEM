'''
CPU Scheduling with different arrival times
1. Shortest Job First
2. Round Robin
'''

import pandas as pd
import numpy as np

# First Come First Serve

def FCFS(PID, BT, AT):

    n = len(PID)

    ''' Calculating Waiting Time '''
    WT = [0] # Waiting Time for first process is 0

    for i in range(1, n):
        WT_CAL = BT[i - 1] + WT[i - 1]
        WT.append(WT_CAL)

    ''' Calculating Turn Around Time '''
    TA = []
    for i in range(n):
        TA_CAL = BT[i] + WT[i]
        TA.append(TA_CAL)

    lst = list(zip(PID, AT, BT, WT, TA))
    df = pd.DataFrame(lst, columns=['PID', 'Arrival Time', 'Burst Time', 'Waiting Time', 'Turn Around Time'])

    print(df)

    ''' Calculating Average Waiting Time '''
    wt = np.mean(df['Waiting Time'])
    print(f'Average Waiting Time - {wt}')

    ''' Calculating Average Turn Around Time '''
    tat = np.mean(df['Turn Around Time'])
    print(f'Average Turn Around Time - {tat}')

    print()


# Shortest Job First with different Arrival Times

def SJF(PID, AT, BT):
    n = len(PID)
    WT = []
    CT = 0 # Current Time
    lst1 = list(zip(PID, AT, BT))
    df1 = pd.DataFrame(lst1, columns=['PID', 'Arrival Time', 'Burst Time'])

    df_sort = df1.sort_values(by=['Arrival Time', 'Burst Time']).reset_index(drop=True) # Sorting by Arrival and Burst time
    #print(df_sort)

    col_1 = [0] * n
    col_2 = [0] * n
    col_3 = [0] * n

    lst2 = list(zip(col_1, col_2, col_3))
    df2 = pd.DataFrame(lst2, columns=['PID', 'Arrival Time', 'Burst Time'])

    for i in range(n):
        df_sub = df_sort[df_sort['Arrival Time'] <= CT]
        df_sub = df_sub.sort_values(by='Burst Time').reset_index(drop=True)
        df2.iloc[i, :] = df_sub.iloc[0, :]
        CT += df_sub['Burst Time'][0]
        df_sort = df_sort.sort_values(by='Burst Time')
        df_sort.drop([0], axis=0, inplace=True)
        df_sort = df_sort.reset_index(drop=True)

    FCFS(df2['PID'], df2['Burst Time'], df2['Arrival Time'])


# Round Robin with different Arrival Times

def RR(PID, AT, BT, quantum):

    n = len(PID)

    lst = list(zip(PID, AT, BT))

    df = pd.DataFrame(lst, columns=['PID', 'Arrival Time', 'Burst Time'])

    CT = 0 # Current Time

    df['Task Done'] = 0

    df['Waiting Time'] = 0

    TAT = []

    while True:

        done = True

        for i in range(n):
            if df['Task Done'][i] == 0:
                done = False
                break

        for i in range(n):
            if CT >= df['Arrival Time'][i]:
                temp = quantum

                if df['Burst Time'][i] < quantum:
                    temp = df['Burst Time'][i]

                df['Burst Time'][i] -= temp
                CT += temp
                for j in range(n):
                    if j != i and df['Task Done'][j] != 1:
                        df['Waiting Time'][j] += temp

            if df['Burst Time'][i] == 0:
                    df['Task Done'][i] = 1

        if done == True:
            break

    for i in range(n):
        TAT_CAL = BT[i] + df['Waiting Time'][i]
        TAT.append(TAT_CAL)

    df_final = df

    df_final['Burst Time'] = BT

    df_final.drop(['Task Done'], axis=1, inplace=True)

    df_final['Turn Around Time'] = TAT

    print(df_final)

    print()

    ''' Calculating Average Waiting Time '''
    wt = np.mean(df_final['Waiting Time'])
    print(f'Average Waiting Time - {wt}')

    ''' Calculating Average Turn Around Time '''
    tat = np.mean(df_final['Turn Around Time'])
    print(f'Average Turn Around Time - {tat}')

    print()
