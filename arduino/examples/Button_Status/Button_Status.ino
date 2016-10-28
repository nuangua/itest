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


#include <Wire.h>
#include <LCD.h>

#include <Button.h>

Button button(2);
LCD lcd;

void setup()
{
	Serial.begin(9600);
  lcd.begin(16,2);
  lcd.setRGB(0, 255, 0);
}

void loop()
{
  lcd.setCursor(0, 0);
  lcd.print(" Button is: ");
  lcd.println(button.status());
  delay(100);
}
