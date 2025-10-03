import datetime
from time import sleep

def main():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    for i in range(5):
        print(current_time)
        sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")

if __name__ == '__main__': main()