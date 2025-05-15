

# to run mai/jarvis
import multiprocessing


def start():
    print("process 1 running...")
    from main import start
    start()


# to run hotword
def listenHotword():
    print('Process 2 running...')
    from engine.features import hotword
    hotword()

if __name__ == '__main__':
    p1 = multiprocessing.Process(target = start())
    p2 = multiprocessing.Process(target = listenHotword())

    p1.start()
    p2.start()
    p1.join()

    if p2.is_alive():
        p2.join()
        p2.terminate()

    print("system stop")