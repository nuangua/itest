#!/usr/bin/python

import Log as log
import ATDevice as ad
import threading
import subprocess

#initilize device
def initDev():
    log.debug("check attach status...")
    if ad.isAttached():
        ad.detachDev()
        log.info("detach device done")
    log.info("list network card names")
    if ad.listNetCards():
        log.info("list network card names done")

#start capturing wireshark traces
def startWiresharkTrace(_tracePath):
    log.debug('entering start wireshark trace')
    subprocess.call('tcpdump -i wwp0s17u1i6 -w '+_tracePath, shell=True)

def threadStartWiresharkTrace(_tracepath):
    instance = threading.Thread(target=startWiresharkTrace,args=(_tracepath,))
    instance.setDaemon(True)
    instance.start()
    log.debug('start new thread for capturing wireshark trace')

#stop capturing wireshark traces
def stopWiresharkTrace():
    subprocess.call('killall -9 tcpdump', shell=True)

