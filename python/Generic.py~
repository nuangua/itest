#!/usr/bin/python

import Log
import ATDevice as ad
import threading
import subprocess

#initilize device
def initDev():
    Log.debug("check attach status...")
    if ad.isAttached():
        ad.detachDev()
        Log.info("detach device done")
    Log.info("list network card names")
    if ad.listNetCards():
        Log.info("list network card names done")

#start capturing wireshark traces
def startWiresharkTrace(_tracePath):
    Log.debug('entering start wireshark trace')
    subprocess.call('tcpdump -i wwp0s17u1i6 -w '+_tracePath, shell=True)

def startWiresharkTraceThread(_tracepath):
    instance = threading.Thread(target=startWiresharkTrace,args=(_tracepath,))
    instance.setDaemon(True)
    instance.start()
    Log.debug('start new thread for capturing wireshark trace')

#stop capturing wireshark traces
def stopWiresharkTrace():
    subprocess.call('killall -9 tcpdump', shell=True)

