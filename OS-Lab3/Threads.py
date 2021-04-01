from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import numpy as np
import time
import matplotlib.pyplot as plt
from urllib.request import urlopen

def visualize_runtimes(results, title):
    start, stop = np.array(results).T     # .T - Transposing the array
    plt.barh(range(len(start)), stop-start, left=start)
    plt.grid(axis='x')
    plt.xlabel('Seconds')
    plt.ylabel('Tasks')
    plt.title(title)
    name = title + '.jpg'
    plt.savefig(name, dpi=300)
    print(name)
    plt.show()
    return stop[-1]-start[0]

def multithreading(func, args, workers):
    begin_time = time.time()

    with ThreadPoolExecutor(max_workers=workers) as executor:
        res = executor.map(func, args, [begin_time for i in range(len(args))])
    return list(res)

def multiprocessing(func, args, workers):
    begin_time = time.time()

    with ProcessPoolExecutor(max_workers=workers) as executor:
        res = executor.map(func, args, [begin_time for i in range(len(args))])
    return list(res)

def download(url, base):
    start = time.time() - base

    try:
        resp = urlopen(url)

    except Exception as e:
        print('ERROR: %s' % e)

    stop = time.time() - base

    return start, stop

N = 16 # no. of tasks
URL = 'http://www.pdf995.com/samples/pdf.pdf'
urls = [URL for i in range(N)]

if __name__ == '__main__':
    visualize_runtimes(multithreading(download, urls, 1), '1 Thread')
    visualize_runtimes(multithreading(download, urls, 2), '2 Threads')
    visualize_runtimes(multithreading(download, urls, 3), '3 Threads')
    visualize_runtimes(multithreading(download, urls, 4), '4 Threads')
