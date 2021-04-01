import threading
import random
import time

class BakeryAlgorithm():

    # ticket for threads in line,  n is number of threads
    tickets = [0, 1, 2, 3, 4]

    # True when thread entering in line
    entering = [False] * 5

    def lock(self, *args):
        self.entering[args[0]] = True

        maximum = 0

        for ticket in self.tickets:
            maximum = max(maximum, ticket)

        self.tickets[args[0]] = maximum + 1

        self.entering[args[0]] = False

        for i in range(len(self.tickets)):
            if i != args[0]:
                # Wait until thread j recieves its number:
                while self.entering[i]:
                    print('Waiting')

                # Wait until all threads with smaller numbers or with the same number, but with higher priority finish their work:
                while self.tickets[i] != 0 and (self.tickets[args[0]] > self.tickets[i] or (self.tickets[args[0]] == self.tickets[i] and args[0]) > i):
                    print('Waiting')

        # The critical section goes here ...
        print(f'Critical section used by process {args[0]}')

        # Exit section
        self.tickets[args[0]] = 0

    def main(self):
        t1 = threading.Thread(target = self.lock, args = (0,))
        t2 = threading.Thread(target = self.lock, args = (1,))
        t3 = threading.Thread(target = self.lock, args = (2,))
        t4 = threading.Thread(target = self.lock, args = (3,))
        t5 = threading.Thread(target = self.lock, args = (4,))

        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()


if __name__ == '__main__':
    b = BakeryAlgorithm()
    b.main()
