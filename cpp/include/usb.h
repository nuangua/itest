#ifndef _COM_H_
#define _COM_H_

class Com
{
public:
	virtual ~Com();
	int openCom(char* port);
	int setCom(int baud, int flow, int dataBit, int stopBit, int parity);
	int writeCom(char* buf, int len);
	int readCom(char* buf, int len);
	void closeCom();
private:
	int fd;
	char* serialport;
	int baud;
	int flow;
	int dataBit;
	char parity;
	int stopBit;
	char* writeBuf;
	char* readBuf;
};
#endif
