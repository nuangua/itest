#!/usr/bin/python

import time
import Log
import ATDevice as ad
import Generic as gen

#start MO call
def startMOCall(_simNo):
    rat = "DM_3G"
    if ad.attachDev(rat)== False:
        Log.debug("attach to "+rat+" failed")
        return False
    output, flag = ad.waitAT('ATD'+_simNo+';','OK',ad.WAIT_TIME)
    return flag

#check Call status
def checkCallStatus():
    output, flag = ad.waitAT('AT+CLCC','OK', ad.WAIT_TIME)
    if ',' not in output:
        return -1
    out_list = output.split(',')
    Log.debug('return: '+out_list[2].strip())
    return out_list[2].strip()

def stopCall():
    output,flag= ad.waitAT('ATH','OK',ad.WAIT_TIME)
    checkCallStatus()
    return flag

if __name__ == "__main__":
    Log.debug("start call")
    ad.openDefaultSerialPort()
    gen.startWiresharkTraceThread('/home/root/itest/logs/call.cap')
    ad.detachDev()
    #Log.debug(ad.listNetCards())
    startMOCall('+8613121549945')
    time.sleep(5)
    while checkCallStatus() != '0':
        Log.debug('call not pick up, check again after 5 seconds')
        time.sleep(5)
    startTime = time.time()
    endTime = time.time()
    waitTime = 60
    while (endTime - startTime) <= waitTime:
        Log.info('calling...')
        checkCallStatus()
        time.sleep(5)
        endTime = time.time()
    stopCall()
    gen.stopWiresharkTrace()
