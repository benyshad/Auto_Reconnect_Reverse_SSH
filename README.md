# Auto Reconnect Reverse SSH Shell



## Description

This project was designed to maintain a constant connection between 2 servers where the remote server was not capable of using port forwarding. 
Therefore a reverse ssh shell was needed to be created on the remote server.
The issue was, the reverse shell would fail from time to time and would have to be reconnected.
I created a simple but very helpful python and bash script that would check the reverse connection and if it was down it would attempt to reconnect, logging each time it the reverse shell needed to be restarted and transferring the log to the local server when the connection was re-established.
On occasions the reverse shell would fail to restart, after 4 failed attempts to reconnect the remote server would automatically restart and log that a restart was required. 

## Usage
crontab was used to run the script that would check the connection and reconnect if need be
```bash
crontab -e 
```
