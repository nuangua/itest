#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "../include/at.h"
#include "../include/usb.h"
#include "../include/bool.h"

At::At()
{
	//TODO
	com.openCom("/dev/ttyACM0");
	com.setCom(115200, 0, 8, 1, 'N');
}

At::At(char port[])
{
	com.openCom(port);
	com.setCom(115200, 0, 8, 1, 'N');
}

int At::waitAt(char atCmd[], char waitStr[], int waitTime)
{
	char output[512];
	com.writeCom(atCmd, sizeof(atCmd));
	usleep(100);
	com.readCom(output, sizeof(output));
	return TRUE;
}

At::~At()
{
	com.closeCom();
}
