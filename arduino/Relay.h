/*
 * Relay library for Grove Relay v1.2.
 *
 * Copyright (c) 2016 Intel Corporation.  All rights reserved.
 *
 * Author: David Gu
 * 2016-09-08
 * Email: nuanguang.gu@intel.com 
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

#ifndef _RELAY_H_
#define _RELAY_H_
#include "Arduino.h"


/* Note that this MOSFET provides interface functions to help you better control and manage
 * Relay.
 *
 * Please refer to the respective .cpp files for documentation on each of the
 * methods provided by these classes.
 */
class Relay
{
public:
	//Relay constructor
	Relay(int pin);
	//Turn on Relay
	void on();
	//Turn off Relay
	void off();
	//Reverse Relay status
	void reverse();
	//Justify if Relay status is on
	boolean isOn();
	//Justify if Relay status is off
	boolean isOff();
	//Return Relay status
	int status();

private:
	//Relay pin No
	int _pin;
};

#endif
