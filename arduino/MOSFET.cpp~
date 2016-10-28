/*
 * Copyright (c) 2016 Intel Corporation.  All rights reserved.
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.

 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.

 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
 *
 */

#include "Arduino.h"
#include "LED.h"

LED::LED(int pin)
{
	_pin = pin;	
	pinMode(_pin, OUTPUT);
}

void LED::on()
{
	digitalWrite(_pin, HIGH);
}

void LED::off()
{
	digitalWrite(_pin, LOW);
}

boolean LED::isOn()
{
	if (HIGH == status())
	{
		return true;
	}
	return false;
}

boolean LED::isOff()
{
	if (LOW == status())
	{
		return true;
	}
	return false;
}

void LED::reverse()
{
	if(isOn())
	{
		off();	
	} else
	{
		on();
	}	
}

int LED::status()
{
	return digitalRead(_pin);
}

