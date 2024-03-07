#include <stdio.h>

void count_bits( int val )
{
	int count0 = 0;
	int count1 = 0;
	// int in C is 32 bits we start on the most relevant bit
	for(int i = 31; i >= 0; i--)
	{
		if(((val >> i) & 1) == 0) {
			count0++;
		} else {
			count1++;
		}
    }
    printf("bits 0: %d\nbits 1: %d\n", count0, count1);
}
