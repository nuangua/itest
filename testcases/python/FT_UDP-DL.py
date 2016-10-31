#!/usr/bin/python

import time
import Log as log
import ATDevice as ad
import Generic as gen
import UDP

if __name__=="__main__":
    ad.openDefaultSerialPort()
    ad.detachDev()
    ad.attachDev('TM_4G')
    ad.activatePdpContext()
    gen.startWiresharkTraceThread('/home/root/itest/logs/udp.cap')
    UDP.udpDownload()
    gen.stopWiresharkTrace()
