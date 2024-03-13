#include <stdio.h>

void count_bits(int val);
void print_fibonacci(int n);
int file_symbol_freq(char *file_name, char symbol);

int main()
{
	int n = 42;
	char my_first_file[] = "test.txt";
	char symbol = 'e';

	printf("\n ------------------ \n");
	printf("\ncount_bits(%d):\n", n);
	count_bits(n);

	printf("\n ------------------ \n");
	printf("\nprint_fibonnaci(%d):\n", n);
	print_fibonacci(n);

	printf("\n ------------------ \n");
	printf("\nfile_symbol_freq('%c') : %d\n", symbol, file_symbol_freq(my_first_file,symbol));
	printf("\n ------------------ \n");

	return 0;
}
