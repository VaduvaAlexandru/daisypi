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
	

						Info
				
	Found a bug: when inserting a USB Hub the USB rebooted.