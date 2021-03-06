#!/usr/bin/python

import subprocess
import Log
import ATDevice as ad
import Generic as gen
from ftplib import FTP
import threading
import time
import subprocess

ip='54.223.54.250'
ITEST_CONFIG='/home/root/itest/config/itest.conf'

dlHandler = None
upHandler = None

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

#read ftp account information
def getFtpAccount():
    ftpIp=None
    ftpUsername=None
    ftpPassword=None
    for line in open(ITEST_CONFIG,'r'):
        if 'ftp.ip' in line:
            ftpIp = line.split('=')[1]
            continue
        if 'ftp.username' in line:
            ftpUsername = line.split('=')[1]
            continue
        if 'ftp.password' in line:
            ftpPassword = line.split('=')[1]
            continue
    return ftpIp,ftpUsername,ftpPassword


#connect to ftp server
def ftpConnect():
    ftp_ip,ftp_username,ftp_password = getFtpAccount()
    Log.debug('ftp_ip='+ftp_ip)
    ftp = FTP()
    ftp.set_debuglevel(2)
    ftp.connect(ftp_ip,21)
    ftp.login(ftp_username,ftp_password)
    return ftp

#ftp download
def ftpDownload():
    ftp = ftpConnect()
    Log.info(ftp.getwelcome())
    remotepath="/download/100_MBytes.txt"
    localpath="/home/root/itest/config/ftp/100_MBytes.txt"
    bufsize=1024
    fp=open(localpath,'wb')
    ftp.retrbinary('RETR '+remotepath,fp.write,bufsize)
    ftp.set_debuglevel(0)
    fp.close()
    ftp.quit()

def ftpDownloadThread():
    dlHandler = threading.Thread(target=ftpDownload,args=())
    dlHandler.setDaemon(True)
    dlHandler.start()

def ftpDownloadThreadStop():
    dlHandler.stop()

#ftp upload
def ftpUpload():
    ftp = ftpConnect()
    Log.info(ftp.getwelcome())
    remotepath="/upload/100_MBytes.txt"
    localpath="/home/root/itest/config/ftp/100_MBytes.txt"
    bufsize=1024
    fp=open(localpath,'rb')
    ftp.storbinary('STOR '+remotepath,fp,bufsize)
    ftp.set_debuglevel(0)
    fp.close()
    ftp.quit()

def ftpUploadThread():
    ulHandler = threading.Thread(target=ftpUpload,args=())
    ulHandler.setDaemon(True)
    ulHandler.start()

def ftpUploadThreadStop():
    ulHandler.stop()

if  __name__=="__main__":
    ad.openDefaultSerialPort()
    gen.startWiresharkTraceThread('/home/root/itest/logs/ftp.cap')
    ad.detachDev()
    ad.attachDev('SM_4G')
    ad.activatePdpContext()
    if isAlive(0.8)== True:
        Log.debug('network connection is alive')
        ftpDownloadThread()
        ftpUploadThread()
    else:
        Log.debug('network connection is dead')
    time.sleep(5)
    startTime = time.time()
    endTime = time.time()
    waitTime = 60
    while (endTime - startTime) <= waitTime:
        Log.info('ftp downloading and uploading...')
        time.sleep(5)
        endTime = time.time()
    Log.debug('killing ftp thread...')
    #ftpDownloadThreadStop()
    #ftpUploadThreadStop()
    gen.stopWiresharkTrace()
