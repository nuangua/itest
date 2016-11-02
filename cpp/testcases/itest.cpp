#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "../include/at.h"

int main()
{

/**	Com com;
	char port[] = "/dev/ttyACM0";
	com.openCom(port);
	//printf("open com port is %i\n", oc);
	int ret = com.setCom(115200, 0, 8, 1, 'N');
	if(FALSE == ret)
	{
		printf("set port error\n");
		exit(1);
	}
	char wBuf[]="AT+COPS?\r", rBuf[255];
	com.writeCom(wBuf, sizeof(wBuf));
	usleep(100);
	com.readCom(rBuf, sizeof(rBuf));
	com.closeCom();
  */
	char port[] = "/dev/ttyACM0";
	char atCmd[] = "AT\r";
	char waitStr[] = "OK";
	At at(port);
	at.waitAt(atCmd, waitStr, 10);
	return 0;
}
