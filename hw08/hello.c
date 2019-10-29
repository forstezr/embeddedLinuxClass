#include <stdint.h>
#include <pru_cfg.h>
#include "resource_table_empty.h"
#include "prugpio.h"

volatile register unsigned int __R30;
volatile register unsigned int __R31;

#define GPIO3_SADDR 0x481AE000
#define GPIO0_SET 0x190
#define GPIO1_SET 0x194
#define LED (1<<14) //GPIO3

unsigned int volatile * const GPIO3_CLEAR = (unsigned int *) (GPIO3_SADDR + GPIO0_SET);
unsigned int volatile * const GPIO3_SET   = (unsigned int *) (GPIO3_SADDR + GPIO1_SET);


void main(void) {
	int i;

	uint32_t *gpio1 = (uint32_t *)GPIO1;
	
	/* Clear SYSCFG[STANDBY_INIT] to enable OCP master port */
	CT_CFG.SYSCFG_bit.STANDBY_INIT = 0;

	for(i=0; i<1000000000000; i++) {
		//gpio1[GPIO_SETDATAOUT]   = USR3;			// The the USR3 LED on
		*GPIO3_SET   = LED;

		__delay_cycles(0);    // Wait 1/2 second

		//gpio1[GPIO_CLEARDATAOUT] = USR3;
		*GPIO3_CLEAR   = LED;

		__delay_cycles(0); 

	}
	__halt();
}

// Turns off triggers
#pragma DATA_SECTION(init_pins, ".init_pins")
#pragma RETAIN(init_pins)
const char init_pins[] =  
	"/sys/class/leds/beaglebone:green:usr3/trigger\0none\0" \
	"\0\0";

