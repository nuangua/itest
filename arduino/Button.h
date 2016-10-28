/*
 * LED library for Grove Button v1.1.
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

#ifndef _BUTTON_H_
#define _BUTTON_H_
#include "Arduino.h"

/* Note that this Button provides interface functions to help you better control and manage button.
 *
 * Please refer to the respective .cpp files for documentation on each of the
 * methods provided by these classes.
 */
class Button
{
public:
	//Button constructor
	Button(int pin);
	//Justify if button status is on
	boolean isOn();
	//Justify if button status is off
	boolean isOff();
	//Return button status
	int status();

private:
	//button pin No
	int _pin;
};

#endif
