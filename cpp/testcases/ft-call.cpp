#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "../include/call.h"

int main()
{
	Call call;
	call.makeCall("+8613121549945");
	return 0;
}
