//Zachary Forster Blink LED on GPIO60

#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include "gpio-utils.c"

int main(int argc, char** argv)
{
	//create a variable to store whether we are sending a '1' or a '0'
	char set_value[5]; 
	//Integer to keep track of whether we want on or off
	int toggle = 0;
	int onOffTime;	// Time in micro sec to keep the signal on/off
	int gpio = 60;
	int gpio_fd;

	if (argc < 2) {
		printf("Usage: %s <on/off time in us>\n\n", argv[0]);
		printf("Toggle gpio 60 at the period given\n");
		exit(-1);
	}
	onOffTime = atoi(argv[1]);

	//Using sysfs we need to write the gpio number to /sys/class/gpio/export
	//This will create the folder /sys/class/gpio/gpio60
	gpio_export(gpio);
	//SET DIRECTION
	gpio_set_dir(gpio, "out");
	gpio_fd = gpio_fd_open(gpio, O_RDONLY);
	while(1)
	{
		toggle = !toggle;
		gpio_set_value(gpio, toggle);
		//Pause for a while
		usleep(onOffTime*1000);
	}
	gpio_fd_close(gpio_fd);
	return 0;
}
