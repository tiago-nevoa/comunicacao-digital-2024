#include <stdio.h>

void count_bits(int val)
{
	int count0 = 0;
	int count1 = 0;
	unsigned int mask = 1;

	for (int i = 0; i < sizeof(int) * 8; i++)
	{
		if (val & mask)
			count1++;
		else
			count0++;
		mask <<= 1;
	}
	printf("Número de bits a 0: %d\n", count0);
	printf("Número de bits a 1: %d\n", count1);
}
