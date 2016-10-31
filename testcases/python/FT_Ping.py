#!/usr/bin/python

import Ping
import Log
import ATDevice as ad
import Generic as gen
import time

if __name__=="__main__":
    ad.openDefaultSerialPort()
    gen.startWiresharkTraceThread('/home/root/itest/logs/ping.cap')
    time.sleep(5)
    ad.detachDev()
    ad.attachDefaultDev()
    ad.activatePdpContext()
    status,percent = Ping.startPing(30)
    gen.stopWiresharkTrace()
    Log.debug('status='+str(status)+',percentage='+str(percent*100)+'%')
