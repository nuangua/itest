#!/usr/bin/python

import subprocess
import Log as log
import ATDevice as ad
from ftplib import FTP

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
    log.debug(counter)
    if (counter/5) < percent:
        return False
    else:
        return True

#read ftp account information
def getFtpAccount():
    ftpIp=None
    ftpUsername=None
    ftpPassword=None
    for line in open('../config/itest.conf','r'):
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
    log.debug('ftp_ip='+ftp_ip)
    ftp = FTP()
    ftp.set_debuglevel(2)
    ftp.connect(ftp_ip,21)
    ftp.login(ftp_username,ftp_password)
    return ftp

#ftp download
def ftpDownload():
    ftp = ftpConnect()
    log.info(ftp.getwelcome())
    remotepath="/download/100_MBytes.txt"
    localpath="../config/ftp/100_MBytes.txt"
    bufsize=1024
    fp=open(localpath,'wb')
    ftp.retrbinary('RETR '+remotepath,fp.write,bufsize)
    ftp.set_debuglevel(0)
    fp.close()
    ftp.quit()

#ftp upload
def ftpUpload():
    ftp = ftpConnect()
    log.info(ftp.getwelcome())
    remotepath="/upload/100_MBytes.txt"
    localpath="../config/ftp/100_MBytes.txt"
    bufsize=1024
    fp=open(localpath,'rb')
    ftp.storbinary('STOR '+remotepath,fp,bufsize)
    ftp.set_debuglevel(0)
    fp.close()
    ftp.quit()

if  __name__=="__main__":
    ad.openDefaultSerialPort()
    ad.detachDev()
    ad.attachDev('SM_4G')
    ad.activatePdpContext()
    if isAlive(0.8)== True:
        log.debug('network connection is alive')
        #ftpDownload()
        ftpUpload()
    else:
        log.debug('network connection is dead')
