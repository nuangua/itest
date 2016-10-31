#!/usr/bin/python
import ATDevice as ad

if __name__=="__main__":
    ad.openDefaultSerialPort()
    ad.detachDev()
    ad.attachDev('TM_4G')
    ad.sendSMS('TEST123')
