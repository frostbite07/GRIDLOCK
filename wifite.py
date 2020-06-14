import os
import subprocess as sub
import time
from subprocess import check_call

def crack():
    print()
    order = "sudo aircrack-ng -a2 -b F4:F2:6D:3C:40:92 -w /frostbite/Desktop/MinorProject/Code/capture/dict.txt /frostbite/Desktop/MinorProject/Code/capture/key.cap"
    os.system(order)
    #os.system("airodump-ng -c 6 — bssid 9C:5C:8E:C9:AB:C0 -w ./capture/ wlan0mon")
