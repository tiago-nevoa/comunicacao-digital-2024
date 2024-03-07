#include <stdio.h>
void count_bits( int val );
void print_fibonnaci( int n );

int main()
{
	int n = 42;
	printf("\n ------------------ \n");
	printf("\ncount_bits(%d):\n", n);
	count_bits(n);
	printf("\n ------------------ \n");
	printf("\nprint_fibonnaci(%d):\n", n);
	print_fibonnaci(n);
	printf("\n ------------------ \n");
	return 0;
}
