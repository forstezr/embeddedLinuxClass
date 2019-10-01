#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h> 
#include <signal.h>    // Defines signal-handling functions (i.e. trap Ctrl-C)

#define GPIO0_SA 0x44E07000 //gpio start address
#define GPIO0_EA 0x44E09000 //end address
#define GPIO0_SIZE (GPIO0_EA - GPIO0_SA)

#define GPIO1_SA 0x4804C000 //gpio start address
#define GPIO1_EA 0x4804E000 //end address
#define GPIO1_SIZE (GPIO1_EA - GPIO1_SA)

#define GPIO_DATAIN 0x138
#define GPIO_CLEAR  0x190
#define GPIO_SET    0x194

#define USR2 (1<<23)
#define USR3 (1<<24)

#define butt1 (1<<17) //17th pin of gpio1
#define butt2 (1<<15) //15th pin of gpio0

void signal_handler(int sig);
int keepGoing = 1;

void signal_handler(int sig){
    printf("\nExiting and cleaning up\n");
    keepGoing = 0;
}


void main() {
    volatile void *gpio1_addr;
    volatile unsigned int *gpio1_datain;
    volatile unsigned int *gpio1_setdataout_addr;
    volatile unsigned int *gpio1_cleardataout_addr;
    
    volatile void *gpio_addr;
    volatile unsigned int *gpio_datain;

    // Set the signal callback for Ctrl-C
    signal(SIGINT, signal_handler);

    int fd = open("/dev/mem", O_RDWR);

    gpio_addr = mmap(0, GPIO0_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 
                        GPIO0_SA);
                        
    gpio1_addr = mmap(0, GPIO1_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 
                        GPIO1_SA);

    gpio1_datain            = gpio1_addr + GPIO_DATAIN;
    gpio1_setdataout_addr   = gpio1_addr + GPIO_SET;
    gpio1_cleardataout_addr = gpio1_addr + GPIO_CLEAR;
    
    gpio_datain           = gpio_addr + GPIO_DATAIN;

    if(gpio1_addr == MAP_FAILED) {
        printf("Unable to map GPIO\n");
        exit(1);
    }
    printf("GPIO mapped to %p\n", gpio1_addr);
    printf("GPIO SETDATAOUTADDR mapped to %p\n", gpio1_setdataout_addr);
    printf("GPIO CLEARDATAOUT mapped to %p\n", gpio1_cleardataout_addr);
    while(keepGoing) {
        *gpio1_setdataout_addr= butt1;
        //usleep(200);
        *gpio1_cleardataout_addr = butt1;
        //usleep(200);
    }

    munmap((void *)gpio_addr,  GPIO0_SIZE);
    munmap((void *)gpio1_addr, GPIO1_SIZE);
    close(fd);
}