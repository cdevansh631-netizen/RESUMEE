# 7. Basic Alarm Clock
# Concepts: datetime, time
# Set time → plays sound (or prints “Alarm!”).

import datetime
import time
M="19:26:49"
while True:
    T=datetime.datetime.now()
    X=T.strftime("%H:%M:%S")
   
    if M==X:
        print("ALARM!!!")
        break
    else:
        pass
    time.sleep(1)


