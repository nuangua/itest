#include <LED.h>

LED led(6);

void setup()
{
	Serial.begin(9600);
}

void loop()
{
	led.reverse();
	delay(1000);
	Serial.print(" LED status is: ");
	Serial.println(led.status());
}
