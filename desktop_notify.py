import time 
from  plyer import notification

if __name__=="__main__":
    while True:
        notification.notify(title="ALERT!!!",message="Testing notification",timeout=10)
        time.sleep(2000)

