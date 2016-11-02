#ifndef _AT_H_
#define	_AT_H_
#include "../include/usb.h"

class At
{
public:
	At();
	At(char* port);
	~At();
	int waitAt(char* atCmd, char* waitStr, int waitTime);
private:
	Com com;
};
#endif
