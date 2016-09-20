/*
 * UltrasonicRanger library for Grove UltrasonicRanger v2.0.
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

#ifndef _ULTRASONICRANGER_H_
#define _ULTRASONICRANGER_H_
#include "Arduino.h"


/* 
 *
 * Please refer to the respective .cpp files for documentation on each of the
 * methods provided by these classes.
 */
class UltrasonicRanger
{
public:
	//UltrasonicRanger constructor
	UltrasonicRanger(int pin);
	//Return RotaryAngle value
	int value();



private:
	//UltrasonicRanger pin No
	int _pin;
};

#endif
