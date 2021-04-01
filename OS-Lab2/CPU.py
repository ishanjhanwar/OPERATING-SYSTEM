from Scheduler import SJF, RR

PID = [1, 2, 3, 4]
AT = [0, 1, 2, 3]
BT = [5, 4, 2, 1]
quantum = 2

SJF(PID, AT, BT)
RR(PID, AT, BT, quantum)
