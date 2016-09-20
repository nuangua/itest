#include <MOSFET.h>

MOSFET mosfet(6);

void setup()
{
	Serial.begin(9600);
}

void loop()
{
	mosfet.reverse();
	delay(3000);
	Serial.print(" MOSFET status is: ");
	Serial.println(mosfet.status());
}
