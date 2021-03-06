#!/usr/bin/python

import time
import Log
import ATDevice as ad
import Generic as gen
import Call

if __name__ == "__main__":
    Log.debug("start call")
    ad.openDefaultSerialPort()
    gen.startWiresharkTraceThread('/home/root/itest/logs/call.cap')
    time.sleep(5)
    ad.detachDev()
    Call.startMOCall('+8613121549945')
    time.sleep(3)
    while Call.checkCallStatus() != '0':
        Log.debug('call not pick up, check again after 5 seconds')
        time.sleep(3)
    startTime = time.time()
    endTime = time.time()
    waitTime = 60
    while (endTime - startTime) <= waitTime:
        Log.info('calling...')
        Call.checkCallStatus()
        time.sleep(5)
        endTime = time.time()
    Call.stopCall()
    gen.stopWiresharkTrace()
