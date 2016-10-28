#!/usr/bin/python

import subprocess
import commands
import serial
import re
import time
import logging
import logging.config
#import Log
import psutil
import sys

logging.config.fileConfig(sys.path[0] + "/../config/logging.conf")
logger = logging.getLogger("itest")

#serial port config
usbdevice = None
baud = 9600
serialport = None

WAIT_SHORT_TIME = 5
WAIT_TIME = 20
WAIT_LONG_TIME = 60

#Open default serial port
def openDefaultSerialPort():
    global serialport

    openSerialPort('/dev/ttyACM0')
    if serialport != None:
        return True
    else:
        return False

#Open serial port
def openSerialPort(_port):
    global serialport
    closeSerialPort()

    device = usbdevice
    if not device:
        devicelist = commands.getoutput("ls " + _port)
        if devicelist[0] == '/':
            device = devicelist
    if not device:
        logger.debug("Waiting for device...")
        return False
    logger.debug("Connecting to " + device + "...")
    serialport = serial.Serial(device, baud, timeout=0, stopbits=serial.STOPBITS_TWO)
    logger.debug('Opened port: ' + serialport.portstr)
    return True

#Close serial port
def closeSerialPort():
    global serialPort
    if serialport and serialport.isOpen():
        logger.debug("Closing: " + serialport.portstr)
        serialport.close()

#send at command and wait the response in waitting time
def waitAT(_atCommand, _response, _waitTime):
    global serialport
    matched = None
    output = None
    if serialport == None:
        logger.debug("Serial port is not available. Please check serial port.")
        return None, False
    else:
        serialport.write(_atCommand + '\r')
    logger.debug(_atCommand)
    startTime = time.time()
    endTime = time.time()
    while (endTime - startTime) <= _waitTime:
        output = serialport.read(serialport.inWaiting())
        if _response in output:
            break
        else:
            time.sleep(1)
            endTime = time.time()
    if output == None:
        logger.debug('Timeout...')
        return output, False
    matched = re.search(_response, output)
    logger.debug(output)
    if matched != None:
        return output, True
    else:
        return output, False

#attach device to TM_4G as default
def attachDefaultDev():
    return attachDev('SM_4G')

#attach device to a specific rat
def attachDev(ratSetting):
    ratFlag = False
    if "SM_2G" in ratSetting:
        output,ratFlag = waitAT('AT+XACT=0', 'OK', WAIT_TIME)
    elif "SM_3G" in ratSetting:
        output,ratFlag = waitAT('AT+XACT=1', 'OK', WAIT_TIME)
    elif "SM_4G" in ratSetting:
        output,ratFlag = waitAT('AT+XACT=2', 'OK', WAIT_TIME)
    elif "DM_3G" in ratSetting:
        output,ratFlag = waitAT('AT+XACT=3,1', 'OK', WAIT_TIME)
    elif "DM_4G" in ratSetting:
        output,ratFlag = waitAT('AT+XACT=4,2', 'OK', WAIT_TIME)
    elif "TM_4G" in ratSetting:
        output,ratFlag = waitAT('AT+XACT=6,2,1', 'OK', WAIT_TIME)
    else:
        logger.debug('The specific rat is error. Please input the correct one, for example, SM_2G/SM_3G/SM_4G/DM_3G/DM_4G/TM_4G.')
        return False
    if ratFlag == False:
        logger.debug("Select rat failed.")
        return False
    output, flag = waitAT('AT+COPS=0', 'OK', WAIT_TIME)
    return flag

#detach device to ide status
def detachDev():
    waitAT('AT+COPS=2', 'OK', WAIT_TIME)

#return attached status
def isAttached():
    output, flag = waitAT('AT+COPS?', 'OK', WAIT_TIME)
    if flag == False:
        return False
    else:
        if '"CHINA MOBILE"' in output:
            return True
        elif '"CHN-UNICOM"' in output:
            return True

#
def activatePdpContext():
    ip_addr = "255.255.255.255"
    dns = None
    apn = None
    ipList = []
    apnList = []
    dnsList = []

    if isAttached() == False:
        attachDefaultDev()
    if isAttached():
        #waitAT('AT+CFUN=1', 'OK',WAIT_TIME)
        waitAT('AT+CGDCONT=1,"IP","3gnet"','OK',WAIT_TIME)
        waitAT('AT+XDNS=1,1', 'OK', WAIT_TIME)
        waitAT('AT+XDATACHANNEL=1,1,"/USBCDC/0","/USBHS/NCM/0",2,1', 'OK', WAIT_TIME)

        waitAT('AT+COPS=0', 'OK', WAIT_TIME)
        waitAT('AT+COPS?', 'OK', WAIT_TIME)
        waitAT('AT+CGACT=1,1', 'OK', WAIT_TIME)
        output,flag = waitAT('AT+CGDCONT?', 'OK', WAIT_TIME)
        if flag:
            ip_addr = output.split('\n')
            for ip in ip_addr:
                if '+CGDCONT:' in ip:
                    ip_list = ip.split(',')
                    apnList.append(ip_list[2])
                    ipList.append(ip_list[3])
        output,flag = waitAT('AT+XDNS?', 'OK', WAIT_TIME)
        if flag:
            dns = output.split('\n')
            for it in dns:
                if '+XDNS:' in it:
                    dns_ip = it.strip().replace('\r','').replace('"','').split(',')
                    dnsList.append(dns_ip[1].strip())
                    dnsList.append(dns_ip[2].strip())
        waitAT('AT+CGDATA="M-RAW_IP",1', 'CONNECT',WAIT_TIME)
        ip_addr = ipList[1]
        apn = apnList[1]

        interfaceName=None
        for item in listNetCards():
            logger.debug(item)
            if 'p0s17u1i6' in item:
                interfaceName = item
                break
        logger.debug('interface name: ' + interfaceName)
        subprocess.call('ifconfig ' + interfaceName + ' down', shell=True)
        subprocess.call('ifconfig ' + interfaceName + ' ' + ip_addr, shell=True)
        subprocess.call('ifconfig ' + interfaceName + ' up', shell=True)
        subprocess.call('ifconfig ' + interfaceName + ' -arp', shell=True)
        subprocess.call('route add default gw ' + ip_addr + ' ' + interfaceName, shell=True)
        for nameserver in dnsList:
            subprocess.call('echo "nameserver ' + nameserver + '" >> /etc/resolv.conf', shell=True)
        logger.debug('ifconfig configuration list:')
        subprocess.call('ifconfig', shell=True)
        logger.debug('route table:')
        subprocess.call('route', shell=True)
        logger.debug('DNS configuration:')
        subprocess.call('cat /etc/resolv.conf', shell=True)
        logger.debug('ping server 54.223.54.250:')
        subprocess.call('ping -c 5 54.223.54.250', shell=True)

#list network card names
def listNetCards():
    netcardList=[]
    info = psutil.net_if_addrs()
    for key,value in info.items():
        netcardList.append(key)
    return netcardList

if __name__ == '__main__':
    openDefaultSerialPort()
    detachDev()
    attachDefaultDev()
    activatePdpContext()
    logger.debug(listNetCards())
