import sys
import time
from multiprocessing import Array, Process, RLock, Manager

DATA_FOR_TEST = [128, 255, 99999, 10651060]


def factorize_1(*number):
    res = []
    for i in list(number):
        res_p = []
        for j in range(1, i+1):
            if i % j == 0:
                res_p.append(j)
        res.append(res_p)
    return res

def factorize_p(args, i, val, lock):
    res_p = []
    for j in range(1, args[i]+1):
        if args[i] % j == 0:
            res_p.append(j)

    with lock:
        val[i] = res_p

    sys.exit(0)

def factorize_4(args, arr, lock):

    pr_1 = Process(target=factorize_p, args=(args, 3, arr, lock))
    pr_1.start()

    pr_2 = Process(target=factorize_p, args=(args, 2, arr, lock))
    pr_2.start()

    pr_3 = Process(target=factorize_p, args=(args, 1, arr, lock))
    pr_3.start()

    pr_4 = Process(target=factorize_p, args=(args, 0, arr, lock))
    pr_4.start()

    pr_1.join()
    pr_2.join()
    pr_3.join()
    pr_4.join()

if __name__ == '__main__':

    time_start = time.time()
    lock = RLock()
    arr = Array('l', [0] * 4, lock=lock)
    manager = Manager()
    arr = manager.list([[], [], [], []])
    lock = manager.RLock()
    factorize_4(DATA_FOR_TEST, arr, lock)
    time_f = time.time()
    total_time = time_f - time_start
    a, b, c, d = arr
    print(f'total_time for multiprocess {total_time}.')

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]

    time_start = time.time()
    a, b, c, d = factorize_1(*DATA_FOR_TEST)
    time_f = time.time()
    total_time = time_f - time_start
    print(f'total_time for singleprocess {total_time}.')

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]

    conclusion = '''
    Для поточного набору даних вийшло, що багатопотокове виконання
    розрахунку довше за виконання в один потік. Це можу бути через
    складність створення нових потоків для заліза. Збільшення 
    складності обчислень (збільшенню порядку чисел для тесту) 
    призвело до більшої ефективності багатопотокового коду.
    '''
    print(conclusion)








