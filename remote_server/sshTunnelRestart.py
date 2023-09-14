#!/usr/bin/env python3
from datetime import datetime
import os
import subprocess as sp

#check to see if there is a screen named "UbuntuSSHTunnel" and if it does exsit then assign it to the variabel "cutout"
output = sp.getoutput('screen -ls |grep 11869.UbuntuSSHTunnel')
cutout = output[7:22]
#set variable to not connected
status = "not connected"
#open file which says the status of the server
fileS = open("status.txt", "r+")
lines = fileS.readlines()

for x in lines:
    status = x

fileS.close()
#check if the file says connected
if status == "connected":
    print("connected")
    #clear the file so the new status can be written to it
    fileS = open("status.txt", "w")
    fileS.close()
    #clear the reboot.txt file
    filereboot = open("reboot.txt", "w")
    filereboot.close()

#if file does not say connected
else:
    #check to see if the screen "UbuntuSSHTunnel" exsits, if it doesnt
    if cutout != "UbuntuSSHTunnel":
        #open reboot.txt and append i to the file to indicate that the ssh connection failed
        filereboot = open("reboot.txt", "a")
        filereboot.write("i")
        filereboot.close()
        #kill any previous screen with the name newScreen
        os.system("screen -S newScreen -p 0 -X quit")
        #start a new screen
        os.system("screen -d -m -S newScreen")
        print("starting ssh")
        #get the current time and date
        nowint = datetime.now()
        #make the time and date a readable format
        nowstr = nowint.strftime('%Y-%m-%d %I:%M:%S %p')
        #log the time and date and that a new screen needed to be started
        filelog = open("sshTunnelLog.txt", "a")
        filelog.write(nowstr + " NEW SCREEN STARTED!!!\n")
        filelog.close()
        #run the transfer bash file that will transfer the log file to local_server
        os.system("bash logTransfer.sh")
        #start the reverse ssh connection
        os.system("screen -S newScreen -X stuff 'ssh -R 52626:localhost:12626 local_server\\n'")

        #if the screen "UbuntuSSHTunnel" does exsit
    else:
        #open reboot.txt and append i to the file to indicate that the ssh connection failed
        filereboot = open("reboot.txt", "a")
        filereboot.write("i")
        filereboot.close()
        print("starting ssh")
        #get current date and time
        nowint = datetime.now()
        #make date and time into readable format
        nowstr = nowint.strftime('%Y-%m-%d %I:%M:%S %p')
        #log the time and date
        filelog = open("sshTunnelLog.txt", "a")
        filelog.write(nowstr + "\n")
        filelog.close()
        #run the transfer bash file that will transfer the log file to local_server
        os.system("bash logTransfer.sh")
        #start the reverse ssh connection
        os.system("screen -S UbuntuSSHTunnel -X stuff 'ssh -R 42626:localhost:12626 local_server\\n'")
