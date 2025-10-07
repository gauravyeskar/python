# According to current time wish message:- 

import time,datetime
currentTime = int(time.strftime('%H'))
if currentTime > 00 and currentTime < 12:
    print(datetime.datetime.now().strftime("%H:%M:%S"))
    print("Good Morning..!!")
elif currentTime > 12 and currentTime < 16:
    print(datetime.datetime.now().strftime("%H:%M:%S"))
    print("Good Afternoon..!!")
elif currentTime > 16 and currentTime < 21:
    print(datetime.datetime.now().strftime("%H:%M:%S"))
    print("Good Evening ..!!")
else:
    print(datetime.datetime.now().strftime("%H:%M:%S"))
    print("Good Night..!!")