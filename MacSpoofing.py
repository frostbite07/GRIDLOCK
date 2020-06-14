import os
import subprocess
import time
from subprocess import check_call

def macspoofing():
    print("Attempting Mac Spoofing...")
    time.sleep(10)
    #os.system("macchanger -s wlan0")
    os.system("ip link set dev wlan0 down")

    order = "sudo macchanger -r wlan0"
    geny  = os.system(order)

    os.system("ip link set dev wlan0 up")
    #os.system("macchanger -s wlan0")
    time.sleep(2)
    
    return 1   
