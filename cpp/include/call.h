#include "../include/at.h"
#include "../include/bool.h"

class Call
{
private:
	At at;
	char* from;
	char* to;
public:
	Call();
	virtual ~Call();
	int makeCall(char* simNum);
	int answerCall();
	int checkStatus();
	int endCall();
};
