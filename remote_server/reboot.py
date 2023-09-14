#!/usr/bin/env python3

from datetime import datetime
import os
import subprocess as sp


reboot = "r"
reboot = sp.getoutput("cat /home/pi/reboot.txt")


if reboot=="iiii":
    #get the current time and date
    nowint = datetime.now()
    #make the time and date a readable format
    nowstr = nowint.strftime('%Y-%m-%d %I:%M:%S %p')
    #log the time and date annd that the pi is rebooting
    filelog = open("/home/pi/sshTunnelLog.txt", "a")
    filelog.write(nowstr + " REBOOTING!!!\n")
    filelog.close()
    #run the transfer bash file that will transfer the log file to shadownet
    os.system("bash /home/pi/logTransfer.sh")
    filereboot = open("/home/pi/reboot.txt", "w")
    filereboot.close()
    os.system("reboot now")

else:
    print(reboot)
