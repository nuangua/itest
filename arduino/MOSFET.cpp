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
#include "MOSFET.h"

MOSFET::MOSFET(int pin)
{
	_pin = pin;	
	pinMode(_pin, OUTPUT);
}

void MOSFET::on()
{
	digitalWrite(_pin, HIGH);
}

void MOSFET::off()
{
	digitalWrite(_pin, LOW);
}

boolean MOSFET::isOn()
{
	if (HIGH == status())
	{
		return true;
	}
	return false;
}

boolean MOSFET::isOff()
{
	if (LOW == status())
	{
		return true;
	}
	return false;
}

void MOSFET::reverse()
{
	if(isOn())
	{
		off();	
	} else
	{
		on();
	}	
}

int MOSFET::status()
{
	return digitalRead(_pin);
}

