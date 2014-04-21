/*
    smbus.h - SMBus level access helper functions

    Copyright (C) 1995-97 Simon G. Vogl
    Copyright (C) 1998-99 Frodo Looijaard <frodol@dds.nl>

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
    MA 02110-1301 USA.
*/
/*
    smbus.c - SMBus level access helper functions

    Copyright (C) 1995-97 Simon G. Vogl
    Copyright (C) 1998-99 Frodo Looijaard <frodol@dds.nl>
    Copyright (C) 2012    Jean Delvare <khali@linux-fr.org>

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
    MA 02110-1301 USA.
*/
/*
    smbus.h - SMBus level access helper functions

    Copyright (C) 1995-97 Simon G. Vogl
    Copyright (C) 1998-99 Frodo Looijaard <frodol@dds.nl>

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
    MA 02110-1301 USA.
*/
/*
    smbus.c - SMBus level access helper functions

    Copyright (C) 1995-97 Simon G. Vogl
    Copyright (C) 1998-99 Frodo Looijaard <frodol@dds.nl>
    Copyright (C) 2012    Jean Delvare <khali@linux-fr.org>

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
    MA 02110-1301 USA.
*/

        pres_temp_2.c
/*
Raspberry Pi Bosch BMP085 communication code.
By:      John Burns (www.john.geek.nz)
Date:    13 February 2013
License: CC BY-SA v3.0 - http://creativecommons.org/licenses/by-sa/3.0/

This is a derivative work based on:
    BMP085 Extended Example Code
    by: Jim Lindblom
    SparkFun Electronics
    date: 1/18/11
    license: CC BY-SA v3.0 - http://creativecommons.org/licenses/by-sa/3.0/
    Source: http://www.sparkfun.com/tutorial/Barometric/BMP085_Example_Code.pde

Compile with: gcc -Wall -o testBMP085 ./smbus.c ./testBMP085.c


Circuit detail:
    Using a Spark Fun Barometric Pressure Sensor - BMP085 breakout board
    link: https://www.sparkfun.com/products/9694
    This comes with pull up resistors already on the i2c lines.
    BMP085 pins below are as marked on the Sparkfun BMP085 Breakout board

    SDA -   P1-03 / IC20-SDA
    SCL -   P1-05 / IC20_SCL
    XCLR    -   Not Connected
    EOC -   Not Connected
    GND -   P1-06 / GND
    VCC -   P1-01 / 3.3V
    
    Note: Make sure you use P1-01 / 3.3V NOT the 5V pin.
*/

        poll_1.c
/*
Raspberry Pi Bosch BMP085 communication code.
By:      John Burns (www.john.geek.nz)
Date:    13 February 2013
License: CC BY-SA v3.0 - http://creativecommons.org/licenses/by-sa/3.0/

This is a derivative work based on:
    BMP085 Extended Example Code
    by: Jim Lindblom
    SparkFun Electronics
    date: 1/18/11
    license: CC BY-SA v3.0 - http://creativecommons.org/licenses/by-sa/3.0/
    Source: http://www.sparkfun.com/tutorial/Barometric/BMP085_Example_Code.pde

Compile with: gcc -Wall -o testBMP085 ./smbus.c ./testBMP085.c


Circuit detail:
    Using a Spark Fun Barometric Pressure Sensor - BMP085 breakout board
    link: https://www.sparkfun.com/products/9694
    This comes with pull up resistors already on the i2c lines.
    BMP085 pins below are as marked on the Sparkfun BMP085 Breakout board

    SDA -   P1-03 / IC20-SDA
    SCL -   P1-05 / IC20_SCL
    XCLR    -   Not Connected
    EOC -   Not Connected
    GND -   P1-06 / GND
    VCC -   P1-01 / 3.3V
    
    Note: Make sure you use P1-01 / 3.3V NOT the 5V pin.
*/