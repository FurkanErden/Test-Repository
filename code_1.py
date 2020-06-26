import datetime
import time

for x in range(1, 10000):
    time.sleep(10)
    print("Hello World!" + str(datetime.datetime.now()))
