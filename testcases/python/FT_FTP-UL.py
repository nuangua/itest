#!/usr/bin/python

import time
import FTP
import Log
import ATDevice as ad
import Generic as gen


if  __name__=="__main__":
    ad.openDefaultSerialPort()
    gen.startWiresharkTraceThread('/home/root/itest/logs/ftp.cap')
    ad.detachDev()
    ad.attachDev('SM_4G')
    ad.activatePdpContext()

    Log.debug('start ftp uploading')
    FTP.ftpUploadThread()
    startTime = time.time()
    endTime = time.time()
    waitTime = 60
    while (endTime - startTime) <= waitTime:
        Log.info('ftp uploading...')
        time.sleep(5)
        endTime = time.time()
    Log.debug('killing ftp thread...')
    #ftpDownloadThreadStop()
    #ftpUploadThreadStop()
    gen.stopWiresharkTrace()
