from datetime import datetime
import time
import random

odds = []
for i in range(60):
    if i%2:
        odds.append(i)
    else:
        continue

for i in range(5):
    
    seconds = random.randint(1,60)

    right_this_minute = datetime.today().minute

    if right_this_minute in odds:
        print  ("This minute seems a little odd")
    else:
        print ("Not an odd minute")

    time.sleep(seconds)
    
