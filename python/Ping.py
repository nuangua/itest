#!/usr/bin/python

import subprocess
import Log
import ATDevice as ad

ip='54.223.54.250'
#to test if network connection is alive
def isAlive(percent):
    counter=0
    subp = subprocess.Popen('ping -c 5 '+ip,shell=True,stdout=subprocess.PIPE)
    while subp.poll()==None:
        line = subp.stdout.readline()
        print line
        if 'bytes from '+ip in line:
            counter = counter+1
    Log.debug(counter)
    if (counter/5) < percent:
        return False
    else:
        return True

def startPing(_pingTime):
    counter=0
    subp = subprocess.Popen('ping -c '+ str(_pingTime)+ ' ' + ip, shell=True, stdout=subprocess.PIPE)
    while subp.poll()==None:
        line = subp.stdout.readline()
        print line
        if 'bytes from '+ip in line:
            counter = counter +1
    Log.debug(counter)
    return subp.returncode,counter/_pingTime

def stopPing():
    return False

if __name__=="__main__":
    ad.openDefaultSerialPort()
    ad.detachDev()
    ad.attachDefaultDev()
    ad.activatePdpContext()
    #Log.debug(isAlive())
    status,percent = startPing(30)
    Log.debug('status='+str(status)+',percentage='+str(percent*100)+'%')
