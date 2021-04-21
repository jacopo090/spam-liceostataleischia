import requests, threading

i=1

def do_request():
    global i
    while True:
        r = requests.get("https://www.liceoischia.edu.it/index.php/cerca-nel-sito/11-generale/167-foto-01")
        i=i+1
        print(i)

threads = []

for i in range(50):
    t = threading.Thread(target=do_request)
    t.daemon = True
    threads.append(t)

for i in range(50):
    threads[i].start()

for i in range(50):
    threads[i].join()