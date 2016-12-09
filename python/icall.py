#!/usr/bin/python

import psutil
import os
import commands
import time
import Log
import ATDevice as device
import Ping as ping
import Call as call

usbList=[]
interfaceList=[]
modemList=[]
modemDict={}
portList=[]

def init():
	#getUsbDevicesList()
	#getNetworkInterfacesList()
	getModemInterfacesList()
	getModemDict()
	#getACMPortsList()

def getUsbDevicesList():
	(status, output) = commands.getstatusoutput('lsusb|grep "Intel Corp"')
	for item in output.split('\n'):
		usbList.append(item)
	return usbList

def getNetworkInterfacesList():
	info = psutil.net_if_addrs()
	for key,value in info.items():
		#Log.debug("key:"+key+', value:'+value)
		interfaceList.append(key)
	return interfaceList

def getModemInterfacesList():
	(status, output) = commands.getstatusoutput('ifconfig -a|grep "HWaddr 00:00:11:12:13:14"')
	for item in output.split('\n'):
		modemList.append(item.split()[0])
	return modemList

def getModemDict():
	for item in modemList:
		modemDict[item.replace('usb','/dev/ttyACM')] = item
	return modemDict

def getACMPortsList():
	(status, output) = commands.getstatusoutput('ls /dev/ttyACM*')
	Log.debug("status="+status)
	Log.debug("output="+output)
	for item in output.split('\n'):
		portList.append(item)
	Log.debug(type(portList))
	return portList

def publishSimStatus(statusDict):
	Log.debug("Sim Status:\n"+str(statusDict))
	for key,value in statusDict.items():
		(status,output) = commands.getstatusoutput('mosquitto_pub -h 54.223.54.250 -p 5101 -t "iot\devices\sim\\'+key+'" -m "'+value+'" -q 2')
		Log.debug('publish message "'+value+'" to topic "iot\devices\sim\\'+ key+' "  done.')

if __name__=='__main__':
	#init()
	#Log.debug(usbList)
	#Log.debug(interfaceList)
	#Log.debug(modemList)
	#Log.debug(portList)
	Log.debug(modemDict)
	startTime = time.time()
	endTime = time.time()
	intervalTime = 300
	isAlived = False
	while 1:
		init()
		for port,interface in modemDict.items():
			device.openSerialPort(port)
			#call.startMOCall('10086')
			if device.isAttached() == False:
				device.attachDev('TM_4G')
			#Log.debug("SIM Status:\n"+str(device.getSimStatus()))
			publishSimStatus(device.getSimStatus())
			#device.activatePdpContextWith(interface)
			"""if os.path.exists(port):
				device.openSerialPort(port)
				device.attachDev('TM_4G')
				if (endTime - startTime) > intervalTime or isAlived == False:
					if ping.isAlive(0.8) == False:
						device.activatePdpContextWith(interface)
					if ping.isAlive(0.8) == True:
						isAlived = True
					else:
						isAlived = False
					startTime = endTime
					endTime = time.time()"""
				#device.waitAT('AT','OK', device.WAIT_TIME)
			device.closeSerialPort()
		time.sleep(10)
