#include "../include/Com.h"
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define	FALSE	-1
#define	TRUE	0

int main()
{
	Com com;
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
	return 0;
}
