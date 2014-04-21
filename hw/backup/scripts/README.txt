This README file has all the steps of the implementation taken in the process of building Daisy Pi device drivers that reads the information registered by this devices and sends it to the output in a friendly format so it can be easely processed by cron and periodicaly submited in COSM or any other external application. For that we suggest the DaisyPI cloud application.

Enable watchdog:
	$ sudo modprobe bcm2708_wdog
	$ echo "bcm2708_wdog" | sudo tee -a /etc/modules
	$ sudo apt-get install watchdog
	$ sudo update-rc.d watchdog defaults
	$ sudo nano /etc/watchdog.conf
		Uncomment the line that starts with #watchdog-device
		Uncomment the line that says #max-load-1 = 24
	$ sudo /etc/init.d/watchdog start
	
	You are done! You may play around with the settings in /etc/watchdog.conf if you'd like.
	For a fork-bomb test use: ":(){:|:&};:"
	
Enable Webcam:
	$ mkdir workspace
	$ cd workspace
	$ svn co https://mjpg-streamer.svn.sourceforge.net/svnroot/mjpg-streamer mjpg-streamer
	$ sudo apt-get install libjpeg8-dev
	$ sudo apt-get install imagemagick
	$ cd mjpg-streamer/mjpg-streamer
	$ make
	$ ./mjpg_streamer -i "./input_uvc.so -n -f 15 -r 1280x960" -o "./output_http.so -n -w ./www"

Enable SPI Driver functionality:
	Install wiringPi and test it with: "gpio -v".
	Write SPI driver for ADC temperature read.

Command line changes for the DaisyPi project, both setup and devel related.

1. Expanded filesystem
2. Installed midnight commander
3. Installed bc ( math cli utility )
4. Created folder /daisypi (main installation folder for the project )
5. Created customized examples from Adafruit/modified by http://www.john.geek.nz/ for I2C sensors ( SHT11 and BMP085 ).
	

						Info
				
	Found a bug: when inserting a USB Hub the USB rebooted.