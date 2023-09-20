import threading
import time

sem = threading.Semaphore(4)
sem1 = threading.Semaphore(0)

lock = threading.Lock()
p = 4


def studying(i):
    global p
    while True:
        sem.acquire()
        lock.acquire()
        p = p - 1
        print(f"\nI am {i} and I am studying. Pieces left:{p}")
        lock.release()
        time.sleep(3)
        if p == 0:
            sem1.release()


def delivering(i):
    global p
    sem1.acquire()
    print("\nDelivering a new pizza")
    time.sleep(5)
    p = 4
    sem.release()
    sem.release()
    sem.release()
    sem.release()
    print("Delivered")


s1 = threading.Thread(target=studying, args=("student_1",))
s2 = threading.Thread(target=studying, args=("student_2",))
s3 = threading.Thread(target=studying, args=("student_3",))
s4 = threading.Thread(target=studying, args=("student_4",))
s5 = threading.Thread(target=studying, args=("student_5",))
d = threading.Thread(target=delivering, args=("deliver",))
s1.start()
s2.start()
s3.start()
s4.start()
s5.start()
d.start()