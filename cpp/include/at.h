#ifndef _AT_H_
#define	_AT_H_
#include "../include/usb.h"

class At
{
public:
	At();
	At(char port[]);
	virtual ~At();
	int waitAt(char atCmd[], char waitStr[], int waitTime);
private:
	Com com;
};
#endif
