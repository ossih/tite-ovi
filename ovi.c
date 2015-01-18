// Read door status from parallel port
// (c) plx 2014

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/io.h>

int addr = 0x37A;					// LPT1 status pins
int pin = 4;						// Define status pin (0..7 -> 0..128 (2^n))

int main(void){
	if(ioperm(addr, 1, 1)){				// Set permissions
		printf("FATAL ERROR\r\n");
		return 1;
	}
	
	int bits = inb(addr);				// Read bits
	
	if((bits & pin) == 0){				// Check if pin is down..
		printf("0\r\n");			// It is down!
	}
	else{						// ..or up?
		printf("1\r\n");			// It is up!
	}
	
	return 0;
}
