/***************************** FILE HEADER ***********************************/
/*!
*  \file    adxl_read.c
*
*  \brief      <b>Demo application that uses adlx345.</b>\n
*
*  \note    
*
*  \author     Rares Plescan
*
*  \version 1.0   2013-08-11 Vaduva Jan Alexandru    created
*
*//**************************** FILE HEADER **********************************/

/******************************************************************************
* Includes
******************************************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>
#include <sys/ioctl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <linux/i2c-dev.h>

/******************************************************************************
 * Defines
 *****************************************************************************/
#define SRF02_I2C_ADDR 0x70
#define ADXL345_I2C_ADDR 0x53

/******************************************************************************
* Local functions
******************************************************************************/
/*!
 *******************************************************************************
 *  selectDevice
 *******************************************************************************
 *
 *  \brief      <b>Selects the I2C device.\n</b>
 *
 *  \param[in]    int      file descriptor
 *  \param[in]    int      device address
 *  \param[in]    int      device name
 *
 *  \author         Rares Plescan
 *
 *  \date           2013-08-12
 ******************************************************************************/
void selectDevice(int fd, int addr, char * name)
{
   if (ioctl(fd, I2C_SLAVE, addr) < 0)
   {
      fprintf(stderr, "%s not present\n", name);
      //exit(1);
   }
}

/*!
 *******************************************************************************
 *  writeToDevice
 *******************************************************************************
 *
 *  \brief      <b>Write to a I2C device.\n</b>
 *
 *  \param[in]    int      file descriptor
 *  \param[in]    int      register used
 *  \param[in]    int      value to be put in register
 *
 *  \author         Rares Plescan
 *
 *  \date           2013-08-12
 ******************************************************************************/
void writeToDevice(int fd, int reg, int val)
{
   char buf[2];

   buf[0] = reg; 
   buf[1] = val;
   
   if (write(fd, buf, 2) != 2)
   {
      fprintf(stderr, "Can't write to ADXL345\n");
      //exit(1);
   }
}


int main(int argc, char **argv)
{
   unsigned char buf[16];
   unsigned int range;
   int count, b, fd;
   short x, y, z;
   float xa, ya, za;
   
   if ((fd = open("/dev/i2c-1", O_RDWR)) < 0)
   {
      /* Open port for reading and writing */
      fprintf(stderr, "Failed to open i2c bus\n");
      exit(1);
   }
   
   /* initialise ADXL345 */
   selectDevice(fd, ADXL345_I2C_ADDR, "ADXL345");

   writeToDevice(fd, 0x2d, 0);
   writeToDevice(fd, 0x2d, 16);
   writeToDevice(fd, 0x2d, 8);
   writeToDevice(fd, 0x31, 0);
   //writeToDevice(fd, 0x31, 11);
   //writeToDevice(fd, 0x31, 1);

   while (1)
   {   
      /* select SRF02 */


      /* select ADXL345 */
      selectDevice(fd, ADXL345_I2C_ADDR, "ADXL345");
      buf[0] = 0x32;
   
      if ((write(fd, buf, 1)) != 1)
      {
         /* Send the register to read from */
         fprintf(stderr, "Error writing to i2c slave\n");
         //exit(1);
      }
   
      if (read(fd, buf, 6) != 6)
      {
         /*  X, Y, Z accelerations */
         fprintf(stderr, "Unable to read from ADXL345\n");
         //exit(1);
      }
      else
      {  
         printf("%d %d %d %d %d %d\n", buf[0], buf[1], buf[2], buf[3], buf[4], buf[5]);
         x = buf[1]<<8 | buf[0];
         y = buf[3]<<8 | buf[2];
         z = buf[5]<<8 | buf[4];
        
         xa = (90.0 / 256.0) * (float) x;
         ya = (90.0 / 256.0) * (float) y;
         za = (90.0 / 256.0) * (float) z;
         printf("x=%d, y=%d, z=%d\n", x, y, z);
         //printf("%4.0f %4.0f %4.0f\n", xa, ya, za);
         //for (b=0; b<6; b++) printf("%02x ",buf[b]); printf("\n");
      }
      //usleep(900000);
      usleep(90000);
   }
   
   return 0;
}
