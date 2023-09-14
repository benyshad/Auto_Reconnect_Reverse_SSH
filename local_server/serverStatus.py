#!/usr/bin/env python3

#this python script is run via the reverse ssh connection that should already be established
#if the reverse connection is working properly then this script will be run and write connected if the
#"status.txt" which will be read by the script "sshTunnelRestart.py"
fileS = open("status.txt", "w")
fileS.write("connected")
fileS.close()
