#include <Relay.h>

Relay relay(6);

void setup()
{
	Serial.begin(9600);
}

void loop()
{
	relay.reverse();
	delay(3000);
	Serial.print(" Relay status is: ");
	Serial.println(relay.status());
}
