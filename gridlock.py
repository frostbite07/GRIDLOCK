import tkinter as tk
from tkinter import *
import os
import subprocess
import time
import threading
import multiprocessing
from subprocess import check_call
from wireless import Wireless
from ARPPoise import *
from wifite import *
from Deauth import *
from MacSpoofing import *
from PixieDust import *
from pingsweeper import *
from portsniffer import *
from evaluation import *

def display_evaluation(s):
    topFrame.destroy()
    topFrame2 = tk.Frame(root, bg="#202020")
    topFrame2.place(rely=0.15, relwidth=1, relheight = 0.65)
    score_banner = "GRIDLOCK Score for " + enter_ssid.get() + ":\n\n" + str(s) +" / 5"
    Label(topFrame2, text=score_banner,pady=120, anchor=CENTER, bg="#202020", fg="#0095FF" , font="noah 15 bold").pack()
    root.update()

def prime():
    ######## Evaluation Variables Initialization ########
    atk1 = atk2 = atk3 = atk4 = atk5 = 0

    ######## Setting up adapters ########
    Label(topFrame, text="Scanning Hardware for Wireless Adapters...", bg="#202020", fg="#FFFFFF").pack()
    os.system("ip a")
    root.update()
    time.sleep(2)
    Label(topFrame, text="Set Up Wireless Adapter wlan0", bg="#202020", fg="#FFFFFF").pack()
    root.update()
    time.sleep(1)
    ssid_mock = "Running test on " + enter_ssid.get()
    Label(topFrame, text=ssid_mock, bg="#202020", fg="#FFFFFF").pack()
    root.update()
    time.sleep(1)

    ######## Attack 1 : MAC #########
    Label(topFrame, text="Attempting MAC Spoofing...", bg="#202020", fg="#FFFFFF").pack()
    atkthread = multiprocessing.Process(target=macspoofing)
    atkthread.start()
    root.update()    
    if  atkthread.is_alive():
        atk1=1
        atkthread.join()
        Label(topFrame, text="MAC Spoofing Successful", bg="#202020", fg="#02FF70").pack()
    else:
        Label(topFrame, text="MAC Spoofing Failed", bg="#202020", fg="#FF0040").pack()
    time.sleep(1)

    ######## Attack 2 : ARP #########
    Label(topFrame, text="Attempting ARP Poisoning", bg="#202020", fg="#FFFFFF").pack()
    atkthread = multiprocessing.Process(target=arp)
    atkthread.start()
    root.update()    
    if  atkthread.is_alive():
        atk2=1
        atkthread.join()
        Label(topFrame, text="ARP Poisoning Successful", bg="#202020", fg="#02FF70").pack()
    else:
        Label(topFrame, text="ARP Poisoning Failed", bg="#202020", fg="#FF0040").pack()
    time.sleep(1)

    ######## Attack 5 : PixieDust #########
    Label(topFrame, text="Attempting PixieDust Attack", bg="#202020", fg="#FFFFFF").pack()
    atkthread = multiprocessing.Process(target=pixie)
    atkthread.start()
    root.update()    
    if  0 and atkthread.is_alive():
        atk5=1
        atkthread.join()
        Label(topFrame, text="PixieDust Successful", bg="#202020", fg="#02FF70").pack()
    else:
        atkthread.join()
        Label(topFrame, text="PixieDust Failed", bg="#202020", fg="#FF0040").pack()
    root.update() 
    time.sleep(1)   

    ######## Change Interface Mode ########
    Label(topFrame, text="Putting wireless interface wlan0 in Monitor mode", bg="#202020", fg="#FFFFFF").pack()
    order = "sudo airmon-ng start wlan0 && sudo airmon-ng check kill"
    os.system(order)    
    root.update()
    time.sleep(2)


    ######## Attack 4 : Deauth #########
    Label(topFrame, text="Attempting Deauthentication", bg="#202020", fg="#FFFFFF").pack()
    root.update()   
    atkthread = multiprocessing.Process(target=deauth)
    atkthread.start()    
    if  atk4 == 0:
        atk4=1
        atkthread.join()
        Label(topFrame, text="All Clients kicked off the Access Point", bg="#202020", fg="#02FF70").pack()
    else:
        Label(topFrame, text="Deauthentication Failed", bg="#202020", fg="#FF0040").pack()
    root.update()
    time.sleep(1)
       
    ######## Attack 5 : Wifite #########
    Label(topFrame, text="Attempting WPA2 cracking", bg="#202020", fg="#FFFFFF").pack()
    root.update()
    order = "sudo airmon-ng start wlan0 && sudo airmon-ng check kill"
    os.system(order)
    var = portsniffer_gg()
    atkthread = multiprocessing.Process(target=crack)
    atkthread.start() 
    # cmd = os.system("wifite")
    if  var == 1:
        atk5=1
        atkthread.join()
        Label(topFrame, text="Cracking Successful", bg="#202020", fg="#02FF70").pack()
    else:
        Label(topFrame, text="Cracking Failed", bg="#202020", fg="#FF0040").pack()

    root.update()
    

    ######## Change Interface Mode ########

    Label(topFrame, text="Resetting Wireless Network Defaults", bg="#202020", fg="#FFFFFF").pack()
    root.update()
    order = "sudo airmon-ng stop wlan0mon && sudo service network-manager restart"
    os.system(order)
    time.sleep(5)
    os.system("nmcli d wifi connect Frosty password bisaat1853# ifname wlan0") 
    
    ######## Evaluation ########
    Label(topFrame, text="Starting Evaluation", bg="#202020", fg="#0095FF").pack()    
    score = evaluate_score(atk1,atk2,atk3,atk4,atk5)
    root.update()
    time.sleep(4)    
    display_evaluation(score)

    
root = tk.Tk()
root.title("GRIDLOCK")


canvas = tk.Canvas(root, height=600, width =850, bg ="#202020") 
canvas.pack()

#frame = tk.Frame(root, bg="white");
#frame.place(relwidth=0.8, relheight = 0.8, relx=0.1, rely=0.1)
header = tk.Frame(root, bg="#202020")
header.place(relwidth=1,relheight=0.15)
Label(header, text="Welcome to GRIDLOCK", pady=25, anchor=CENTER, bg="#202020", fg="#FFFFFF" , font="noah 18 ").pack()

topFrame = tk.Frame(root, bg="#202020")
topFrame.place(rely=0.15, relwidth=1, relheight = 0.65)

bottomFrame = tk.Frame(root, bg="#202020")
bottomFrame.place(rely=0.80, relwidth=1, relheight = 0.20)

enter_ssid = Entry(bottomFrame, width=50, bg="#FFFFFF")
enter_ssid.pack()
enter_ssid.insert(0, "Enter Network Name")

launch = tk.Button(bottomFrame, text="Launch GRIDLOCK", bg="white", fg="#202020", font="noah 10 bold", command=prime)
launch.place(in_=bottomFrame, rely=0.5, relx=0.5, anchor=CENTER)



root.mainloop()