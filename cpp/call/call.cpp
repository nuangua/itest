#include <stdio.h>
#include "../include/call.h"
#include "../include/bool.h"

Call::Call()
{
	printf("entering call constructor\n");
}
Call::~Call()
{

}

int Call::makeCall(char* simNum)
{
	at.waitAt("AT+CLCC", "OK", 10);
	return FALSE;
}

int Call::answerCall()
{
	return FALSE;
}
int Call::checkStatus()
{
	return FALSE;
}
int Call::endCall()
{
	return FALSE;
}
