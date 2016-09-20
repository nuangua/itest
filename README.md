**itest** is an open source software library for modem automation testing. It targets to provide C/C++/Python API library on Windows, Linux and Mac OS for IoT modems in current market.

Installation
==========================
### For Yotco
* install git, python
* clone codes from github to your home directory

```
# git clone https://github.com/nuangua/itest.git
```
* install module pySerial, psutil

```
# pip install pySerial
# pip install psutil
```
* install lftp

```
# wget http://lftp.yar.ru/ftp/lftp-4.7.3.tar.gz
# tar zxvf lftp-4.7.3.tar.gz
# cd lftp-4.7.3
# ./configure
# make
# make install
```
* install iperf3

```
# git clone https://github.com/esnet/iperf.git
# ./configure
# make
# make install
```

### For Ubuntu
* install git, python
* clone codes from github to your home directory

```
$ git clone https://github.com/nuangua/itest.git
```
* install module pySerial, psutil

```
$ pip install pySerial
$ pip install psutil
```
* install lftp

```
$ sudo apt-get install lftp
```
* install iperf3

```
$ sudo apt-get install iperf3
```
